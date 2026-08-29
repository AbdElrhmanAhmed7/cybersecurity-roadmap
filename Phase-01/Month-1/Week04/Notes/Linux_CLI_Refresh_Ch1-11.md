# 🛡️ Linux Command Line — Quick Refresh (Ch 1-11)
> **Cybersecurity-focused summary** with logical bridges between chapters.  
> Designed for rapid review before labs, CTFs, or interviews.

---

## 🗺️ The Big Picture: How It All Connects

Think of the Linux CLI as a **security analyst's workspace**. The chapters don't exist in isolation — they build a workflow:

```
Ch 1-2 (Navigation) 
    → Ch 3 (Reading the terrain: ls -l, /var/log)
        → Ch 4 (Manipulating evidence: cp, mv, rm, ln)
            → Ch 5 (Finding tools: man, type, alias)
                → Ch 6 (Chaining output: pipes, grep, tee)
                    → Ch 7 (Writing correct commands: quoting, expansion)
                        → Ch 8 (Speed: Tab, Ctrl-r)
                            → Ch 9 (Security backbone: permissions, SUID)
                                → Ch 10 (Live response: ps, top, kill, signals)
                                    → Ch 11 (Persistence & config: env, startup files)
```

**The golden thread:** Everything you type (Ch 1-5) gets **expanded** (Ch 7) → **executed** (Ch 10) → under certain **permissions** (Ch 9) → within an **environment** (Ch 11).

---

## Ch 1-2 — Shell & Navigation: The Foundation

| Concept | One-liner |
|---|---|
| Shell vs Terminal | Terminal = window; Shell = interpreter (bash) |
| Prompt ends in `#` | You're root. Be scared. |
| Absolute path | Starts with `/` — from root |
| Relative path | Starts from `.` (here) or `..` (up) |
| `~` | Home directory; `~user` = that user's home |
| Hidden files | Start with `.`; need `ls -a` |

**The bridge to Ch 3:** Once you can move (`cd`, `pwd`, `ls`), you need to **read** what you find.

---

## Ch 3 — Exploring the System: Reading the Terrain

| Command | Security Use |
|---|---|
| `ls -lh` | Human-readable sizes; spot unusually large logs |
| `ls -la` | Hidden files = malware's favorite hiding spot |
| `file` | Extension means nothing; check real type |
| `less` | Page through logs; `/pattern` to search; `q` to quit |

**Reading `ls -l` (bridge to Ch 9):**
```
-rw-r--r-- 1 root root 32059 Apr 3 11:05 file.odf
│└┬┘└┬┘└┬┘  │   │    │   │    │    └── Name
│ │  │  │   │   │    │   │    └─────── Date
│ │  │  │   │   │    │   └──────────── Size
│ │  │  │   │   └────┴──────────────── Owner & Group
│ │  │  │   └───────────────────────── Hard links
│ └┬┘└┬┘└┬┘────────────────────────── Permissions (rwx × 3)
└───────────────────────────────────── File type (-, d, l)
```

**Key directories for security work:**
- `/etc` — configs (`passwd`, `shadow`, `sudoers`)
- `/var/log` — **the most important place in forensics**
- `/tmp` — world-writable; check for suspicious dropper files
- `/proc` — live kernel state; process introspection

**The bridge to Ch 4:** You can see files. Now you need to **copy, move, link, and delete** them safely.

---

## Ch 4 — File Manipulation: The Tools

### The 5 Core Commands
| Command | Danger Level | Key Options |
|---|---|---|
| `mkdir` | Low | `-p` (create parents) |
| `cp` | Medium | `-r` (directories), `-i` (confirm), `-a` (preserve perms) |
| `mv` | Medium | Same as cp but source is **gone** |
| `rm` | **🔴 EXTREME** | `-r` recursive, `-f` force, `-i` interactive |
| `ln` | Medium | `-s` symbolic link |

**`rm` safety rule (memorize this):** Always test your wildcard with `ls` first, then press `↑` and replace `ls` with `rm`.

### Wildcards (Globbing) — Bridge to Ch 7
| Wildcard | Matches |
|---|---|
| `*` | Any chars |
| `?` | Exactly one char |
| `[abc]` | One char from set |
| `[!abc]` | One char NOT in set |
| `[[:class:]]` | Character class (`upper`, `lower`, `digit`, `alnum`) |

> ⚠️ **Hidden files:** `*` skips dotfiles. Use `.*` but watch out for `.` and `..`

