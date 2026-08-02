# RegexFileKit

A small OOP toolkit for common cybersecurity file/log analysis tasks — scanning directories, extracting IOCs (IPs, emails, URLs, hashes) from text, and parsing structured log files. Built as part of a Python + Cybersecurity self-study roadmap (Phase 1, PS1).

All classes inherit from a shared `SecurityToolkit` base class.

## Components

| Module | Class | What it does |
|---|---|---|
| `filescanner.py` | `FileScanner` | Walk directories, find large files, find recently modified files, count files by extension |
| `regexhelper.py` | `RegexHelper` | Extract IPs, emails, URLs, and hashes (MD5/SHA-256) from raw text |
| `log_extractor.py` | `LogExtractor` | Parse structured log lines, export to JSON/CSV, generate summary stats |
| `cli.py` | — | Single entry point that exposes all three tools as subcommands |

## Requirements

- Python 3.10+
- No third-party dependencies — everything used (`argparse`, `pathlib`, `re`, `json`, `csv`, `ipaddress`, `datetime`) is from the standard library.


No `pip install` needed — standard library only.

## Usage

Every tool can be run standalone (e.g. `python regexhelper.py ...`) or through the unified `cli.py`.

### File Scanner — `scan`

```bash
# List files (with optional extension filter — use a full glob pattern, e.g. "*.py")
python cli.py scan --dir ./project walk --ext "*.py" --count 5

# Find files larger than N MB
python cli.py scan --dir ./project largefiles --mn_size 10

# Find files modified in the last N days
python cli.py scan --dir ./project rfiles --days 7

# Count files by extension
python cli.py scan --dir ./project --cext
```

### Log Extractor — `logs`

Expects log lines in the format:
`<ip> - <YYYY-MM-DD> <HH:MM:SS> - <action> - <status>`

```bash
python cli.py logs --log access.log --output report.json --summary
python cli.py logs --log access.log --output report.csv
```

### Regex Helper — `regex`

```bash
python cli.py regex --text "contact admin@example.com" --find emails
python cli.py regex --text "server IP is 192.168.1.1" --find ips
python cli.py regex --text "see https://example.com/page for info" --find urls
python cli.py regex --text "d41d8cd98f00b204e9800998ecf8427e" --find hashes -v
```

## ⚠️ Important: argument order for `scan`

`--dir` (and `--cext`) must come **before** the subcommand (`walk` / `largefiles` / `rfiles`), not after. This is standard `argparse` behavior: once a subcommand keyword is parsed, everything after it is handed off to that subcommand's own parser, so any parent-level option written after it won't be recognized.

```bash
# ❌ Wrong — will fail with "the following arguments are required: --dir"
python cli.py scan walk --dir ./project --count 3

# ✅ Correct
python cli.py scan --dir ./project walk --count 3
```

This applies to every `scan` subcommand (`walk`, `largefiles`, `rfiles`) and to `--cext`.

## Example output

```
$ python cli.py regex --text "server IP is 192.168.1.1, contact admin@example.com" --find ips
Found [IPv4Address('192.168.1.1')] ip/s

$ python cli.py logs --log access.log --output report.json --summary
Saved the file to report.json.
total: 3
unique_ips: 2
failed_count: 1
```

## Known limitations

- **Docstrings**: not added yet — planned for a follow-up pass.
- **Type hints**: return types are annotated on most methods; parameter type hints are only partially added.
- **`scan` argument order**: see the warning above — `--dir` must precede the subcommand.
- `find_ips` returns `ipaddress.IPv4Address` / `IPv6Address` objects rather than plain strings (reflected in its type hint).

## Project structure

```
regex-file-kit/
├── security_toolkit.py   # Base class (SecurityToolkit)
├── filescanner.py         # FileScanner
├── regexhelper.py         # RegexHelper
├── log_extractor.py       # LogExtractor
├── cli.py                 # Unified CLI entry point
└── README.md
```