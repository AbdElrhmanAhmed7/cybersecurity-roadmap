# W06 Notes — `subprocess` Module + PasswordVault Enhancements - Day32

> Quick reference for running external commands in Python and extending the PasswordVault project.

---

## Part 1: `subprocess` Module

### `subprocess.run()`

Executes an external command and returns a `CompletedProcess` object.

Key attributes:

| Attribute | Description |
|-----------|-------------|
| `returncode` | Exit status (`0` = success) |
| `stdout` | Standard output captured |
| `stderr` | Standard error captured |

```python
import subprocess

result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.returncode)
print(result.stdout)
```

---

### `subprocess.check_output()`

Executes a command and returns **only the output**.

- Raises `CalledProcessError` if the command exits with a non-zero status.
- Returns `bytes` by default (use `text=True` for strings).

```python
output = subprocess.check_output(["echo", "hello"], text=True)
```

---

### `capture_output=True`

Instead of printing command output to the terminal, captures it into:

- `result.stdout`
- `result.stderr`

```python
result = subprocess.run(["ping", "-c", "4", "8.8.8.8"], capture_output=True, text=True)
print(result.stdout)
```

---

### `text=True`

| Without `text=True` | With `text=True` |
|---------------------|------------------|
| `stdout` → `bytes` | `stdout` → `str` |

Equivalent to the legacy parameter `universal_newlines=True`.

```python
# Without text=True
result = subprocess.run(["echo", "hi"], capture_output=True)
print(type(result.stdout))  # <class 'bytes'>

# With text=True
result = subprocess.run(["echo", "hi"], capture_output=True, text=True)
print(type(result.stdout))  # <class 'str'>
```

---

### `shell=False` (Default & Safest)

- Prevents many **Command Injection** vulnerabilities.
- Executes the program directly without invoking the system shell.
- **Preferred whenever possible.**

```python
subprocess.run(["ls", "-la"])  # shell=False by default
```

---

### `shell=True`

Runs the command through the system shell.

**Use only when necessary**, such as:

- Windows built-in commands (`start`, `dir`, ...)
- Complex shell features (pipes `|`, redirection `>`, wildcards `*`)

⚠️ **Be extremely careful with untrusted user input.**

```python
subprocess.run('ls -la | grep python', shell=True)
```

---

### `subprocess` on Windows

`start` is **not** an executable — it is a built-in `cmd.exe` command.

Correct usage:

```python
subprocess.run(f'start "" "{url}"', shell=True)
```

> The empty quotes `""` represent the window title (required by `start`).

---

## Part 2: PasswordVault Enhancements

### `backup(backup_dir)`

Responsibilities:

1. Create the backup directory if it doesn't exist.
2. Generate a **timestamped filename**.
3. Copy the vault file using `shutil.copy2()`.

**Example filename:**

```
vault_2026-08-06_18-42-11.json
```

```python
from datetime import datetime
import shutil
from pathlib import Path

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_path = Path(backup_dir) / f"vault_{timestamp}.json"
shutil.copy2(self.vault_path, backup_path)
```

---

### `open_browser()`

Responsibilities:

1. Validate the URL.
2. Open the browser using `subprocess`.

```python
import subprocess
import sys

if sys.platform == "win32":
    subprocess.run(f'start "" "{url}"', shell=True)
elif sys.platform == "darwin":
    subprocess.run(["open", url])
else:
    subprocess.run(["xdg-open", url])
```

---

### URL Validation

Compile the regex **once** at module level for better performance.

**Preferred:**

```python
import re

URL_REGEX = re.compile(
    r"^(https?|ftp)://"              # protocol
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+"  # subdomains
    r"(?:[A-Z]{2,6}|[A-Z0-9-]{2,})"  # TLD
    r"|localhost"                     # localhost
    r"|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # IP
    r"(?::\d+)?"                     # optional port
    r"(?:/?|[/?]\S+)$", re.IGNORECASE)
```

**Avoid:** Compiling the regex inside every function call.

---

### CLI Arguments

Example command:

```bash
python vault.py --backup D:\Backups
```

Parser setup:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--backup", help="Directory to store backup files")
args = parser.parse_args()
```

> Since `--backup` receives a **path value**, do **not** use `action="store_true"`.

| Action | Use Case |
|--------|----------|
| No action (default) | Receives a value (e.g., `--backup path`) |
| `action="store_true"` | Flag only (e.g., `--verbose`) |

---

## Part 3: Design Principles

### Separate Business Logic from UI

**Avoid:**

```python
class PasswordVault:
    def some_method(self):
        print("Success!")  # ❌ mixed concerns
```

**Prefer:**

```
PasswordVault
    └── return values / raise exceptions  ✅ business logic

CLI / GUI / API
    └── print(...) / display(...)         ✅ presentation layer
```

| Benefit | Description |
|---------|-------------|
| Separation of concerns | Each layer has one job |
| Easier testing | Test logic without UI side effects |
| Reusability | Same vault works with CLI, GUI, or API |

---

## Best Practices Summary

| Practice | Why It Matters |
|----------|----------------|
| Prefer `Path` over string paths | Cross-platform compatibility, cleaner API |
| Use `copy2()` instead of `copy()` | Preserves file metadata (timestamps, permissions) |
| Compile regex once | Avoids recompiling on every call — better performance |
| Avoid repeating computations | Cache `value.lower()` instead of calling it repeatedly |
| Add type hints | Improves readability and IDE support |
| Keep methods focused | Single responsibility = easier to test and maintain |
| Use `shell=False` by default | Prevents command injection attacks |
| Validate URLs before opening | Prevents unexpected or malicious navigation |

---

> These notes cover the `subprocess` module and PasswordVault enhancements needed for the project.
