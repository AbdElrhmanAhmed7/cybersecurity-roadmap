# Summary Ch 1-6 — The Linux Command Line
> Filtered summary: historical/theoretical and GUI-only content removed. What's left is what you'll actually need for cybersecurity and use daily.

---

## Ch1 — What Is the Shell?

### Core Concepts
| Term | Meaning |
|---|---|
| **Shell** | The program that takes your keyboard commands and passes them to the OS to execute |
| **bash** | The default shell in most Linux distros (Bourne Again SHell) |
| **Terminal Emulator** | The program that gives you access to the shell (not the shell itself) |
| **Shell Prompt** | `[me@linuxbox ~]$` — if it ends in `#` instead of `$`, you're running with root privileges |

### Commands to Try Right Away
```bash
date      # current time and date
uptime    # how long the system has been running + load average
df        # free disk space
free      # available memory
exit      # or Ctrl-d to end the session
```

### Good to Know (no need to memorize)
- **Command History**: ↑ / ↓ bring back previous commands
- **Copy/Paste in the terminal**: not Ctrl-C/V — use `Shift-Ctrl-C` / `Shift-Ctrl-V`

---

## Ch2 — Navigation

### Core Commands (must memorize)
| Command | Function |
|---|---|
| `pwd` | Prints your current location (Print Working Directory) |
| `ls` | Lists directory contents |
| `cd <path>` | Changes the current directory |

### Absolute vs Relative Path — the most important idea in this chapter
| Type | Starts from | Example |
|---|---|---|
| **Absolute** | Always from root `/` | `cd /usr/bin` |
| **Relative** | From your current location | `cd bin` or `cd ./bin` |

### Important Notation
- `.` = current directory
- `..` = parent directory (one level up)
- `~` = your home directory

### cd Shortcuts
```bash
cd            # takes you to Home
cd -          # takes you to the previous directory you were in
cd ~username  # takes you to another user's home directory
```

### Filename Rules in Linux
1. Any name starting with `.` = a **hidden file** (needs `ls -a` to see it)
2. Filenames and **commands are case-sensitive** (`File1` ≠ `file1`)
3. Linux **has no mandatory file extension** — `.txt` doesn't guarantee actual text content
4. Don't put spaces in filenames — use `_` instead

---

## Ch3 — Exploring the System

### New Commands
| Command | Function |
|---|---|
| `file <name>` | Tells you the file's actual type (not based on extension) |
| `less <file>` | Opens a text file for page-by-page reading |

### Key ls Options (memorize these well)
| Option | Meaning |
|---|---|
| `-l` | Long format (full details) |
| `-a` | Show hidden files too |
| `-h` | Human-readable sizes (KB/MB instead of bytes) |
| `-t` | Sort by last modified |
| `-r` | Reverse the sort order |
| `-S` | Sort by size |

**Important:** options can be combined: `ls -lh` = long + human-readable

### Reading `ls -l` Output (you'll refer to this a lot in security work)
```
-rw-r--r-- 1 root root 32059 2017-04-03 11:05 file.odf
```
| Part | Meaning |
|---|---|
| `-rw-r--r--` | File type + permissions (owner/group/other) — covered in depth in Ch9 |
| `1` | Number of hard links |
| `root root` | Owner and group |
| `32059` | Size in bytes |
| Date | Last modification time |
| Name | Filename |

⚠️ The first character in `-rw-r--r--`:
- `-` = regular file
- `d` = directory
- `l` = symbolic link

### `less` — Essential Keys Only
| Key | Action |
|---|---|
| Space / Page Down | Scroll forward one page |
| b / Page Up | Scroll back one page |
| `/text` | Search for a word |
| `n` | Next search result |
| `q` | Quit |

### Key Filesystem Directories (you'll use these constantly in security work)
| Directory | Why it matters |
|---|---|
| `/etc` | All config files (`/etc/passwd`, `/etc/crontab`, `/etc/fstab`) |
| `/var/log` | Log files — the most important place in any security investigation |
| `/tmp` | Temporary files — a common spot for suspicious files |
| `/proc` | Virtual filesystem showing live kernel state |
| `/home` | User directories |
| `/usr/bin` | Most installed programs |
| `/root` | Home directory of the root user |

