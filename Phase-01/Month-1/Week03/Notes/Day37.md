# Development Notes — FilePermissionsChecker (PS3)

Documentation of the issues encountered while building this project, the fixes, and the reasoning behind each decision. Source: a conversation with Gemini + a live-testing session.

---

## 1. The `~` (Tilde) Problem with `Path`

**The problem:**
```python
test.suid_find("~")
```
Doesn't work, even though `~` is supposed to expand to the home directory.

**Why:**
- `Path("~")` in `pathlib` does **not** expand `~` automatically — it treats it as a literal directory name.
- If you use `subprocess` with `find` and `shell=True`, wrapping the path in an f-string (`f"find {Path(directory)}"`) also breaks the shell's own tilde expansion, so that route doesn't fix it either.

**The fix:**
```python
target_dir = Path(directory).expanduser().resolve()
```
- `.expanduser()` converts `~` into the full path (`/home/username`)
- `.resolve()` converts any relative path into an absolute, unambiguous one

---

## 2. Relying on `subprocess` + `find` Instead of Pure Python

**Original approach:** a line like:
```python
subprocess.check_output(f"find {Path(directory)} -perm -4000 2> /dev/null", shell=True, text=True)
```
to fetch SUID files — except the resulting variable (`suid_files`) was **never actually used**; the real logic ended up relying on `stat.filemode()` inside `scan()` instead.

**Decision:** drop `subprocess` entirely and rely fully on the `stat` module. Reasons:
- Pure Python = portable and easier to test
- Relying on external shell commands (`find`) opens the door to shell-injection issues if the input isn't validated
- `stat.filemode()` gives the same information without needing to parse text output from an external process

---

## 3. Checking SUID by String Comparison Instead of Bitmask — First Real Bug

**Original code:**
```python
"s" == file_permission[3]
```

**The problem:** this checks character index 3 of the string returned by `stat.filemode()` (e.g. `-rwsr-xr-x`), and requires it to be a **lowercase** `s`.

**But there's an edge case:** if a file has the SUID bit set, but the owner has **no execute permission**, that character becomes an **uppercase** `S` instead. Verified with real test files:

| Permissions | String | SUID actually set? | Old code said |
|---|---|---|---|
| `chmod 4755` | `-rwsr-xr-x` | ✅ | ✅ Correct |
| `chmod 4655` | `-rwSr-xr-x` | ✅ | ❌ **Wrong — missed it** |

**First fix (string-based):**
```python
"s" == file_permission[3].lower()
```
Covers both cases (`s` and `S`).

**Better alternative (suggested by Gemini, more technically precise):**
```python
is_suid = bool(mode & stat.S_ISUID)
```
Checking the bitmask directly on `st_mode` instead of relying on a string interpretation — more accurate and doesn't depend on the exact character layout of `filemode()`.

---

## 4. Checking "World-Writable" — a Second Real Bug, Fixed in Two Stages

**First attempt:**
```python
file_permission[1:] == "rwxrwxrwx"
```
Requires an exact match of the entire string. Any file with SUID/SGID/sticky bits changes the string's shape (`rwsrwxrwx` instead of `rwxrwxrwx`), so files that **are** genuinely world-writable get missed.

**Second attempt:**
```python
file_permission.count("rw") == 3
```
Better, but still has a gap: it looks for the adjacent substring `"rw"`. If a file has write without read (e.g. `-w-`) in the "other" group, it won't be caught even though it's genuinely world-writable.

| File | Permissions | Actually world-writable? | `count("rw")==3` |
|---|---|---|---|
| `write_only_others.sh` | `-rwx---rwx` | ✅ | ❌ Missed |
| `tricky_perm.sh` | `-rw-rw--w-` | ✅ | ❌ Missed |

**Final fix:**
```python
file_permission[8] == "w"
```
`stat.filemode()` returns a fixed 10-character string with a stable layout:

```
index:   0     1 2 3     4 5 6     7 8 9
char:    type  owner     group     other
               r w x     r w x     r w x
```

The **"other" write bit** (i.e., can anyone on the system write to this file?) always sits at **index 8**, regardless of what index 9 looks like (it could be `x`, or `s`/`S`, or `t`/`T` depending on other special bits). Relying on a fixed index instead of pattern-matching the whole string fixes the problem completely.

**Verified by testing** that this catches every case: plain `777`, `777` + SUID, `777` + sticky bit, and world-writable-without-world-readable — while correctly excluding a file with a sticky bit but no actual write permission.

---

## 5. `argparse` — the `--count` / `--check` Logic

**The goal:** `--count` should only work alongside `--dir`, and should be rejected if used together with `--check`.

**The original bug:** with `--count` set to `default=10`, the condition:
```python
if args.count and args.command is not None:
```
is **always** `True` — even if the user never typed `--count` — because argparse fills in `10` automatically, so it's never `None`.

**The fix:** remove `default=10` from the argument definition (leave it `None` if the user didn't provide it), and apply the default value (10) inside `main()` only at the point of actual use, when `--check` isn't present.

**A cleaner alternative (suggested):** use `subparsers`, so each subcommand only accepts the arguments that are valid for it, and argparse automatically rejects any invalid combination without needing a manual `if` check.

---

## 6. Why the Class Doesn't Inherit from `SecurityToolkit`

After reviewing the actual content of `SecurityToolkit`, the decision was made that inheriting from it wouldn't add real value to `FilePermissionsChecker` — the same conclusion reached earlier with the Password Manager project (Week 6), where a `SecurityToolkit` inheritance audit confirmed it added no meaningful value to that domain either.

**Note for the future:** this decision needs to be based on an actual review of the class's contents (not an assumption), and could be revisited if `SecurityToolkit` gains shared functionality (like unified logging or a common timestamp/report format) that would genuinely benefit every tool inheriting from it.

---

## Quick Summary of Lessons Learned

1. **Relying on a bitmask (`st_mode & stat.S_ISUID`) is more precise than interpreting a permission string.**
2. **When checking a permission in a system with a fixed structure (like `rwxrwxrwx`), use the direct index rather than pattern-matching the whole string** — the index reflects the actual meaning, while substring matching assumes one specific shape and breaks with any variation.
3. **Code that "runs without errors" doesn't mean it's correct** — real testing against edge cases (like SUID without execute, or world-writable without world-readable) is what reveals silent false negatives.
4. **argparse defaults can silently break validation logic** if their effect on `is not None` checks isn't considered.