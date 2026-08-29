# 🚀 Linux Part 4 Basics — Quick Refresh
> A quick summary after exercises. Read once before you sleep.

## Ch 24 — Your First Script

| Concept | Example |
|---|---|
| Shebang | `#!/bin/bash` on the first line |
| Execution permission | `chmod +x script.sh` |
| Run | `./script.sh` (if in the same directory) |
| Where to put it | `~/bin/` → automatically added to `PATH` in most distros |
| Long options in scripts | `--all` instead of `-a` (clearer for the reader) |

---

## Ch 25 — Variables & Constants

```bash
NAME="target"           # variable
readonly PI=3.14      # constant (rarely used)
DATE=$(date +%F)      # command substitution
FILE="${NAME}.txt"    # braces when something follows directly
```

### Here Document
```bash
cat << EOF
Line 1
Line 2
EOF
```
- Useful for printing multi-line text
- If you use `<< 'EOF'` → no expansion will happen (literal)

---

## Ch 27 — if / test / [[ ]]

### Syntax
```bash
if [ "$VAR" == "value" ]; then
    # something
elif [ "$VAR" == "other" ]; then
    # something else
else
    # default
fi
```

### test Expressions (the ones you'll actually use)
| Expression | Meaning |
|---|---|
| `-e FILE` | exists? |
| `-f FILE` | regular file? |
| `-d FILE` | directory? |
| `-r FILE` | readable? |
| `-w FILE` | writable? |
| `-x FILE` | executable? |
| `-s FILE` | not empty? |
| `"$A" == "$B"` | strings equal? |
| `"$N" -eq 5` | numbers equal? |
| `"$N" -gt 5` | greater than? |
| `"$N" -lt 5` | less than? |

### Modern: [[ ]] and (( ))
```bash
[[ "$FILE" == *.txt ]]      # pattern matching
[[ "$NUM" =~ ^[0-9]+$ ]]  # regex
(( NUM > 5 ))               # arithmetic (without $)
```

### Logical Operators
```bash
[ -f "$F" ] && echo "exists"     # AND
[ -f "$F" ] || echo "missing"    # OR
```

---

## Ch 29 — while / until

```bash
# while: continues as long as condition is true
count=1
while [ "$count" -le 5 ]; do
    echo "$count"
    count=$((count + 1))
done

# until: continues until condition becomes true (opposite of while)
until [ -f "done.txt" ]; do
    echo "Waiting..."
    sleep 1
done

# read from file
while read -r line; do
    echo "$line"
done < file.txt
```

### break / continue
- `break` → stops the loop entirely
- `continue` → skips the current iteration and goes to the next one

---

## Ch 33 — for Loop

```bash
# 1. List
for i in A B C; do echo "$i"; done

# 2. Brace expansion
for i in {1..5}; do echo "$i"; done

# 3. Files
for f in *.txt; do echo "$f"; done

# 4. Command substitution
for ip in $(cat targets.txt); do ping -c 1 "$ip"; done

# 5. C-style
for (( i=0; i<5; i++ )); do echo "$i"; done
```

---

## Ch 26 — Functions (Quick)

```bash
my_func() {
    local name="$1"   # local variable
    echo "Hello $name"
}

my_func "World"
```
- `local` → variable inside the function only (like `nonlocal` in Python but reversed)
- `$1`, `$2`, ... → arguments (like `sys.argv` in Python)

---

## Ch 28 — read (Quick)

```bash
read -p "Enter target IP: " IP
echo "Scanning $IP..."

# read multiple values
read -r ip port < targets.txt
```

---

## ⚠️ Intentionally Left Out (not needed right now)

| Chapter | Why skipped? |
|---|---|
| **Ch 13** (Prompt) | Cosmetic — unrelated to security |
| **Ch 30** (Troubleshooting) | `set -e`, debugging — when your scripts grow |
| **Ch 31** (case) | `case` statement — when you build CLI menus |
| **Ch 32** (Positional Params) | `$1`, `$@`, `getopts` — when you build CLI tools |
| **Ch 34** (Strings & Numbers) | Advanced parameter expansion — rare |
| **Ch 35** (Arrays) | Arrays in bash — complex and rare in simple scripts |
| **Ch 36** (Exotica) | eval, traps, named pipes — very advanced |

---

## ✅ Today's Checklist (Tick Off)

- [ ] Read Ch 14 (Package Management) — 15 minutes
- [ ] Finished the 5 exercises
- [ ] Understood: variable → if → for → while → function
- [ ] Wrote `backup.sh` and it worked

---

> **"You don't need to be a bash expert. You need to be able to write 20 lines to automate any command you repeat more than twice."**