### Hard Links vs Symbolic Links — Bridge to Ch 9
| | Hard Link | Symbolic Link |
|---|---|---|
| Points to | **Inode** (data) | **Filename** (name) |
| Cross filesystem? | ❌ No | ✅ Yes |
| Link to directory? | ❌ No | ✅ Yes |
| Original deleted? | **Still works** | **Broken** (red in `ls`) |
| Security risk | Forensics: data survives deletion | Privilege escalation via symlink attacks |

**The bridge to Ch 5:** You can manipulate files. Now you need to **discover and document** the commands you use.

---

## Ch 5 — Working with Commands: The Manual

### 4 Types of "Commands"
1. **Executable** — file on disk (`/usr/bin/cp`)
2. **Builtin** — part of bash (`cd`, `type`, `alias`)
3. **Function** — mini-script in environment
4. **Alias** — user-defined shortcut

### Documentation Toolkit
| Tool | Use When |
|---|---|
| `type cmd` | "What kind of command is this?" |
| `which cmd` | "Where is the executable?" (only for executables) |
| `man cmd` | **Your default go-to** — the standard reference |
| `man 5 passwd` | File format, not the command |
| `cmd --help` | Quick syntax reminder |
| `apropos keyword` | "I don't know the command name" |
| `alias name='command'` | Create shortcuts (lost after logout unless in startup file) |

**The bridge to Ch 6:** You know the commands. Now you need to **connect them together** and save output.

---

## Ch 6 — Redirection: The Connectors

### The 3 Streams (file descriptors)
| Stream | # | Default | Redirect |
|---|---|---|---|
| stdin | 0 | Keyboard | `<` |
| stdout | 1 | Screen | `>`, `>>` |
| stderr | 2 | Screen | `2>` |

**Critical syntax:**
```bash
command > file        # Overwrite (⚠️ truncates BEFORE command runs!)
command >> file       # Append
command 2> errors.log # Errors only
command &> file       # Both stdout + stderr (modern, clean)
command &>> file      # Both, appended
command > /dev/null 2>&1   # Silence everything
```

### Pipes vs Redirection
| Operator | Connects |
|---|---|
| `>` | Command → **File** |
| `\|` | Command → **Command** |

**Filter pipeline (security bread & butter):**
```bash
cat access.log | grep <IP> | sort | uniq -c | sort -nr
# Count unique occurrences, sorted by frequency
```

**Essential filters:**
| Filter | Function |
|---|---|
| `sort` | Alphabetical sort |
| `uniq` | Remove duplicates (input must be sorted) |
| `uniq -d` | Show duplicates only |
| `wc -l` | Count lines |
| `grep pattern` | Match lines (`-i` case-insensitive, `-v` invert, `-w` whole word) |
| `head -n 5` / `tail -n 5` | First/last N lines |
| `tail -f` | **Live follow** — watch logs in real-time |
| `tee` | Split pipeline: save to file AND pass through |

> 🔐 **Security pattern:** `tail -f /var/log/auth.log | grep Failed` — live monitor brute-force attempts.

**The bridge to Ch 7:** Pipes and redirects use `$VAR`, `*`, and `~`. But the shell **expands** these *before* the command runs. You must understand expansion to avoid silent bugs.

---

## Ch 7 — Expansion & Quoting: The Grammar

**Core principle:** The shell rewrites your command line **before** execution. The command never sees `*`, `~`, or `$VAR`.

### Expansion Types
| Type | Example | Result |
|---|---|---|
| Pathname | `echo D*` | Files starting with D |
| Tilde | `echo ~` / `echo ~bob` | Home directory paths |
| Arithmetic | `echo $((10 / 3))` | `3` (integer only!) |
| Brace | `echo {A,B,C}` | `A B C` |
| Brace range | `mkdir {2007..2009}-{01..12}` | 36 directories |
| Parameter | `echo $USER` | Variable value |
| Command subst. | `echo $(date)` | Output of inner command |

