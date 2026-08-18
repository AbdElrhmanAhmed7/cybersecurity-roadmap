# File Permissions Checker

A Python command-line tool for auditing file permissions on Linux/Unix systems — it looks for **SUID** files and **world-writable** files (files any user on the system can modify), which are among the most common checks in a basic security audit.

> ⚠️ **This tool is built on Unix/Linux concepts (the SUID bit, the Unix permission model) and runs on Linux, macOS, or WSL only. It will not work correctly on plain Windows.**

---

## Requirements

- Python 3.8+
- Linux, macOS, or WSL (Windows Subsystem for Linux)

On Windows, you'll need WSL — Windows' permission system (ACLs) is fundamentally different from the Unix owner/group/other model this tool is built around, and the concept of a SUID bit doesn't exist on Windows at all.

---

## Usage

### General scan (first N files in a directory)

```bash
python checker.py --dir /etc
```

Returns the first 10 files by default (path, permissions, is_suid). To change the count:

```bash
python checker.py --dir /etc --count 20
```

### Find SUID files

```bash
python checker.py --dir /usr/bin --check suid
```

### Find world-writable files

```bash
python checker.py --dir /tmp --check writable
```

### Save the result to a JSON file

```bash
python checker.py --dir /usr/bin --check suid --output report.json
```

> Note: `--count` only works alongside `--dir` and is rejected if combined with `--check` in the same command.

---

## Structure

```python
class FilePermissionsChecker:
    def scan(self, directory)        # generator: (path, permissions, is_suid)
    def suid_find(self, start='/')   # list of SUID files
    def world_writable(self, directory)  # list of 777 / world-writable files
    def report_json(self, data, output_path)  # save a JSON report
```

---

## Real Example — Testing on `/usr/bin`

```
$ python checker.py --dir /usr/bin --check suid
```

Ran without any errors and found the usual SUID files on the system (like `sudo`, `passwd`, `su`) — exactly the kind of files a security audit should focus on, since a misused SUID binary is a common privilege-escalation vector.

*(Insert actual terminal screenshot here)*

---

## Bugs Found and Fixed During Development

This tool was built with live testing against real edge cases, not just "runs without an error." Full details are in [`NOTES.md`](NOTES.md); the two most important fixes:

1. **SUID detection was missing files with the SUID bit set but no execute permission** (shown as an uppercase `S` instead of `s`) — fixed with a case-insensitive comparison.
2. **World-writable detection was missing files with extra special bits** (SUID + 777 together, or a sticky bit), because the original code compared the entire permission string instead of checking the "other" write bit at its fixed position (index 8).

Both cases were confirmed through actual testing with real files at different permission levels, not theoretical assumption.

---

## Known Limitations

- No explicit `PermissionError` handling if the tool is run against restricted system paths (e.g. `/root` without sufficient privileges).
- `suid_find` and `world_writable` return file paths only in the report, not the full permission string.