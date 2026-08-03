# argparse — Complete Reference (from the PS1 code review) Day 27

A structured reference covering everything encountered with `argparse` while reviewing `regex-file-kit`, with real examples from the code and actual test results.

---

## 1. Basics

```python
import argparse

parser = argparse.ArgumentParser(description="A regex helper for finding things in text.")
args = parser.parse_args()
```

- `ArgumentParser()` builds the parser.
- `description` shows up in `--help`.
- `parse_args()` returns a `Namespace` object — access values with `args.argument_name`.

---

## 2. Types: Positional vs Optional

| Type | Form | Required by default? |
|---|---|---|
| **Positional** | `parser.add_argument("directory")` | ✅ Always required |
| **Optional** | `parser.add_argument("--dir")` | ❌ Optional unless `required=True` |

Example from the code:
```python
parser.add_argument("--dir", required=True, type=str, help="The file path")
```
`--dir` is optional by nature (the `--` prefix), but `required=True` forces the user to provide it anyway.

---

## 3. `type`, `default`, `required`, `choices`

```python
parser.add_argument("--mn_size", type=float, help="Min size to search", required=True)
parser.add_argument("--count", type=int, help="how many to get back", default=1)
parser.add_argument("--find", choices=["urls", "ips", "emails", "hashes"], required=True)
```

- `type=` automatically converts the incoming command-line string to the given type (and rejects the value if it can't be converted).
- `default=` is used when the argument is never provided.
- `choices=` restricts allowed values — argparse automatically rejects anything else with a clear error message.

---

## 4. `action="store_true"` — Flags

```python
parser.add_argument("-v", "--verbose", action="store_true", help="for showing the logs")
```

No `type`, no value after it — just including it on the command line sets `args.verbose = True`; leaving it out sets `False`. Used for on/off flags like `--summary` in `log_extractor.py`.

---

## 5. `nargs` — and its gotcha

`nargs="?"` means the argument can take zero or one value.

```python
parser.add_argument("--cext", default=None, const="*", nargs="?")
```

- `--cext` (with no value) → takes `const` (here `"*"`)
- `--cext py` → takes `"py"`
- `--cext` not given at all → takes `default` (here `None`)

### ⚠️ The trap we actually ran into

```python
parser_recent_files.add_argument("--days", type=int, nargs="?", required=True, const=7)
```

`required=True` + `nargs="?"` together mean: **`--days` must be typed (even with no value)**, but it won't auto-activate if omitted entirely. That means any `default=` set inside the function itself (e.g. `def find_recent_files(directory, days=7)`) becomes **dead code** — it can never actually fire through the CLI, because argparse itself will refuse to run the program at all if `--days` is missing.

**If you actually want `--days` to be optional and default to 7 when omitted:**
```python
parser_recent_files.add_argument("--days", type=int, default=7, help="Days to search")
# no required, no nargs="?"
```

---

## 6. Subparsers — Subcommands (like `git commit`, `git push`)

```python
sub_commands = parser.add_subparsers(dest="command", description="Adding some functions")

parser_walk = sub_commands.add_parser("walk", help="listing file names in the file path")
parser_walk.add_argument("--ext", type=str, default=None)
parser_walk.add_argument("--count", type=int, default=1)
```

- `dest="command"` → after parsing, `args.command` holds the name of the chosen subcommand (e.g. `"walk"`).
- Each subcommand has its own arguments, completely separate from the other subcommands.
- Without `required=True` on `add_subparsers()`, the program can run with no subcommand at all (`args.command = None`).

---

## 7. ⚠️ The most important trap: argument order with subparsers

This was the single biggest lesson from the whole review — confirmed by actual testing, not just reading.

### Why it happens

Once argparse reaches a subcommand keyword (like `walk`), it hands off **everything after it** entirely to that subcommand's own parser, and never goes back to try matching any parent-level optional arguments (like `--dir`) that appear after that point.

### The proof (tested directly)

```bash
# ❌ Fails — even though --dir is right there in the command!
$ python filescanner.py walk --dir . --count 2
error: the following arguments are required: --dir

# ✅ Works — because --dir comes before the subcommand
$ python filescanner.py --dir . walk --count 2
```

### The practical rule

> **Any optional argument belonging to the parent parser must be typed before the subcommand name, not after.**

This is general `argparse` behavior — not a strange bug or something specific to one project — and should always be documented (in `--help` or the README) for any CLI that combines subparsers with parent-level options.

---

## 8. `parents=` — Merging existing parsers

```python
parser_file = subparsers.add_parser("scan", parents=[parser_scanner()], add_help=False)
```

Lets you take a whole existing parser (with all its arguments) and use it as a "parent" for another parser, instead of redefining the same arguments twice.

### The trap we discovered

If the parser you pass as `parents=` itself contains subparsers inside it (like `parser_scanner()`, which has `walk`/`largefiles`/`rfiles`), it will carry over **all** of the trap from Section 7 as well — meaning that trap isn't just present in the original file (`filescanner.py`), it automatically propagates into any unified CLI that uses `parents=` on it.

**Tip:** if the parser you're passing as a parent has subparsers inside it, assume the same "order matters" rule still applies, and test it yourself before considering it done.

### An additional possible trap: reusing the same `dest`

If you use `dest="command"` at more than one level (a top-level parser + a subparser nested inside it), both will write into the same `args.command` — the most recent (deepest) value wins. If you need to distinguish between the levels, use different `dest` names, e.g. `dest="tool"` at the top level and `dest="action"` at the nested level.

---

## 9. `add_help=False` with `parents=`

```python
subparsers.add_parser("scan", parents=[parser_scanner()], add_help=False, description="...")
```

If the parser you're using as a parent was itself created with `add_help=True` (the default), it already has `-h` built in. If the new subparser also tries to add `-h` (the default behavior), you'll get a conflict (`conflicting option string`). `add_help=False` here prevents the subparser from trying to add `-h` a second time, letting the inherited `-h` from the parent work instead.

---

*This reference was built from real observations and actual testing while reviewing the `regex-file-kit` project (PS1) — not just from the official docs.*
