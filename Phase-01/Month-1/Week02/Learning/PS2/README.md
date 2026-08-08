# Password Manager (PS2)

A command-line password manager built with Python OOP — featuring a
pluggable storage architecture, secure password generation, and a
full `argparse`-based CLI.

## Features

- **Secure password generation** using the `secrets` module (not `random`)
  - Character-based generation with configurable rules (upper/lower/digits/symbols)
  - Batch generation (multiple passwords at once)
  - Passphrase generation from a word list (`.txt` or `.json`)
- **Password strength validation** — weak passwords are rejected automatically
- **Pluggable storage backend** — currently supports JSON, designed to support
  additional backends (CSV, SQLite, etc.) without changing the core vault logic
- **Full CLI** — add, get, list, delete, search, check expiry, backup, and
  open a saved website directly in your browser

## Project Structure

```
PS2/
├── vault.py                  # CLI entry point
├── vault.json                # your vault data (created on first use)
├── words_alpha.txt           # word list used for passphrase generation
└── Python/
    ├── password_generator.py # PasswordGenerator class
    ├── password_entry.py     # PasswordEntry class
    └── password_vault.py     # PasswordVault + VaultStorage (ABC) + JSONStorage
```

## Architecture

The project is built around three core classes plus a storage abstraction:

- **`PasswordGenerator`** — generates secure passwords and passphrases using
  `secrets` (cryptographically secure randomness), with a Fisher-Yates shuffle
  step to avoid positional bias.
- **`PasswordEntry`** — represents a single saved credential. Password
  strength is validated on both creation and update via a `@property` setter.
- **`PasswordVault`** — manages the collection of entries (add/get/delete/search/etc.)
  and delegates persistence to a storage object.
- **`VaultStorage`** (abstract base class) — defines the storage contract
  (`save`/`load`). `JSONStorage` is the current implementation; new storage
  types can be added later without modifying `PasswordVault` itself
  (composition over inheritance).

## Installation

Requires Python 3.10+ (uses the `X | Y` type hint syntax). No external
dependencies — everything used is from the standard library.

```bash
git clone <repo-url>
cd password-manager
```

## Usage

All commands go through `vault.py`. The vault file defaults to `vault.json`
in the current directory; override it with `--file` and the storage backend
with `--storage`.

### Add an entry

With a manually chosen password:
```bash
python vault.py vault add --website gmail --username me@gmail.com --password "YourStrongPass1!"
```

With an auto-generated password:
```bash
python vault.py vault add --website gmail --username me@gmail.com --generate --length 20
```

> Weak passwords (manual or generated) are rejected — a password needs at
> least 12 characters and a mix of uppercase, lowercase, digits, and symbols
> to be accepted.

### Retrieve an entry

```bash
python vault.py vault get --website gmail
```

### List all entries

```bash
python vault.py vault list
```

### Delete an entry

```bash
python vault.py vault delete --website gmail
```

### Search entries (by website or username)

```bash
python vault.py vault search --query gmail
```

### Find expired entries (default: older than 90 days)

```bash
python vault.py vault expired --days 90
```

### Back up the vault

```bash
python vault.py vault backup --dir ~/backups
```

### Open a saved website in your browser

```bash
python vault.py vault open --website gmail
```

### Generate a password without saving it

```bash
python vault.py generate password --length 20
python vault.py generate batch --count 5 --length 16
python vault.py generate passphrase --dict words_alpha.txt --words 4 --sep -
```

> Run these commands from inside the `PS2/` folder — `words_alpha.txt` is
> bundled there so the command works right out of the box.

## Example Session

```bash
$ python vault.py vault add --website github --username dev@example.com --generate --length 18
Added successfully!

$ python vault.py vault list
[PasswordEntry('github', 'dev@example.com', '****', '', '2026-08-08 ...')]

$ python vault.py vault get --website github
Website 'github' : dev@example.com

$ python vault.py vault backup --dir ./backups
Backup is Done!

$ python vault.py vault delete --website github
Deleted successfully!
```

## Security Notes

- Passwords are generated using `secrets`, Python's cryptographically secure
  random module — never `random`.
- Password strength is enforced on every entry, whether typed manually or
  auto-generated.
- Opening saved websites uses Python's built-in `webbrowser` module (no shell
  execution involved).

## Known Limitations

- Passwords are stored as plaintext in `vault.json` (no encryption layer yet).
  This is a learning project — do not use it for real credentials.
- Only JSON storage is currently implemented, though the architecture
  supports adding more backends.

## Author's Notes

Built as part of Week 6 of a 52-week cybersecurity roadmap, as a practical
exercise in Python OOP: encapsulation, abstraction (`ABC`), composition over
inheritance, classmethods as alternate constructors, and dunder methods.