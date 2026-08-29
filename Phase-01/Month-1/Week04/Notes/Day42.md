# Summary Ch 17 — Searching for Files
> This chapter has more tables than any chapter so far (commands, tests, operators, actions, options) — that's the book being thorough for reference purposes, not a sign the topic is inherently harder. This summary is split into **"use constantly"** vs. **"exists, look up when needed"** — don't try to memorize everything with equal weight.

---

## 🟢 TIER 1 — Learn These Well (you'll actually type these often)

### `locate` — the fast, simple way to find a file by name
```bash
locate bin/zip
```
Searches a **pre-built database** of every pathname on the system and returns anything containing your search string. Instant, because it's just searching a database, not scanning the actual disk.

**Combine with `grep` for more specific searches:**
```bash
locate zip | grep bin
```

⚠️ **Why `locate` sometimes "misses" a file you just created:** the database (built by a background program called `updatedb`, usually run once a day via `cron`) isn't updated in real time. A file created 5 minutes ago genuinely won't show up yet. If you need it to see recent files immediately:
```bash
sudo updatedb
```

### `find` — the powerful, flexible way to search by attributes (not just name)
```bash
find ~ -type f -name "*.txt"
```
Unlike `locate`, `find` actually **scans the filesystem live** each time you run it — slower, but far more flexible: you can search by type, size, permissions, owner, modification time, and more, and you can combine multiple conditions.

### The Core Pattern to Remember
```bash
find <where-to-look> <what-to-look-for> <what-to-do-with-it>
```

### The 3 tests you'll use constantly
```bash
find ~ -type f              # regular files only
find ~ -type d               # directories only
find ~ -type f -name "*.txt"   # regular files matching a name pattern
```
⚠️ **Always quote the `-name` pattern** (`"*.txt"`) — this stops the shell itself from expanding the wildcard (Ch4/Ch7 pathname expansion) before `find` ever sees it. Without quotes, the shell might expand `*.txt` into actual filenames from your current directory instead of passing the literal pattern to `find`.

| File type letter | Meaning |
|---|---|
| `f` | regular file |
| `d` | directory |
| `l` | symbolic link |

### Searching by size
```bash
find ~ -type f -size +1M      # larger than 1 MB
find ~ -type f -size -1M       # smaller than 1 MB
find ~ -type f -size 1M         # exactly 1 MB
```
`+` = more than, `-` = less than, no sign = exact match. Units: `k` (KB), `M` (MB), `G` (GB).

### The action you already know and use: `-delete`
```bash
find ~ -type f -name '*.bak' -delete
```
🚨 **Golden safety rule (same principle as `rm` from Ch4):** always run the exact same `find` command with `-print` (or no action at all — `-print` is the default) FIRST, look at the results, and only add `-delete` once you're sure the list is exactly what you want to remove. There's no undo.

### `-exec` — running a command on every match (the practical version)
```bash
find ~ -type f -name 'foo*' -exec ls -l '{}' ';'
```
- `{}` = a placeholder that gets replaced with each matching file's path
- `;` = required to mark the end of the command (usually escaped as `\;` or quoted `';'` since `;` has meaning to the shell)

**Real example you'll actually use — the SUID-finding command from your roadmap:**
```bash
find / -perm -4000 2>/dev/null
```
You already know this one. It's `find` + a permission test (`-perm -4000` = has SUID bit set) + suppressing permission-denied noise (`2>/dev/null`, from Ch6).

---

## 🟡 TIER 2 — Good to Recognize, Not Urgent to Memorize

You'll understand these when you see them in someone else's script or a man page — no need to actively memorize the syntax yet.

### More useful tests
| Test | Meaning |
|---|---|
| `-iname pattern` | like `-name` but case-insensitive |
| `-mtime n` | content modified n days ago |
| `-newer file` | modified more recently than a reference file — useful for backup scripts |
| `-perm mode` | matches a specific permission mode |
| `-user name` / `-group name` | owned by a specific user/group |
| `-nouser` | belongs to no valid user — **can indicate a deleted account or attacker activity, worth knowing this exists for security investigation** |
| `-empty` | matches empty files/directories |

### Combining tests with logical operators
```bash
find ~ \( -type f -not -perm 0600 \) -or \( -type d -not -perm 0700 \)
```
This looks intimidating, but it's just: **"find files that don't have 0600 permissions, OR directories that don't have 0700 permissions."**

| Operator | Meaning | Shortcut |
|---|---|---|
| `-and` | both sides must be true (this is the *default* if you write nothing) | `-a` |
| `-or` | either side true | `-o` |
| `-not` | negates the following test | `!` |
| `\( \)` | groups tests together, like parentheses in math | — |

⚠️ Parentheses need to be **escaped** (`\(` `\)`) because `(` and `)` mean something to the shell itself — without the backslash, the shell tries to interpret them before `find` ever sees them.

**Why this specific example uses `-or` and not `-and`:** a single item can't simultaneously be "a file with bad permissions" AND "a directory with bad permissions" — it's one or the other. So `-or` correctly catches either case.

