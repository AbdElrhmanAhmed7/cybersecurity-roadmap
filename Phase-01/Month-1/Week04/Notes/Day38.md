# Summary Ch 10 — Processes
> This chapter explains how Linux tracks every running program, and gives you the tools to inspect, control, and terminate them. Directly relevant to security work: process monitoring is how you spot suspicious activity, and signal handling is how you (or an attacker) can kill, pause, or manipulate running programs.

---

## How Processes Work — The Big Picture

### Multitasking, in one sentence
The kernel creates the *illusion* of running many programs simultaneously by rapidly switching the CPU between them. Each running program instance is tracked as a **process**.

### Boot sequence (just enough to understand what you'll see in `ps`)
```
kernel → init (PID 1) → systemd → all system services
```
- **`init`** is always the very first process, and it **always gets PID 1**
- Many system services run as **daemons** — programs with no user interface that just sit in the background doing their job (this is why your system is "doing stuff" even when you're not logged in)

### Parent and Child Processes
Any process can launch another process. The launcher is the **parent**, the launched one is the **child**. This relationship is tracked by the kernel and is why tools like `pstree` can show you a tree structure.

### What the Kernel Tracks Per Process
- **PID** (Process ID) — a unique number, assigned in ascending order
- Memory usage
- Whether it's ready to resume execution
- Owner / user ID / effective user ID (yes — processes have permissions too, just like files)

---

## Viewing Processes: `ps`

### Bare `ps` — only shows processes tied to your current terminal
```bash
ps
  PID TTY          TIME CMD
 5198 pts/1    00:00:00 bash
10129 pts/1    00:00:00 ps
```
| Column | Meaning |
|---|---|
| `PID` | Process ID |
| `TTY` | Controlling terminal ("teletype" — a legacy Unix term) |
| `TIME` | Total CPU time consumed (not wall-clock time) |
| `CMD` | The command that launched it |

### `ps x` — show ALL your processes, regardless of terminal
```bash
ps x
```
A `?` in the TTY column means "no controlling terminal" (common for background daemons). This adds a **STAT** (state) column:

| State | Meaning |
|---|---|
| `R` | Running or ready to run |
| `S` | Sleeping — waiting for an event (keystroke, network packet, etc.) |
| `D` | Uninterruptible sleep — waiting on I/O (e.g. disk) |
| `T` | Stopped |
| `Z` | **Zombie** — child process that finished but its parent hasn't "cleaned it up" yet |
| `<` | High priority ("less nice" — takes more CPU time from others) |
| `N` | Low priority ("nice" — only gets CPU time after higher-priority processes are served) |

### `ps aux` — the big one: every process, every user
```bash
ps aux
USER    PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root      1  0.0  0.0   2136   644 ?        Ss   Mar05   0:31 init
```
| Column | Meaning |
|---|---|
| `USER` | Process owner |
| `%CPU` | CPU usage percentage |
| `%MEM` | Memory usage percentage |
| `VSZ` | Virtual memory size |
| `RSS` | **Resident Set Size** — actual physical RAM used (in KB) |
| `START` | When it started |

**Note the "no dash" style:** `ps x`, `ps aux` — these are BSD-style options (no leading `-`), which is the conventional way to invoke them, even though `ps` also supports Unix-style dashed options.

```bash
ps uw 44719      # detailed snapshot of one specific PID
```

**Practical tip:** `ps aux` output is long — pipe it: `ps aux | less` or filter it: `ps aux | grep firefox`

---

## Viewing Processes Live: `top`

`ps` is a **snapshot** — a single moment in time. `top` is a **continuously updating** view (refreshes every 3 seconds by default), sorted by CPU activity.

```bash
top
```

### Reading the summary header
```
top - 14:59:20 up  6:30,  2 users,  load average: 0.07, 0.02, 0.00
Tasks: 109 total,   1 running, 106 sleeping,   0 stopped,   2 zombie
Cpu(s):  0.7%us,  1.0%sy,  0.0%ni, 98.3%id,  0.0%wa
Mem:    319496k total,   314860k used,     4636k free
```

| Field | Meaning |
|---|---|
| `up 6:30` | Uptime — time since last boot |
| `load average: 0.07, 0.02, 0.00` | Number of processes waiting for CPU time, averaged over **1 min, 5 min, 15 min** respectively. **Values under 1.0 = machine isn't busy.** |
| `Tasks:` | Breakdown of process counts by state |
| `%us` | CPU time spent on user processes (outside the kernel) |
| `%sy` | CPU time spent on system/kernel processes |
| `%ni` | CPU time spent on "nice" (low-priority) processes |
| `%id` | CPU idle percentage |
| `%wa` | CPU time waiting on I/O |

**Keyboard commands inside `top`:** `h` = help, `q` = quit

**Why `top` is preferred over graphical system monitors:** it's fast and uses very few system resources itself — a heavy graphical monitor risks *becoming* the source of the slowdown you're trying to diagnose. This matters especially on servers or resource-constrained systems.

---

## Controlling Processes: Foreground, Background, and Job Control

### The Core Problem
When you run a program normally, your shell **waits** for it to finish before giving you the prompt back — this is why the prompt doesn't return while a GUI program window is open.

### Interrupting: Ctrl-c
```bash
xlogo
# (window opens, prompt doesn't return)
# press Ctrl-c
```
Politely asks the foreground program to terminate. Works on most (not all) command-line programs.

### Backgrounding a process: `&`
```bash
xlogo &
[1] 28236
```
- `[1]` = **job number**
- `28236` = **PID**
- The prompt returns immediately, and the program keeps running behind the scenes

```bash
xlogo & gedit &     # launch multiple programs in the background at once
```

### `jobs` — list your background jobs
```bash
jobs
[1]+  Running                 xlogo &
```

### `fg` — bring a background job back to the foreground
```bash
fg %1        # %1 is the "jobspec" — the % plus job number
fg           # jobspec optional if there's only one background job
```
⚠️ A backgrounded process **ignores Ctrl-c** entirely — you must `fg` it first before you can interrupt it that way.

### Ctrl-z — stop (pause) a foreground process without killing it
```bash
xlogo
# press Ctrl-z
[1]+  Stopped                 xlogo
```
The process is now paused (not running, not terminated). From here:
```bash
bg %1        # resume it, but in the background
fg %1        # resume it, back in the foreground
```

### Why launch a GUI program from the terminal at all?
1. Some programs (like `xlogo`) aren't in any menu
2. **You get to see error messages** that would otherwise be invisible — a program that silently fails to open from a desktop icon might explain exactly why when launched from the command line

---

## Process Priority: `nice` and `renice`

### The concept: "niceness"
Every process has a **niceness** value controlling its scheduling priority — how much CPU time it gets relative to other processes.

| Value | Meaning |
|---|---|
| `-20` | Most favorable (highest priority) — process is **"less nice"** because it hogs more CPU from everyone else |
| `0` | Default |
| `19` | Least favorable (lowest priority) — process is **"nice"** because it yields CPU to others |

⚠️ **Only the superuser can *increase* a process's priority** (make it less nice / more negative). Regular users can only decrease priority on processes **they own**.

```bash
nice -n 10 cpu-hog              # launch a new process with lower priority
sudo nice -n -10 must-run-fast   # launch with higher priority (requires root)

ps                                # find the PID first
renice -n 19 379215               # adjust priority of an ALREADY-RUNNING process
```

**When you'd actually use this:** giving a heavy background task (video encoding, compiling) lower priority so it doesn't make your interactive work sluggish, or giving a latency-critical process higher priority. Rarely needed day-to-day — and increasing priority carries real risk of starving essential system processes.

---

## Signals — The Real Mechanism Behind "Killing" a Process

### Critical concept: `kill` doesn't just "kill" — it sends **signals**
Signals are how the OS communicates with running programs. `Ctrl-c` and `Ctrl-z` are actually signals in disguise:
- `Ctrl-c` → sends the **INT** (interrupt) signal
- `Ctrl-z` → sends the **TSTP** (terminal stop) signal

Programs can "listen" for signals and choose how to react — e.g. saving unsaved work before terminating when it receives a termination signal.

### `kill` syntax
```bash
kill [-signal] PID...
```
If you don't specify a signal, it defaults to sending **TERM**.

### The Signals You'll Actually Use

| # | Name | Meaning |
|---|---|---|
| 1 | `HUP` | Hangup — sent when the controlling terminal closes. Also used by many daemons to mean "reload your config" (e.g. Apache) |
| 2 | `INT` | Interrupt — same as Ctrl-c |
| 9 | `KILL` | **Immediate, forced termination.** The kernel kills the process directly — it's **never actually delivered** to the program, so the program gets **zero chance to clean up or save work**. Use only as a last resort. |
| 15 | `TERM` | Terminate — the **default** signal `kill` sends. A "polite" request the program can still respond to before exiting. |
| 18 | `CONT` | Continue — resumes a stopped process (this is what `bg`/`fg` send) |
| 19 | `STOP` | Pause a process. Like `KILL`, it's **never delivered to the program** — cannot be ignored. |
| 20 | `TSTP` | Terminal stop — what Ctrl-z sends. Unlike `STOP`, the program **does** receive this and can choose to ignore it. |

**Other signals worth recognizing:**
| # | Name | Meaning |
|---|---|---|
| 3 | `QUIT` | Quit |
| 11 | `SEGV` | Segmentation violation — the program tried to access memory it wasn't allowed to touch |
| 28 | `WINCH` | Window changed size (some programs like `top`/`less` redraw themselves in response) |

### Sending Signals — 3 equivalent ways to specify them
```bash
kill -1 13546          # by number
kill -INT 13601         # by name
kill -SIGINT 13608       # by name with SIG prefix
```

**Ownership requirement:** you can only signal processes you own, unless you're the superuser.

**Full list of all signals:**
```bash
kill -l
```

### `nohup` — Make a Process Immune to Hangup
```bash
nohup xlogo
```
Normally, closing the terminal sends `HUP` and kills the foreground program running in it. `nohup` prevents this — useful for long-running tasks you want to survive a closed terminal/SSH disconnect.

### `killall` — Signal Multiple Processes by Name
```bash
killall xlogo                # kills every process named "xlogo"
killall -u username processname   # kill by owner
```
Same ownership rule applies — superuser privileges needed to signal processes you don't own.

---

## Shutting Down the System

```bash
sudo reboot           # restart
sudo halt              # stop, don't power off
sudo poweroff           # stop and power off
sudo shutdown -h now     # halt, right now
sudo shutdown -r now      # reboot, right now
```
`shutdown` is the most flexible — it supports a time delay and **broadcasts a warning to all logged-in users** before the event happens (relevant on shared/multi-user systems).

---

## Other Process-Related Commands (Good to Know Exist)

| Command | Function |
|---|---|
| `pstree` | Shows processes as a tree, visualizing parent-child relationships |
| `vmstat` | Snapshot of memory/swap/disk I/O usage. `vmstat 5` = continuous updates every 5 seconds |
| `xload` / `tload` | Graphs of system load over time (GUI / terminal respectively) |

---

## 🔐 Why This Chapter Matters for Security Work
- **`ps aux`** is one of the first things you check when investigating a compromised or suspicious system — unfamiliar processes, unexpected owners, odd CPU/memory usage are all red flags
- **Zombie processes (`Z` state)** in unusual numbers can indicate a poorly-written or malicious program not cleaning up after its children
- Understanding **signals** matters for both attacking and defending: malware may specifically ignore `TERM` and require `KILL`; some persistence mechanisms respond to `HUP` by respawning
- **`kill -9` (SIGKILL)** is the "nuclear option" — a process that survives `kill -TERM` (won't respond politely) may need it, but you lose any chance at clean shutdown or forensic state
- **`nohup`** is exactly the mechanism attackers (and legitimate admins) use to keep a process running after a terminal/session disconnects — relevant to understanding persistence
- `top`/`ps` load-average and CPU spikes are often the first visible sign of cryptomining malware or a resource-exhausting attack running on a system

---

## ⚠️ Intentionally Left Out (not needed right now)
- Full `ps` option reference beyond `x`, `aux`, `uw <pid>` — man page has dozens more, situational
- GUI system monitors (Task Manager equivalents) — the chapter itself says CLI tools are strictly better for this
- Deep detail on every possible process state suffix character beyond the main table
- `xload`/`tload` in practical depth — nice to know they exist, not something you'll use often

---

## 🎯 What You Should Be Able to Recall After Today
1. **PID** = unique process ID; `init` is always PID 1; processes have parent-child relationships
2. `ps` = one-time snapshot; `top` = continuously updating live view
3. `ps aux` shows every process on the system, with owner, CPU%, memory%, and state
4. Key process states: `R` running, `S` sleeping, `D` uninterruptible sleep (I/O wait), `Z` zombie, `T` stopped
5. `top`'s **load average** (1/5/15 min) — under 1.0 means the machine isn't busy
6. `&` backgrounds a process at launch; `Ctrl-z` stops a foreground process; `bg`/`fg` move jobs between background/foreground
7. `jobs` lists your background jobs; jobspecs are referenced as `%1`, `%2`, etc.
8. **`kill` sends signals, it doesn't directly "kill"** — default signal is `TERM` (15), polite and interceptable
9. **`SIGKILL` (9) and `SIGSTOP` (19) can never be intercepted or ignored by the target process** — the kernel forces them directly
10. `HUP` (1) = hangup, often reused by daemons to mean "reload config"
11. `nohup` protects a process from being killed when its terminal closes
12. `killall <name>` signals every process matching a program name; requires ownership or superuser privileges
13. `nice`/`renice` control CPU scheduling priority — lower niceness value = higher priority; only root can increase priority