### Symbolic Links (very important in security — used in privilege escalation attacks)
- A file that points to another file/directory (like a shortcut)
- Shows up in `ls -l` as: `lrwxrwxrwx ... link_name -> target`
- If the target is deleted, the link becomes **broken** (Linux usually colors it red)
- Difference from **Hard Link**: a hard link can't cross partitions and can't point to a directory

---

## Ch4 — Manipulating Files and Directories
> This is the heaviest chapter so far — the commands here are the ones you'll type constantly, and `rm` is genuinely destructive if misused. This section is denser on purpose.

### The 5 Core Commands
| Command | Function |
|---|---|
| `mkdir` | Create directories |
| `cp` | Copy files and directories |
| `mv` | Move / rename files and directories |
| `rm` | Remove (delete) files and directories |
| `ln` | Create hard and symbolic links |

### Wildcards (a.k.a. globbing)
Special characters the shell expands into matching filenames **before** the command even runs.

| Wildcard | Meaning | Example | Matches |
|---|---|---|---|
| `*` | Any characters, including none | `*.txt` | any file ending in `.txt` |
| `?` | Exactly one character | `Data???` | `Data` + exactly 3 chars |
| `[abc]` | Any one char in the set | `[abc]*` | files starting with a, b, or c |
| `[!abc]` or `[^abc]` | Any char **not** in the set | `[!0-9]*` | not starting with a digit |
| `[[:class:]]` | Any char in a character class | `[[:upper:]]*` | starts with an uppercase letter |

**Character classes you'll actually use:** `[:alnum:]` `[:alpha:]` `[:digit:]` `[:lower:]` `[:upper:]`

⚠️ Avoid old-style ranges like `[A-Z]` or `[a-z]` — they don't behave predictably on modern systems. Use character classes instead.

**Dot files:** files starting with `.` are hidden from both `ls` and wildcards. `.*` matches them but also grabs `.` and `..` — use `.[!.]*` or `.??*` to exclude those two.

### `mkdir` — Create Directories
```bash
mkdir dir1              # creates one directory
mkdir dir1 dir2 dir3     # creates three directories at once
```

### `cp` — Copy Files and Directories
```bash
cp item1 item2          # copy item1 to item2
cp item1 item2 dir1     # copy multiple items into an existing directory
```

| Option | Long form | Meaning |
|---|---|---|
| `-i` | `--interactive` | Ask for confirmation before overwriting |
| `-r` | `--recursive` | **Required** to copy directories |
| `-u` | `--update` | Only copy files that are new or newer than the destination |
| `-v` | `--verbose` | Print what's being copied |
| `-a` | `--archive` | Preserve ownership/permissions too (covered fully in Ch9) |

**Common patterns:**
```bash
cp -r dir1 dir2     # copy dir1's contents into dir2 (or create dir2 if it doesn't exist)
cp -u *.html dest    # only copy newer/missing HTML files — hard to do with a GUI, easy here
```