### Quoting Hierarchy
| Level | What it blocks | What survives |
|---|---|---|
| None | Nothing | Everything expands |
| `" "` Double | Pathname, tilde, brace, word-splitting | `$VAR`, `$(cmd)`, `\` |
| `' '` Single | **Everything** | Nothing — literal output |

**Security-critical use case:**
```bash
grep '^[0-9]*$' file.log   # Single quotes protect regex from shell expansion
```

> ⚠️ **Silent failure:** Misspelled variables (`$SUER`) return empty string, no error.

**The bridge to Ch 8:** Now that your commands are syntactically correct, speed up typing them.

---

## Ch 8 — Keyboard Tricks: The Speed

> The book calls this chapter **optional**. Learn two things, ignore the rest for now.

| Shortcut | Action | Why It Matters |
|---|---|---|
| `Tab` (×2) | Complete filenames/commands | Saves more time than everything else combined |
| `Ctrl-r` | Reverse history search | Find that complex `find` or `grep` pipeline you built earlier |
| `Ctrl-a` / `Ctrl-e` | Jump to start/end of line | Fast editing of long commands |
| `Ctrl-u` / `Ctrl-k` | Delete to start/end | Quick cleanup |

**The bridge to Ch 9:** You can navigate, manipulate, and type fast. Now you hit the **security backbone**: who can access what?

---

## Ch 9 — Permissions: The Security Backbone

### Identity Levels
| Level | Scope |
|---|---|
| Owner (user) | The file's owner |
| Group | A defined set of users |
| Other | Everyone else on the system |

### `rwx` Meaning (FILES vs DIRECTORIES)
| | On Files | On Directories |
|---|---|---|
| `r` | Read contents | List contents |
| `w` | Write/truncate | **Create/delete/rename files inside** |
| `x` | Execute | **Enter** (`cd`), access metadata, use files inside |

> 🚨 **Counter-intuitive:** You can delete a file you don't own if you have `w` on its **parent directory**.

### Octal Shortcuts (memorize these 5)
| Octal | Meaning | Use Case |
|---|---|---|
| `7` | `rwx` | Full control |
| `6` | `rw-` | Standard file |
| `5` | `r-x` | Standard directory / program |
| `4` | `r--` | Read-only |
| `0` | `---` | No access |

```bash
chmod 600 file    # Private file
chmod 755 dir     # Enterable, listable directory
chmod u+x file    # Add execute for owner
```

### Special Permissions (the 4th digit)
| Permission | Octal | Symbol | Effect |
|---|---|---|---|
| **SUID** | `4000` | `s` in owner `x` | Runs as **file owner** (privesc vector!) |
| **SGID** | `2000` | `s` in group `x` | On dirs: new files inherit dir's group |
| **Sticky** | `1000` | `t` at end | Only owner/root can delete files in dir |

> 🔴 **SUID audit:** `find / -perm -4000 2>/dev/null` — classic first step in privilege escalation enumeration.

### `umask` — Default Permissions at Creation
- Mask = bits to **subtract** from default (`rw-rw-rw-` for files)
- `umask 0002` = remove world-write → `rw-rw-r--`
- `umask 0022` = remove group-write AND world-write → `rw-r--r--`

### Identity Switching
| Command | Password Needed | Use Case |
|---|---|---|
| `su -` | Root's password (often disabled) | Switch to root shell |
| `sudo cmd` | **Your own** password | Run single command as root (modern standard) |
| `sudo -i` | Your password | Interactive root shell |

### Shared Directory Setup (Practical Workflow)
```bash
sudo groupadd team
sudo usermod -a -G team user1
sudo usermod -a -G team user2
sudo mkdir /shared
sudo chown :team /shared
sudo chmod 2775 /shared      # SGID + rwxrwxr-x
umask 0002                   # Keep group-write on new files
```

**The bridge to Ch 10:** Files have permissions. **Running programs** (processes) also have an identity (uid/euid) and can be inspected, controlled, and killed.

---

## Ch 10 — Processes: The Running System

### Key Concepts
- **PID** = unique process ID; `init` is always PID 1
- **Parent/Child** = processes launch processes; tracked by kernel
- **Daemon** = background service with no UI

### Process Inspection
| Command | What It Shows |
|---|---|
| `ps` | Your terminal's processes |
| `ps x` | All your processes (+ STAT column) |
| `ps aux` | **Every process on the system** — the big one |
| `top` | Live, updating view sorted by CPU |

**Process States:**
| State | Meaning |
|---|---|
| `R` | Running/ready |
| `S` | Sleeping (waiting for event) |
| `D` | Uninterruptible sleep (I/O) |
| `T` | Stopped |
| `Z` | **Zombie** — finished but parent hasn't cleaned up |

**`top` load average:** Under 1.0 = machine isn't busy. Values are 1min, 5min, 15min averages.

### Job Control
| Action | Command |
|---|---|
| Background at launch | `cmd &` |
| Stop foreground | `Ctrl-z` |
| Resume in background | `bg %1` |
| Resume in foreground | `fg %1` |
| List jobs | `jobs` |

### Signals (the real mechanism behind "killing")
| Signal | # | Meaning |
|---|---|---|
| `HUP` (1) | Hangup / reload config |
| `INT` (2) | Interrupt (`Ctrl-c`) |
| `KILL` (9) | **Forced termination** — cannot be caught or ignored |
| `TERM` (15) | Polite termination (default) |
| `STOP` (19) | Pause — cannot be caught |
| `TSTP` (20) | Terminal stop (`Ctrl-z`) — can be caught |

```bash
kill -9 PID      # Nuclear option — last resort
killall name     # Kill all processes by name
nohup cmd &      # Survive terminal disconnect
```

> 🔐 **Security note:** Malware may ignore `TERM` and require `KILL`. `nohup` is used for persistence (keep running after SSH disconnect).

**The bridge to Ch 11:** Processes run within an **environment** inherited from their parent. Startup files define that environment, and variables control tool behavior.

---

## Ch 11 — The Environment: The Context

### What Is Stored?
The environment holds **environment variables** (inherited by child processes) and **shell variables** (local to current shell), plus aliases and functions.

### Key Commands
| Command | Purpose |
|---|---|
| `printenv` | Show environment variables only |
| `set` | Show shell + environment variables + functions |
| `echo $VAR` | Show one variable's value |
| `export VAR=value` | Make shell variable available to children |
| `source file` | Execute file in current shell (apply changes immediately) |
| `alias` | List all aliases |

### Important Environment Variables
| Variable | Controls |
|---|---|
| `PATH` | Colon-separated list of directories searched for executables |
| `HOME` | Your home directory |
| `USER` | Your username |
| `SHELL` | Your default shell |
| `PS1` | Your prompt string (customizable) |
| `PWD` / `OLDPWD` | Current / previous directory |
| `EDITOR` / `PAGER` | Default text editor / page viewer |
| `LANG` | Character set and language |
| `HISTSIZE` / `HISTCONTROL` | History length and behavior |

### Startup Files Sequence
**Login shell** (username + password):
1. `/etc/profile` (global)
2. `~/.bash_profile` → `~/.bash_login` → `~/.profile` (first found wins)

**Non-login shell** (terminal in GUI):
1. `/etc/bash.bashrc` (global)
2. `~/.bashrc` (personal)

> **Key insight:** `~/.bashrc` is almost always read. Login shells usually source it via `~/.bash_profile`.

### How `PATH` Works
```bash
PATH=$PATH:$HOME/bin
export PATH
```
- The shell searches `PATH` directories **left-to-right** to find executables
- Adding `$HOME/bin` lets you run personal scripts without typing full paths

### Variable Scope: Parent vs Child
```bash
foo="bar"        # Shell variable (local)
bash             # Launch child shell
echo $foo        # Empty — not inherited!
exit
export foo="bar" # Environment variable
echo $foo        # Now it's inherited
```
> **Rule:** A child cannot alter its parent's environment.

### Temporary Environment
```bash
MANWIDTH=75 man ls       # One-shot variable for this command only
alias man='MANWIDTH=75 man'  # Make it permanent (for the session)
```

### Modifying Startup Files Safely
1. **Always backup first:** `cp .bashrc .bashrc.bak`
2. **Add comments** explaining your changes
3. **Activate without logout:** `source ~/.bashrc`

**Common `.bashrc` additions:**
```bash
# Shared directory fix
umask 0002