### Combining `find` results into one efficient command with `xargs`
```bash
find ~ -type f -name 'foo*' -print | xargs ls -l
```
Instead of running `ls -l` separately for every single match (slow), `xargs` bundles all the results into **one single command call**. Nice to know exists; the `-exec ... ';'` form you already know works fine for smaller jobs.

---

## 🔴 TIER 3 — Reference Only (skip memorizing, come back if you ever specifically need it)

These are genuinely edge-case or advanced — the book includes them for completeness, not because a beginner needs them day one.

- **`-cmin`/`-cnewer`/`-ctime`** (change-time-based tests, subtly different from modification time)
- **`-inum`/`-samefile`** (searching by inode number — ties back to the hard-link concept from Ch4, only needed for advanced forensic-style file tracing)
- **`-exec ... {} +`** (the `+` variant that batches into fewer command executions — a performance optimization, not a new concept)
- **`-print0` / `xargs --null`** (handling filenames with embedded spaces/newlines safely — a real but rare edge case)
- **`find` options**: `-maxdepth`, `-mindepth`, `-depth`, `-mount`, `-noleaf` (scope-control options for advanced searches)
- **`stat`** command (detailed file metadata — useful, but `ls -l` covers 90% of what you'll need day to day)

---

## 🔐 Why This Chapter Matters for Security Work
- `find / -perm -4000 2>/dev/null` — you already know this one; it's a core privilege-escalation enumeration step
- `find / -nouser 2>/dev/null` — finds files owned by non-existent user IDs, a real indicator of a deleted account being reused or an attacker leaving traces
- `find` with `-newer` is exactly how backup/monitoring scripts detect "what changed since last time I checked"
- Locating and safely testing-before-deleting matches (`-print` before `-delete`) is the same defensive habit as testing wildcards with `ls` before `rm` — a recurring theme across this whole book

---

## 🎯 What You Should Be Able to Recall After Today
1. `locate` = fast database search by name; misses very recent files until `updatedb` runs
2. `find <path> <tests> <action>` = slower but flexible, live filesystem search by many attributes
3. `-type f` / `-type d` / `-name "pattern"` (always quoted) are your everyday go-to tests
4. `-size +1M` / `-1M` / `1M` — `+` bigger, `-` smaller, no sign exact
5. **Test with `-print` (or no action) before ever using `-delete`** — same safety discipline as `rm`
6. `-exec command '{}' ';'` runs a command on each match; `{}` is the placeholder, `;` marks the end
7. You already know and use: `find / -perm -4000 2>/dev/null` for SUID enumeration
8. `-and`/`-or`/`-not` combine tests; `-and` is implied by default; parentheses need escaping (`\(` `\)`)
9. Everything in Tier 3 is fine to skip for now — it's there for when a specific need arises, not something missing from your understanding today

---


# Summary Ch 18 — Archiving and Backup
> Same idea as Ch17: this chapter covers 5 tools (`gzip`, `bzip2`, `tar`, `zip`, `rsync`), but they're not all equally important day-to-day. Tiered below so you know exactly what to actually remember vs. what's just good to recognize.

---

## 🟢 TIER 1 — Learn These Well (you'll actually use these constantly)

### The Core Concept: Compression vs. Archiving — Two Different Jobs
| Job | What it does | Tools |
|---|---|---|
| **Compression** | Shrinks a **single file's** size by removing redundant data | `gzip`, `bzip2` |
| **Archiving** | Bundles **many files/folders** into **one** file (doesn't necessarily shrink anything) | `tar`, `zip` |

**Why this distinction matters:** `gzip` only compresses *one file at a time* — it can't bundle a folder full of files into one thing by itself. That's `tar`'s job. This is exactly why you constantly see them **combined**: `tar` bundles everything into one file, then `gzip` shrinks that bundle.

### `tar` — the standard Linux archiving tool
```bash
tar cf archive.tar folder/       # Create an archive
tar xf archive.tar                 # eXtract an archive
tar tf archive.tar                  # list contents (Test/list) without extracting
```
The letter right after `tar` is the **mode** — always comes first, no dash needed:
| Mode | Meaning |
|---|---|
| `c` | create |
| `x` | extract |
| `t` | list contents |
| `f` | (always paired with one of the above) means "the next argument is the archive filename" |

**Add `v` for verbose** (see every file as it's processed): `tar cvf archive.tar folder/`

### The Combo You'll Use Constantly: Archive + Compress in One Step
```bash
tar czf archive.tar.gz folder/     # c=create, z=gzip compression, f=filename
tar xzf archive.tar.gz               # extract a gzip-compressed tar archive
```
| Flag | Compression |
|---|---|
| `z` | gzip (`.tar.gz` or `.tgz`) |
| `j` | bzip2 (`.tar.bz2` or `.tbz`) — slower, but compresses more |

**Rule of thumb: use `z` (gzip) by default.** It's faster and the difference in compression size rarely matters for everyday use. Only reach for `j` (bzip2) when you specifically need the smallest possible file and don't mind the extra time.

### Single-File Compression: `gzip` / `gunzip`
```bash
gzip file.txt          # replaces file.txt with file.txt.gz (compressed)
gunzip file.txt.gz      # replaces file.txt.gz with file.txt (restored)
```
⚠️ **Important behavior to remember:** `gzip` **replaces the original file** — it doesn't keep both versions by default. Same for `gunzip` in reverse.

**Quick peek inside a compressed text file without fully extracting it:**
```bash
zcat file.txt.gz | less
```

### 🚨 Golden Rule: Don't Compress Already-Compressed Files
```bash
gzip picture.jpg     # DON'T — usually makes the file slightly LARGER, not smaller
```
JPEG, MP3, and most modern file formats are **already compressed internally**. Running `gzip` on them wastes time and typically adds overhead without removing any actual redundancy — there's nothing left to compress.

---

## 🟡 TIER 2 — Good to Recognize, Not Urgent to Memorize

### `zip` / `unzip` — mainly for Windows interoperability
```bash
zip -r archive.zip folder/     # -r = recursive, needed to include folder contents
unzip archive.zip
```
On Linux, `tar`+`gzip` is strongly preferred — `zip` exists mainly because `.zip` is the format Windows users expect. Know the basic syntax exists; you'll reach for `tar` far more often on Linux systems.

### `bzip2` / `bunzip2` — gzip's stronger, slower sibling
```bash
bzip2 file.txt        # → file.txt.bz2
bunzip2 file.txt.bz2
```
Same usage pattern as `gzip`, just a different (slower but tighter) compression algorithm. Comes with `bzcat` (same idea as `zcat`).

### `rsync` — smart, efficient syncing (not just copying)
```bash
rsync -av source/ destination/
```
- `-a` = archive mode (recursive + preserves permissions/timestamps)
- `-v` = verbose

**The one thing that makes `rsync` genuinely special:** run it twice on the same source/destination, and the second run only copies what actually **changed** — it's smart enough to detect differences instead of blindly re-copying everything. This makes it excellent for repeated backups (copy once, then just "top up" the differences each time after).

⚠️ **One subtle but important syntax detail — the trailing slash matters:**
```bash
rsync source destination        # copies the folder "source" INTO destination (→ destination/source)
rsync source/ destination        # copies the CONTENTS of source into destination (→ destination/file1, file2...)
```

**Practical backup pattern worth recognizing:**
```bash
rsync -av --delete /etc /home /media/BigDisk/backup
```
`--delete` removes files from the backup that no longer exist in the source — keeps the backup an exact mirror rather than an ever-growing pile of old files.

---

## 🔴 TIER 3 — Reference Only (skip for now, come back if a specific need arises)

- **`tar` over `ssh` for network file transfer** (`ssh remote-sys 'tar cf - dir' | tar xf -`) — a clever trick, but a specialized one; you already know `scp`/`sftp` from Ch16 for straightforward remote file transfer
- **`tar --wildcards`** for extracting specific files by pattern from an archive
- **`tar` + `find` combined** for incremental backups (only archiving files newer than a timestamp)
- **`zip`'s standard-input quirks** (`-@` option, the awkward `-` filename handling) — `zip` piping is clunky by design; not worth memorizing
- **`rsync` over a remote server URI** (`rsync://host/path`) — used for mirroring public software repositories, a fairly specialized use case
- **`bzip2recover`** — recovery tool for damaged `.bz2` files, situational

---

## 🔐 Why This Chapter Matters for Security Work
- `tar czf` is the standard way to package up evidence, logs, or a compromised directory for later analysis or transport
- Knowing `gzip`/`bzip2` file signatures and behavior matters when examining unknown files during forensics — a `.tar.gz` you find on a system tells you something was intentionally bundled and compressed
- `rsync -av --delete` is a real, practical way to maintain a synced backup of critical config or log directories before making risky changes
- Understanding that compression ≠ encryption is worth internalizing: none of these tools (`gzip`, `tar`, `zip` without a password) provide any security on their own — a `.tar.gz` is just as readable as its contents once extracted, by anyone with access to the file

---

## 🎯 What You Should Be Able to Recall After Today
1. **Compression** (shrink one file: `gzip`/`bzip2`) is a different job from **archiving** (bundle many files: `tar`/`zip`) — they're usually combined, not interchangeable
2. `tar czf archive.tar.gz folder/` to create, `tar xzf archive.tar.gz` to extract — this single combo covers most of what you'll actually do
3. `gzip`/`gunzip` replace the original file by default — no automatic "keep both" behavior
4. Never compress already-compressed formats (JPEG, MP3, etc.) — it usually makes files slightly bigger, not smaller
5. `rsync -av source/ destination/` — smart syncing that only copies what changed on repeat runs; mind the trailing slash, it changes the result
6. Tier 2 and Tier 3 tools/options exist and are fine to look up later — you don't need to have them memorized to consider this chapter "done"