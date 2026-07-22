# MiniSOC
 
A small security operations console — password vault, log analyzer, and
incident tracker, unified under one shared `SecurityToolkit` base class.
 
Built as a Phase 0 capstone project, reusing and integrating code written
across Weeks 1-4 rather than starting from scratch.
 
## What it does
 
- **Password vault** — store, validate, and check the age of website
  credentials.
- **Log analyzer** — read a log file, filter for warnings/errors, sort and
  search by timestamp.
- **Incident tracker** — automatically opens phishing / malware /
  unauthorized-access incidents from suspicious log lines, and ranks them
  by priority.
- **Persistence** — save and reload everything as JSON.
- All from one command-line menu.

## Project structure
 
```
minisoc/
    security_toolkit.py     Base class: scan / log / report / save_results / load_results
    password_vault.py       PasswordEntry, PasswordVault, PasswordVaultIterator
    log_analyzer.py         read_log_lines, parse_log_line, filtering, sorting, searching
    incident_tracker.py     Analyst, SecurityIncident hierarchy, IncidentLog, classification
    algorithms.py           merge_sort, merging, binary_search_iter
    main.py                 CLI entry point
    sample.log               sample data for testing / trying it out
    data/
        vault.json
        incidents.json
```

## Architecture
 
```
main.py (CLI entry point)
  |
  +--> PasswordVault     --> inherits SecurityToolkit
  +--> LogAnalyzer       --> inherits SecurityToolkit
  +--> IncidentTracker   --> inherits SecurityToolkit
 
SecurityToolkit (base class)
  scan() / log() / report() / save_results() / load_results()
```
 
## Usage
 
```
python main.py
```
 
```
=== MiniSOC ===
1) Add a password entry
2) List vault (sorted by date)
3) Load a log file
4) Auto-create incidents from the loaded log
5) List incidents (sorted by priority)
6) Save everything to JSON
7) Load everything from JSON
8) Exit
Choose an option:
```
 
A typical first run: option 1 to add a password, option 3 with `sample.log`
to load some test data, option 4 to turn the suspicious lines into
incidents, option 5 to see them ranked, option 6 to save.
