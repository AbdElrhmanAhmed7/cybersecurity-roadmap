# Summary Ch 9 — Permissions
> This chapter is the security backbone of everything else in your roadmap. Take your time with it — it's dense, but every concept here maps directly to real attack/defense scenarios you'll deal with constantly.

---

## Why This Chapter Exists: The Multi-User Model
Linux was designed from day one to support **multiple users on the same machine at the same time** (originally: one big central computer, many terminals connected to it). To make that safe, the system needed a way to stop users from interfering with each other's files — that's the entire reason permissions exist.

Even on a single-user personal machine today, this model still matters: it's what stops a regular user account (or malware running under it) from touching system-critical files without explicit elevated access.

---

## Identity: Users, Groups, and "Everybody Else"

### The 3 Levels of Access
| Level | Meaning |
|---|---|
| **Owner (user)** | The specific user who owns the file |
| **Group** | A set of users who share access, defined by the owner |
| **Other** (a.k.a. "world") | Everyone else on the system |

### `id` — See Your Own Identity
```bash
id
# uid=1000(me) gid=1000(me) groups=4(adm),20(dialout),24(cdrom),...
```
| Term | Meaning |
|---|---|
| `uid` | User ID — a number, mapped to your username for human convenience |
| `gid` | Your **primary** group ID |
| `groups` | All the additional groups you belong to |

