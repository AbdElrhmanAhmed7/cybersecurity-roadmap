# Summary Ch 7 — Seeing the World as the Shell Sees It (Expansion & Quoting)
> The book calls this "one of the most important subjects to learn about the shell" — and it's true. Every wildcard, every `~`, every `$VAR` you've used since Ch4 has actually been an *expansion*. This chapter finally explains the machinery behind all of it.

---

## The Core Idea: Expansion
Every time you press Enter, bash rewrites parts of your command line **before** the command ever runs. The command itself never sees the raw symbols (`*`, `~`, `$VAR`) — only the expanded result.

```bash
echo *
```
`echo` never sees `*` — the shell replaces it with the actual filenames in the current directory *first*, and `echo` just prints whatever it was handed.

---

## 1. Pathname Expansion (the formal name for wildcards from Ch4)
```bash
echo D*              # anything starting with D
echo *s               # anything ending with s
echo [[:upper:]]*     # anything starting with an uppercase letter
```
**Hidden files:** `*` never matches files starting with `.`. `.*` will match them but may also include `.` and `..` themselves (depends on the `globskipdots` shell option — default-on since bash 5.2). The safe, version-independent pattern is:
```bash
echo .[!.]*     # hidden files only, excludes . and ..
ls -A            # or just use this instead
```

---

## 2. Tilde Expansion
```bash
echo ~          # → /home/yourusername
echo ~bob       # → /home/bob (another user's home dir)
cd ~sara        # actually navigates into sara's home directory
```

---

## 3. Arithmetic Expansion
```bash
echo $((expression))
```
| Operator | Meaning |
|---|---|
| `+` `-` `*` | standard |
| `/` | integer division only — **no decimals**, result is truncated |
| `%` | modulo (remainder) |
| `**` | exponentiation |

```bash
echo $((10 / 3))    # → 3 (not 3.33 — integers only)
echo $((10 % 3))    # → 1
echo $((2 ** 4))    # → 16
```
Same behavior as integer arithmetic in C — no floats, results get truncated not rounded.

---

## 4. Brace Expansion — turns one pattern into multiple strings
```bash
echo Front-{A,B,C}-Back
# → Front-A-Back  Front-B-Back  Front-C-Back
```
| Type | Example | Result |
|---|---|---|
| Comma list | `{A,B,C}` | A B C |
| Integer range | `{1..5}` | 1 2 3 4 5 |
| Zero-padded range | `{01..15}` | 01 02 ... 15 |
| Letter range | `{a..e}` | a b c d e |
| Reverse range | `{Z..A}` | Z Y X ... A |

**Real use case (from your roadmap):**
```bash
mkdir -p ~/security/{tools,logs,reports}
```
Expands to `~/security/tools ~/security/logs ~/security/reports` *before* `mkdir` runs — creates all 3 directories (plus `security` itself, thanks to `-p`) in one command.

```bash
mkdir {2007..2009}-{01..12}   # two braces combine → 36 directories at once
```

---

## 5. Parameter Expansion — reading variables
```bash
echo $USER      # prints your username
echo $HOME      # same result as echo ~
```
⚠️ **Silent failure trap:** misspelling a variable name doesn't error — it just returns an empty string.
```bash
echo $SUER      # (prints nothing, no warning)
```
Variables are **case-sensitive** just like everything else in bash — `$HOME` ≠ `$home`. Uppercase for system variables is just convention, not a hard rule.

To list all available variables: `printenv | less`

---

## 6. Command Substitution — using a command's output as part of another command
```bash
$(command)      # modern syntax
`command`       # older backtick syntax, still works
```
```bash
ls -l $(which cp)      # runs `which cp` first, gets /bin/cp, then runs ls -l /bin/cp
echo "Today is $(date)"
```
**Key distinction:** `echo $(whoami)` actually *executes* `whoami` and prints its output. `echo whoami` (no `$()`) just prints the literal word `whoami` — without `$()`, the shell never tries to run anything, it treats it as plain text.

---

## Quoting — controlling when expansion happens