### `mv` — Move and Rename
Same syntax style as `cp`, but the source is **gone** afterward (it's not a copy):
```bash
mv file1 file2       # renames file1 to file2
mv file1 dir1        # moves file1 into dir1
mv dir1 dir2         # if dir2 exists → moves dir1 inside it; if not → renames dir1 to dir2
```
Shares the `-i`, `-u`, `-v` options with `cp` (no `-r` needed — `mv` handles directories natively).

### `rm` — Remove Files and Directories
```bash
rm file1              # delete silently — NO confirmation, NO undo
rm -i file1            # ask before deleting
rm -r dir1              # required to delete a directory (recursive)
rm -rf file1 dir1        # force + recursive — skips prompts, ignores missing files
```

🚨 **This is the most dangerous command in the chapter — memorize this section, not just skim it:**
- Linux has **no undelete**. Once `rm` runs, the data is gone.
- Classic disaster: `rm *.html` is safe, but `rm * .html` (extra space) deletes **everything** in the directory, then complains it can't find a file called `.html`.
- **Golden rule:** before running `rm` with a wildcard, run the exact same pattern with `ls` first. If the `ls` output looks right, press ↑ and swap `ls` for `rm`.

### `ln` — Create Links
```bash
ln file link          # hard link
ln -s item link         # symbolic link
```

### Hard Links vs Symbolic Links — the core concept of this chapter

Think of a file as two separate parts:
1. **The data** (actual content) — stored in an **inode**
2. **The name** — just a label pointing at an inode

| | Hard Link | Symbolic Link |
|---|---|---|
| Points to | The **inode** (the actual data) | The **name** of the target file |
| Can cross filesystems/partitions? | ❌ No | ✅ Yes |
| Can link to a directory? | ❌ No | ✅ Yes |
| Shown differently in `ls -l`? | No — looks identical to a normal file | Yes — `l` prefix + `link -> target` |
| If the original is deleted | **Still works** — data isn't freed until every hard link to it is deleted | **Breaks** — becomes a "broken link" pointing at nothing |
| Writing to the link | Writes to the shared data | Writes to the target file (transparent) |
| Deleting the link | Removes one name; data survives if other links exist | Only the link is deleted, target untouched |

**Check it yourself:** `ls -li` shows the **inode number** as the first column. Two hard links to the same file will show the *same* inode number — that's the proof they're really the same file.

⚠️ **Security relevance:** because `rm` doesn't truly erase data until all hard links are gone, deleted files can sometimes be recovered — relevant to digital forensics. Symbolic links are also a classic vector in **privilege escalation / symlink attacks** (pointing a writable symlink at a sensitive file like `/etc/passwd`).

### The Playground Exercise (do this, don't just read it)
```bash
cd
mkdir playground && cd playground
mkdir dir1 dir2
cp /etc/passwd .
mv passwd fun
ln fun fun-hard              # hard link
ln -s fun fun-sym            # symbolic link
ls -li                       # compare inode numbers
rm fun                       # fun-hard still has the data, fun-sym is now broken
less fun-sym                 # "No such file or directory" — proof it's broken
rm -r ~/playground            # clean up everything
```

---

## Ch5 — Working with Commands
> This chapter is about *tooling* — how to figure out what a command is and how to find its documentation on your own, without needing to ask anyone (or me).

### The 4 Types of "Commands" in Linux
| Type | What it is | Example |
|---|---|---|
| **Executable program** | An actual file on disk (compiled binary or script) | `/usr/bin/cp` |
| **Shell builtin** | Built directly into bash itself | `cd`, `type`, `alias` |
| **Shell function** | A mini-script stored in the shell environment | (covered later, Ch26) |
| **Alias** | A shortcut you define yourself | `ls` (often aliased to `ls --color=auto`) |

### Identifying a Command
| Command | Function |
|---|---|
| `type <cmd>` | Tells you which of the 4 types a command is |
| `which <cmd>` | Shows the exact file path of an **executable only** (returns nothing for builtins/aliases) |

```bash
type ls      # ls is aliased to `ls --color=auto`
type cp      # cp is /usr/bin/cp
type cd      # cd is a shell builtin
which cd     # → error, because cd isn't an executable file
```

### 🎯 Getting Documentation — this is the actually useful part
| Tool | Best for | Usage |
|---|---|---|
| `help <builtin>` | Shell builtins only (`cd`, `type`, etc.) | `help cd` |
| `<command> --help` | Most executables — quick syntax + options | `mkdir --help` |
| `man <command>` | **The standard reference** for almost everything | `man ls` |
| `man <section> <term>` | Disambiguate when a name means multiple things | `man 5 passwd` (file format, not the command) |
| `apropos <keyword>` | Search man pages by keyword when you don't know the exact command name | `apropos partition` |
| `whatis <command>` | One-line description of what a command does | `whatis ls` |
| `info <command>` | GNU's hyperlinked alternative to man (deeper, more tutorial-like for GNU tools) | `info coreutils` |

### man Page Sections (useful when a name is ambiguous)
| Section | Contents |
|---|---|
| 1 | User commands |
| 2 | Kernel system calls (programming) |
| 3 | C library calls (programming) |
| 4 | Device files/drivers |
| 5 | **File formats** — e.g. `man 5 passwd` explains the `/etc/passwd` file layout, not the `passwd` command |
| 6 | Games |
| 7 | Misc |
| 8 | System administration commands |

### `alias` — Making Your Own Commands
```bash
alias foo='cd /usr; ls; cd -'   # define
foo                              # use it like any command
type foo                         # confirms: foo is aliased to `cd /usr; ls; cd -'
unalias foo                      # remove it
alias                            # list all currently defined aliases
```
⚠️ Aliases defined this way **disappear when the shell session ends** — making them permanent (via startup files) is covered in Ch11 (The Environment).

**Multiple commands on one line:** separate with `;`
```bash
command1; command2; command3
```

---

## Ch6 — Redirection
> This chapter is dense but foundational — I/O redirection and pipes are the backbone of almost every security workflow (log analysis, filtering scan output, chaining tools together). Worth the extra time it took.

### The Core Concept: 3 Numbered Streams
Every program has three default data streams, referenced internally by **file descriptor numbers**:

| Name | Descriptor # | Default source/destination |
|---|---|---|
| **stdin** (input) | `0` | Keyboard |
| **stdout** (normal output) | `1` | Screen |
| **stderr** (error/status messages) | `2` | Screen |

Redirection just means: change where one of these streams goes instead of the default.

### Redirecting Output: `>` and `>>`
```bash
command > file    # overwrite: truncates/creates file, writes fresh output
command >> file   # append: adds output to the end, keeps existing content
```

⚠️ **Critical gotcha:** `>` truncates the file **immediately**, before the command even runs. If the command then fails (e.g. target doesn't exist), you're left with an **empty (0-byte) file** — because `>` already wiped it.

⚠️ **Real disaster example from the book:** running `ls > less` while inside `/usr/bin` **overwrote the actual `less` program** with text output, because `>` silently creates/overwrites *any* file with no warning — even a critical system binary. Treat `>` with respect.

**Trick:** `> file` with no command truncates a file to zero length (or creates an empty one).

### Group Commands `{ }`
Bundle multiple commands so their combined output redirects as one unit:
```bash
{ command1; command2; command3; } > logfile.txt
```
(Note: whitespace after `{` and before `}` is required, and the last command needs a `;` or newline.)

### Redirecting Errors: `2>`
```bash
command 2> errors.txt     # only stderr goes to the file; stdout still prints to screen
```

### Redirecting Both Output + Errors to One File
| Method | Syntax | Notes |
|---|---|---|
| Traditional (order-sensitive!) | `command > file 2>&1` | Must redirect stdout **first**, then point stderr (`2`) at wherever stdout (`1`) now goes. Reversing the order breaks it — `2>&1 > file` sends stderr to the screen instead. |
| Modern (order doesn't matter) | `command &> file` | Cleaner, one notation for both streams |
| Modern + append | `command &>> file` | Same, but appends instead of overwriting |

**Why order matters in the traditional form:** the shell processes redirections left to right at that instant. `2>&1` means "point stderr wherever stdout *currently* points" — if stdout hasn't been redirected yet, stderr just gets linked to the screen (the current stdout destination) and stays there even after stdout is redirected afterward.

### Disposing of Unwanted Output: `/dev/null`
A special "bit bucket" device — anything sent there vanishes permanently. No storage, no trace.
```bash
command 2> /dev/null      # discard errors only, keep normal output visible
command > /dev/null 2>&1  # discard everything (common in scripts/cron jobs)
find / -perm -4000 2>/dev/null   # suppress "Permission denied" spam while scanning the whole filesystem
```

### Redirecting Input: `<`
```bash
cat < file.txt
```
Changes stdin's source from the keyboard to a file. Not very useful with `cat` itself, but the concept matters for commands that read from stdin.

### `cat` — Concatenate Files
```bash
cat file.txt              # dump file contents to screen (no paging, unlike less)
cat file1 file2 > combined.txt   # join multiple files together
cat                        # no arguments → reads from keyboard until Ctrl-d (EOF)
cat > newfile.txt          # quick way to type a short file directly from the keyboard
```

### Pipes `|` — Connecting Commands Together
| Operator | Connects |
|---|---|
| `>` | command ↔ **file** |
| `\|` | command ↔ **command** (stdout of the first becomes stdin of the second) |

```bash
command1 | command2 | command3   # chain as many as needed
```

⚠️ **Common beginner mistake:** `command1 > command2` is *not* a pipe — it silently overwrites a file literally named `command2`. Always use `|` to connect two commands, `>` only to connect a command to a file.

### Filter Commands (used heavily in pipelines)

| Command | Function | Example |
|---|---|---|
| `sort` | Sort lines alphabetically | `ls /bin /usr/bin \| sort` |
| `uniq` | Remove duplicate lines — **input must already be sorted** | `sort \| uniq` |
| `uniq -d` | Show only the duplicates instead of removing them | `sort \| uniq -d` |
| `wc` | Count lines/words/bytes | `wc file.txt` → outputs `lines words bytes` |
| `wc -l` | Count lines only (most commonly used for counting items) | `sort \| uniq \| wc -l` |
| `grep pattern` | Print lines matching a pattern | `grep zip` |
| `head -n X` | First X lines (default 10) | `head -n 5 file.txt` |
| `tail -n X` | Last X lines (default 10) | `tail -n 5 file.txt` |
| `tail -f` | **Follow a file live** — keeps printing new lines as they're added. Stop with Ctrl-c | `tail -f /var/log/messages` |
| `tee file` | Splits the pipeline — writes to `file` **and** passes data through unchanged to the next command | `ls \| tee out.txt \| grep zip` |

### `grep` — Key Options to Remember
| Option | Effect |
|---|---|
| `-i` | Case-insensitive search |
| `-l` | Print only filenames that contain a match (not the matching lines) |
| `-v` | Invert match — print lines that **don't** match |
| `-w` | Match whole words only |

### `tee` — Why It Matters
Think of it as a T-junction in a pipe: it lets data continue down the pipeline **and** saves a copy to a file at the same time, instead of only doing one or the other.
```bash
tail -n 20 /var/log/auth.log | tee last-auth.txt | grep Failed
```
Here you get the full 20 lines saved to `last-auth.txt` (untouched), while the screen only shows the `Failed` matches — useful when you want both a filtered view *and* the full context preserved for later.

If you only need the filtered result saved (not the full unfiltered context too), skip `tee` and just redirect normally:
```bash
tail -n 20 /var/log/auth.log | grep Failed > hi.txt
```

### 🔐 Why This Chapter Matters for Security Work
- `tail -f /var/log/auth.log | grep Failed` — live-monitor failed login attempts
- `2>/dev/null` — suppress permission-denied noise while scanning the whole filesystem (`find`, `locate`)
- `command &> scan_results.log` — capture full tool output (e.g. `nmap`) including errors, for later analysis
- Piping is how most CLI security tools are chained together (`cat access.log | grep <IP> | sort | uniq -c`)

---

## ⚠️ Intentionally Left Out (not needed right now)
- GUI-specific details (Nautilus, Dolphin, "focus follows mouse", GUI symlink creation)
- Virtual consoles (`Ctrl-Alt-F1`)
- Historical trivia (who Steve Bourne / Brian Fox are)
- Detailed ASCII explanation
- Full character-range edge cases beyond the basic wildcard set
- `info` reader's full keybinding set beyond the basics (n/p/u/q)
- Advanced `head`/`tail` negative-offset tricks (`head -n -5 | tail -n +6`) — good to know exists, not worth memorizing yet
- `sort`'s full option set (covered properly in Ch20)

---

## 🎯 What You Should Be Able to Recall After Today
1. The difference between absolute and relative paths
2. `pwd` / `ls` / `cd` and their shortcuts
3. How to read `ls -l` output (permissions, link count, owner, group, size, date, name)
4. What `file` and `less` do
5. The top 5 directories (`/etc`, `/var/log`, `/tmp`, `/home`, `/proc`)
6. `mkdir` / `cp` / `mv` / `rm` / `ln` — syntax and key options (`-r`, `-i`, `-v`, `-f`)
7. The 5 core wildcards (`*`, `?`, `[abc]`, `[!abc]`, `[[:class:]]`)
8. **Hard link = points to the data (inode), survives the original's deletion**
9. **Symbolic link = points to the name, breaks if the original is deleted**
10. Why `rm` is dangerous and the "test with `ls` first" safety habit
11. The 4 types of commands (executable / builtin / function / alias) and how `type` tells them apart
12. **`man <command>` is your default go-to** — `--help` for a quick syntax reminder, `apropos` when you don't know the command's name
13. The 3 file descriptors: `0` stdin, `1` stdout, `2` stderr
14. `>` overwrites, `>>` appends, `&>` does both stdout+stderr at once
15. **`>` connects a command to a file; `|` connects a command to another command**
16. `sort | uniq | wc -l` — the classic "count unique items" pipeline
17. `tee` splits a pipeline: saves a copy to a file **and** passes data onward unchanged
18. `tail -f` for live log monitoring, `2>/dev/null` for silencing permission errors during scans