**Where this data actually lives:**
| File | Contains |
|---|---|
| `/etc/passwd` | Username, uid, gid, real name, home directory, login shell |
| `/etc/group` | Group definitions |
| `/etc/shadow` | Password hashes (this is why you get "Permission denied" trying to read it as a regular user — that's *correct*, expected behavior) |

**Note:** the superuser (`root`) is always `uid=0`. Modern Linux practice gives each regular user their own unique, single-member group (usually same name as the username) rather than dumping everyone into one shared "users" group — this makes permission management cleaner.

---

## Reading `ls -l` Output — The Core Skill of This Chapter

```bash
-rw-rw-r-- 1 me me 0 2016-03-06 14:52 foo.txt
```

### First character = file type
| Char | Type |
|---|---|
| `-` | Regular file |
| `d` | Directory |
| `l` | Symbolic link (permissions shown are always dummy `rwxrwxrwx` — the *real* permissions belong to the target file) |
| `c` | Character special file (e.g. a terminal, `/dev/null`) |
| `b` | Block special file (e.g. a disk device) |

### Next 9 characters = the file mode, in 3 groups of 3
```
User  Group  Other
rwx   rwx    rwx
```

### What `r`, `w`, `x` actually mean — **this differs between files and directories**, and this is the part most people gloss over

| Attribute | On Files | On Directories |
|---|---|---|
| `r` | Open and read the file's contents | List the directory's contents (but you can't see file *details* without `x` too) |
| `w` | Write to or truncate the file — **but does NOT allow renaming or deleting it** | Create, delete, and rename files inside — **but only if `x` is also set** |
| `x` | Execute the file as a program (scripts also need `r` to run) | Enter the directory (`cd`) and access its metadata (`ls -l`); required for `cp`, `rm`, `mv` to work on files inside |

⚠️ **The single most counter-intuitive fact in this chapter:** whether you can **delete or rename a file** depends on the **write permission of the directory it's in** — not the permissions of the file itself. You can have zero permissions on a file and still delete it, if you have write access to its parent directory. This trips up almost everyone the first time.

### Worked Examples
| Permissions | Meaning |
|---|---|
| `-rwx------` | Owner: full access. Nobody else can do anything. |
| `-rw-r--r--` | Owner: read/write. Group and others: read only. (Common default for regular files) |
| `-rwxr-xr-x` | Owner: full access. Everyone else: read + execute. (Common for programs) |
| `drwxrwx---` | Directory. Owner and group can enter and create/delete/rename files inside. Others: nothing. |
| `drwxr-x---` | Directory. Owner has full control. Group can enter and browse, but **cannot** create/delete/rename files. |

---

## `chmod` — Changing Permissions
Only the file's **owner** or the **superuser** can change its mode. Two ways to do it:

### Method 1: Octal (Numeric) Notation

**Why octal specifically?** Because each permission group (`rwx`) is exactly 3 bits — and octal digits represent exactly 3 binary digits each. It's a clean, compact way to express 3 yes/no flags per digit.

| Binary | Octal | Meaning |
|---|---|---|
| `000` | 0 | `---` (nothing) |
| `001` | 1 | `--x` |
| `010` | 2 | `-w-` |
| `011` | 3 | `-wx` |
| `100` | 4 | `r--` |
| `101` | 5 | `r-x` |
| `110` | 6 | `rw-` |
| `111` | 7 | `rwx` |

**You only really need to memorize 5 values:** `7` (rwx), `6` (rw-), `5` (r-x), `4` (r--), `0` (---). Everything else is a combination of these.

```bash
chmod 600 file    # owner: rw-, group: none, other: none
chmod 644 file    # owner: rw-, group: r--, other: r--   (typical file default)
chmod 755 file    # owner: rwx, group: r-x, other: r-x   (typical program/directory default)
chmod 700 file    # owner: rwx, group: none, other: none (fully private)
```

### Method 2: Symbolic Notation
Format: **who** + **operation** + **permission**

| Who | Meaning |
|---|---|
| `u` | user (owner) |
| `g` | group |
| `o` | other |
| `a` | all (default if you specify nobody) |

| Operation | Meaning |
|---|---|
| `+` | add a permission |
| `-` | remove a permission |
| `=` | set exactly these permissions, remove everything else |

```bash
chmod u+x file        # add execute for owner only
chmod u-x file        # remove execute from owner
chmod +x file          # add execute for everyone (same as a+x)
chmod o-rw file        # remove read+write from "other"
chmod go=rw file       # set group AND other to exactly rw- (removes x if it was there)
chmod u+x,go=rx file   # multiple changes at once, comma-separated
```

**When to use which method:** octal is faster once you're fluent; symbolic is better when you want to change *just one* permission bit without needing to know or recalculate the full current mode.

⚠️ **Caution with `chmod --recursive`:** it applies the same mode to both files and directories inside a tree — but files and directories usually need *different* modes (e.g. a directory needs `x` to be enterable, most files don't need `x` at all). Recursive chmod is rarely the clean solution it looks like.

---

## `umask` — Controlling *Default* Permissions on New Files

### The concept
`umask` is a **mask** — a set of bits to *subtract* from the maximum default permissions whenever a new file or directory is created. It doesn't change existing files; it only affects what happens at creation time.

```bash
umask        # shows current mask, e.g. 0002
```

### How the subtraction works
Wherever a `1` bit appears in the mask (in binary), that permission gets **removed** from the default.

```
Default max for a new file:  rw- rw- rw-
Mask 0002 in binary:         000 000 010
Result:                       rw- rw- r--   ← world "write" got removed
```

```
Default max for a new file:  rw- rw- rw-
Mask 0022 in binary:         000 010 010
Result:                       rw- r-- r--   ← group AND world "write" removed
```

```bash
umask 0000    # turns masking off entirely — new files become world-writable (rw-rw-rw-)
umask 0002    # common default — blocks world write only
umask 0022    # common default — blocks group AND world write
```

**Practical note:** you rarely need to touch this — the distro default is fine — but in shared-directory / high-security setups it matters a lot (see the `janet`/`tony` example below).

---

## Special Permissions — the 4th Octal Digit

You'll usually see permissions as 3 digits (`644`, `755`), but there's technically a **4th, leading digit** for special permissions, defaulting to `0` when omitted.

### 1️⃣ SUID — setuid bit (`4000`)
Applies to **executable files**. When set, the program runs with the **effective privileges of its owner** — not the privileges of whoever launched it.

```bash
ls -l /usr/bin/passwd
-rwsr-xr-x
```
The lowercase `s` replacing the owner's `x` means SUID is active (and execute permission is also present — if execute were missing, you'd see a capital `S` instead).

**Why it exists:** a regular user running `passwd` needs to modify `/etc/shadow`, which regular users can't write to directly. Since `passwd` is owned by `root` and has SUID set, it temporarily runs *as root* just long enough to make that change, then returns control normally.

🚨 **Security-critical fact:** because SUID grants elevated privileges, the number of SUID programs on any system should be kept to an absolute minimum. Any unnecessary or misconfigured SUID binary is a direct **privilege escalation** path — this is exactly why `find / -perm -4000` is one of the first commands run during security auditing or penetration testing enumeration.

### 2️⃣ SGID — setgid bit (`2000`)
Same idea as SUID, but for the **group** instead of the owner. Behaves differently depending on what it's applied to:

- **On an executable file:** the program runs with the privileges of the file's **group owner**.
- **On a directory (the far more common use):** any **new file created inside inherits the directory's group ownership**, instead of the creator's own primary group.

```bash
drwxrwsr-x    # lowercase 's' in the group execute position = SGID active
```

**Why this matters practically:** in a shared team directory, without SGID, every new file takes on the *creator's* personal group — meaning teammates might not automatically have access to files their colleagues create. With SGID set on the directory, every file created inside automatically belongs to the shared team group, so everyone retains access consistently.

### 3️⃣ Sticky Bit (`1000`)
Applies **only to directories** (Linux ignores it on files entirely — it's a legacy Unix leftover).

**Effect:** in a directory with the sticky bit set, users can create files freely, but **can only delete or rename a file if they are**: the file's owner, the directory's owner, or the superuser.

```bash
drwxrwxrwt    # lowercase 't' at the end = sticky bit active (world-writable directory)
```

**Classic example: `/tmp`.** It's world-writable (`777`) so anyone can create temp files there — but without the sticky bit, anyone could also **delete anyone else's files**. The sticky bit closes that hole: you can only remove what you own.

### Setting Special Permissions
```bash
chmod u+s program    # SUID
chmod g+s dir          # SGID
chmod +t dir            # Sticky bit
```
Or numerically, as the leading 4th digit: `chmod 4755 program`, `chmod 2775 dir`, `chmod 1777 dir`.

### Quick Reference Table
| Permission | Octal | Applies to | Effect | Symbol in `ls -l` |
|---|---|---|---|---|
| SUID | `4000` | Executable files | Runs as the file's **owner** | `s` in owner's `x` position |
| SGID | `2000` | Files or directories | On dirs: new files inherit the **directory's group** | `s` in group's `x` position |
| Sticky Bit | `1000` | Directories only | Only owner/file-owner/root can delete files | `t` at the very end |

---

## Changing Identity: `su` vs `sudo`

There are 3 ways to act as another user; logging out and back in is impractical, so in practice it's `su` or `sudo`.

### `su` — Switch User (older approach)
```bash
su          # switch to root — asks for ROOT's password
su -        # same, but also loads root's environment + changes to root's home dir (the "-l" flag, commonly abbreviated as just "-")
su -c 'command'    # run a single command as root, then return
```
⚠️ **Modern distros (Ubuntu and most others) disable the root account's password entirely by default.** This means plain `su` will *always* fail with "Authentication failure" — not because you typed the wrong password, but because there is no valid password to check against. This is expected behavior, not a bug.

### `sudo` — Execute As Another User (modern standard)
```bash
sudo command       # run a single command with elevated privileges
sudo -i              # start an interactive root shell (roughly equivalent to su -)
sudo -l               # list what commands you're permitted to run
```
**Key differences from `su`:**
| | `su` | `sudo` |
|---|---|---|
| Password required | Root's password | **Your own** password |
| Needs a root password set | Yes | No |
| Grants a full shell by default | Yes | No — runs a single command unless `-i` is used |
| Configurability | All-or-nothing access | Admin can restrict to specific commands per user via `/etc/sudoers` |

**Why `sudo` won: security philosophy.** Giving everyone the root password (the `su` model) tempts people to just stay logged in as root permanently — which means any malware they run also gets full root power. `sudo` grants privileges *only for the specific moment needed*, authenticated with the user's own credentials, and every use is logged — a much smaller attack surface. This is why Ubuntu and most modern distros disable root's password entirely and route everything through `sudo`.

---

## `chown` / `chgrp` — Changing Ownership
Requires superuser privileges.

```bash
chown bob file          # change owner to bob
chown bob:users file     # change owner to bob AND group to users
chown :admins file        # change group only, owner unchanged
chown bob: file            # change owner to bob, group to bob's own login group
```

`chgrp` is an older, more limited command that only changes group ownership (chown can do everything chgrp does, plus more).

---

## 🔧 Full Worked Example: Setting Up a Shared Directory
This ties SGID, umask, chown, and chmod together in one realistic scenario — worth understanding end-to-end since it's the kind of task you'll actually be asked to do.

**Goal:** `janet` and `tony` need a shared music directory where either of them can create files/folders that the other can also read and write.

```bash
# 1. Create a group and add both users to it
sudo groupadd music
sudo usermod -a -G music janet
sudo usermod -a -G music tony

# 2. Create the shared directory
sudo mkdir /usr/local/share/Music
# → currently: drwxr-xr-x root root (nobody but root can write)

# 3. Change group ownership to the new group
sudo chown :music /usr/local/share/Music

# 4. Set permissions AND enable SGID in one step (2775 = SGID + rwxrwxr-x)
sudo chmod 2775 /usr/local/share/Music
# → now: drwxrwsr-x root music

# 5. Fix umask so group members can write into each other's subdirectories
umask 0002    # instead of the stricter default (often 0022)
```

**Why step 5 matters:** even with SGID ensuring new files inherit the `music` group, the *default* umask might still strip group-write permission from new files — meaning janet couldn't edit a subdirectory tony created, even though they're in the same group. Lowering the umask to `0002` (instead of `0022`) ensures group members keep write access on each other's new files/folders.

---

## `passwd` — Changing Passwords
```bash
passwd           # change your own password
passwd username    # (superuser only) change another user's password
```
`passwd` actively rejects weak passwords — too short, too similar to the old one, or based on a dictionary word.

---

## 🔐 Why This Chapter Is Central to Security Work
- **`find / -perm -4000 2>/dev/null`** — enumerate all SUID binaries system-wide; a classic first step in privilege escalation hunting
- Understanding that **delete permission comes from the directory, not the file** explains a huge class of real misconfigurations
- SGID on directories vs. regular umask behavior is a common source of "why can't my teammate edit this file" bugs in real shared environments
- The `su` vs `sudo` philosophy (why root's password is disabled by default) is core to understanding modern Linux hardening
- `/etc/passwd`, `/etc/group`, `/etc/shadow` are exactly the files you'll be examining in any real investigation or CTF involving user enumeration

---

## ⚠️ Intentionally Left Out (not needed right now)
- GUI permission dialogs (GNOME Files / KDE Dolphin properties panels)
- Deep octal/hex/binary number theory beyond what's needed to read chmod values
- `shadow-utils` suite commands beyond `passwd` (`useradd`, `userdel`, `groupmod`, `lastlog`) — good to know they exist, not needed yet
- Full `/etc/sudoers` syntax and configuration — that's an admin-side deep dive for later

---

## 🎯 What You Should Be Able to Recall After Today
1. **uid/gid** come from `/etc/passwd` and `/etc/group`; `id` shows your own identity
2. Reading `ls -l`: file type character, then 3×3 permission blocks for owner/group/other
3. **`r`, `w`, `x` mean different things on directories than on files** — especially: directory `w`+`x` controls whether files inside can be created/deleted/renamed, regardless of the file's own permissions
4. Octal shortcuts: `7`=rwx, `6`=rw-, `5`=r-x, `4`=r--, `0`=---
5. `chmod` — octal (`chmod 644 file`) vs symbolic (`chmod u+x,go=rx file`) notation
6. `umask` subtracts permissions from the default at file-creation time — a `1` bit in the mask removes that permission
7. **SUID (4000)** = program runs as its owner (huge privilege-escalation relevance)
8. **SGID (2000)** on a directory = new files inherit the directory's group automatically
9. **Sticky bit (1000)** on a directory = only the file's owner (or dir owner/root) can delete/rename it — this is what protects `/tmp`
10. `su` needs root's password (usually disabled on modern distros); `sudo` needs *your own* password and is the modern standard
11. `chown user:group file` changes ownership; requires superuser privileges
12. The full shared-directory workflow: create group → add members → `chown :group` → `chmod 2775` (SGID) → adjust `umask`