**Why you need it:**
```bash
echo The total is $100.00
# → The total is  00.00        (the shell tried to expand $1 as a variable — empty)

ls -l two words.txt
# → error: treats "two" and "words.txt" as two separate arguments (word-splitting)
```

### Double Quotes `" "`
Suppresses **most** expansions, but keeps 3 working: `$` (parameter expansion), `` `command substitution` ``, and `\` (backslash).

| Suppressed inside `" "` | Still active inside `" "` |
|---|---|
| Word-splitting | Parameter expansion (`$VAR`) |
| Pathname expansion (`*`, `?`) | Command substitution (`$()`) |
| Tilde expansion (`~`) | Backslash escapes |
| Brace expansion (`{}`) | |

```bash
ls -l "two words.txt"          # fixes the spaces problem
echo "$USER lives in $HOME"    # still expands correctly
echo "Front-{A,B,C}-Back"      # brace expansion is now suppressed — prints literally
```

**Subtle but important:** double quotes preserve newlines from command substitution.
```bash
echo $(df -h)      # newlines get word-split away → one messy long line
echo "$(df -h)"     # newlines preserved → readable, formatted output
```

### Single Quotes `' '` — suppresses absolutely everything, no exceptions
```bash
echo 'text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER'
# → text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER     (all printed literally, nothing expanded)
```

| Quoting level | Suppresses |
|---|---|
| None | Nothing — everything expands |
| `" "` Double | Everything **except** `$`, command substitution, and `\` |
| `' '` Single | **Everything**, no exceptions |

**Security-relevant use case:** when passing regex patterns to `grep` (later, Ch19), single quotes are essential — otherwise the shell tries to expand `*`, `$`, `[]` as pathname/parameter expansion *before* `grep` ever sees the pattern, corrupting it.
```bash
grep '^[0-9]*$' file.log     # single quotes protect the regex syntax from the shell
```

### Escaping Characters — `\` for a single character
Use when you only need to protect one character, often inside double quotes:
```bash
echo "The balance is: \$5.00"      # → The balance is: $5.00
mv bad\&filename good_filename      # escapes & in a filename (prevents background-execution interpretation)
```
Inside single quotes, `\` loses its special meaning entirely and is treated as a literal character.

---

## 🔐 Why This Chapter Matters for Security Work
- Regex patterns, wildcards, and paths passed to security tools **must** be quoted correctly or the shell silently mangles them before the tool ever runs
- `&` in a filename/command left unquoted gets interpreted as "run in background" — a classic scripting bug
- Command substitution (`$(...)`) is how you chain recon commands together, e.g. `nmap $(cat targets.txt)`
- Brace expansion is a fast way to generate wordlists or bulk directory structures for testing/organizing scan output

---

## ⚠️ Intentionally Left Out (not needed right now)
- Backslash escape sequences table (`\a`, `\b`, `\n`, `\r`, `\t`) — recognize them if you see them, not urgent to memorize
- Arithmetic expansion's full operator set (bit operations, logic) — deeper coverage in Ch34
- Full nested brace expansion edge cases beyond the basics shown above

---

## 🎯 What You Should Be Able to Recall After Today
1. **Expansion happens before the command runs — the command never sees the raw symbol, only the result**
2. Pathname expansion is the formal name for wildcards (`*`, `?`, `[abc]`, character classes)
3. `~` and `~username` expand to home directories
4. Arithmetic expansion `$((...))` — integers only, `/` truncates, `%` is remainder, `**` is exponent
5. Brace expansion `{a,b,c}` / `{1..5}` generates multiple strings from one pattern — huge time-saver for bulk `mkdir`/file naming
6. `$VAR` reads a variable; misspelling one fails silently (empty string, no error)
7. `$(command)` runs a command and substitutes its output; without it, text is just literal text
8. **Double quotes block most expansion but keep `$`, `` ` ``, and command substitution alive; single quotes block everything, no exceptions**
9. Double quotes preserve newlines from command substitution — unquoted `$()` gets mangled by word-splitting
10. Why unquoted `$1`, spaces in filenames, and `&` in filenames cause silent, confusing bugs
11. `\` escapes a single character; loses meaning entirely inside single quotes