# History tuning
export HISTCONTROL=ignoredups
export HISTSIZE=1000

# Aliases
alias ll='ls -l --color=auto'
alias l.='ls -d .* --color=auto'
```

> 🔐 **Security note:** Startup files (`~/.bashrc`, `~/.bash_profile`) are prime targets for persistence. Attackers add reverse shells or alias hijacking (`alias ls='ls --color=auto; evil_cmd'`). Always audit these files on compromised systems.

---

## 🔗 Practical Bridge: FilePermissionsChecker (Day37)

This project connects **Ch 4 (wildcards)**, **Ch 7 (quoting/expansion)**, and **Ch 9 (permissions)** into real Python code.

### Key Lessons Applied
| Lesson | Chapter Source |
|---|---|
| `~` doesn't expand in `pathlib` — use `.expanduser()` | Ch 7 (Tilde Expansion) |
| Check SUID via bitmask `stat.S_ISUID`, not string parsing | Ch 9 (Special Permissions) |
| Check world-writable via fixed index `[8]`, not pattern matching | Ch 9 (Permission Structure) |
| Avoid `subprocess` + `shell=True` to prevent injection | Ch 6 (Redirection / Security) |
| `argparse` defaults can break `is not None` validation | Ch 5 (Command Design) |

**The security mindset:** "Code that runs without errors isn't necessarily correct." Test edge cases: SUID without execute (`rwSr-xr-x`), world-writable without world-readable (`-rw-rw--w-`), sticky bits, etc.

---

## 🎯 The Security Analyst's Workflow (All Chapters Combined)

```bash
# 1. Navigate to evidence (Ch 1-2)
cd /var/log

# 2. Inspect with correct permissions in mind (Ch 3, 9)
ls -la

# 3. Search logs using pipes and filters (Ch 6)
tail -n 1000 auth.log | grep "Failed password" | sort | uniq -c | sort -nr

# 4. Save output safely with quoting (Ch 7)
tee "attack_summary_$(date +%F).txt"

# 5. Check for suspicious processes (Ch 10)
ps aux | grep -i suspicious

# 6. Hunt for SUID binaries (Ch 9)
find / -perm -4000 2>/dev/null

# 7. Check environment for persistence (Ch 11)
cat ~/.bashrc | grep -E "alias|export|source"
```

---

## 💬 My Review & Recommendations

### What's Excellent
1. **Practical filtering:** Removing GUI/historical trivia keeps the signal-to-noise ratio high. This is exactly how technical books should be summarized.
2. **Security framing:** Every chapter explicitly maps to real attack/defense scenarios (SUID hunting, log analysis, symlink attacks, persistence in startup files).
3. **The Day37 bridge:** Seeing theoretical permission bugs (string parsing vs bitmask) in actual code solidifies Ch 9 concepts better than any table.
4. **"Intentionally Left Out" sections:** Shows mature judgment — knowing what *not* to memorize is as important as knowing what to memorize.

### Suggested Additions
1. **Add a "Common Mistakes" box** per chapter — e.g., `rm * .txt` (extra space), `2>&1 > file` (wrong order), unquoted `$1`.
2. **Link Ch 11 to Ch 5:** Mention that `alias` in Ch 5 is temporary unless written to `~/.bashrc` (Ch 11).
3. **Link Ch 10 to Ch 9:** Processes have effective UID/GID (euid/egid) — a root-owned SUID binary spawns a process with euid=0, which is why `ps aux` shows the *real* owner, not the effective one.
4. **Add a "One-Command Review" section:** A single complex pipeline that uses concepts from Ch 1-11 together.

### The Logical Flow Verdict
The progression from **navigation → inspection → manipulation → discovery → chaining → syntax → speed → security → processes → environment** is pedagogically sound. Each chapter answers a question raised by the previous one:
- Ch 1-2: "How do I move around?" → Ch 3: "What am I looking at?"
- Ch 3: "What are these permission strings?" → Ch 9: "How do they work?"
- Ch 9: "Who owns this file?" → Ch 10: "What processes are they running?"
- Ch 10: "How did this process get its settings?" → Ch 11: "From the environment."

**Overall rating:** This is a textbook example of how to study for applied cybersecurity — theory immediately grounded in operational relevance.

---

## ✅ Quick Recall Checklist

After reading this refresh, you should be able to:
- [ ] Navigate with absolute/relative paths and `cd` shortcuts
- [ ] Read `ls -l` output and identify file type + permissions
- [ ] Use `cp -r`, `mv`, `rm -rf` safely (test with `ls` first!)
- [ ] Explain hard vs symbolic links and their security implications
- [ ] Chain commands with `|` and redirect with `>`, `>>`, `2>`, `&>`
- [ ] Use `grep`, `sort`, `uniq`, `wc -l`, `tee`, `tail -f` in pipelines
- [ ] Quote correctly: double quotes for "most stuff", single quotes for regex
- [ ] Use `Tab` and `Ctrl-r` efficiently
- [ ] Read and set permissions in octal (7/6/5/4/0) and symbolic (`u+x`)
- [ ] Explain SUID/SGID/Sticky bit and run `find / -perm -4000`
- [ ] Understand `umask` and set up a shared directory with SGID
- [ ] Inspect processes with `ps aux` and `top`; understand load average
- [ ] Send signals: `TERM` vs `KILL`, `HUP` for config reload
- [ ] Know the difference between shell variables and environment variables
- [ ] Edit and source `~/.bashrc` safely with backups

---

> *"The command line is not just a tool — it's the forensic lens through which you understand a system's true state."*
