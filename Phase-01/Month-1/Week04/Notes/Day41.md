# Summary Ch 16 — Networking
> Practical toolkit for examining, monitoring, and moving data across a network from the command line — plus secure remote access via SSH. Directly relevant to security work: these are the exact tools used for reconnaissance, remote administration, and secure file transfer.

---

## Prerequisite Concepts (assumed background)
The chapter assumes familiarity with: **IP address**, **host/domain name**, **URI**. If any of these feel shaky, worth a quick look — everything else in the chapter builds on them.

---

## Examining and Monitoring a Network

### `ping` — "Is this host even reachable?"
Sends an **ICMP ECHO_REQUEST** packet; a responding host confirms basic connectivity.
```bash
ping linuxcommand.org
```
Runs continuously (once per second by default) until interrupted with **Ctrl-c**, then prints summary statistics (packets sent/received, % loss, round-trip time).

⚠️ **Security-relevant caveat:** many hosts and firewalls are deliberately configured to **ignore or block ICMP traffic** — often specifically to make reconnaissance harder. So a failed `ping` doesn't necessarily mean a host is down; it might just mean it's configured to not respond. Don't treat "no ping response" as proof of "host unreachable."

A 0% packet loss result means the network path (cabling, routing, gateways) is generally healthy.

### `traceroute` — "What path does traffic take to get there?"
```bash
traceroute slashdot.org
```
Lists every router ("hop") the traffic passes through on the way to the destination, with round-trip time samples for each. Hops that don't respond (due to config, congestion, or firewalls) show as `* * *`.

**Practical use:** diagnosing where a connection is slow or failing, and — from a security angle — mapping the network path/infrastructure a target sits behind.

### `ip` — the modern all-purpose network configuration tool
Replaces the older, now-deprecated `ifconfig`. Syntax:
```bash
ip [-options] object [command]
```
Object and command names can be shortened to any unambiguous prefix, and `show` is the default command — so `ip address show` can be shortened to just `ip a`, and `ip route show` to `ip r`.

**Checking interfaces:**
```bash
ip address show    # or: ip a
```
What to actually look for in the output:
- **`state UP`** on the first line → the interface is enabled
- **A valid IP in the `inet` field** → confirms the interface has an address (and, for DHCP setups, that DHCP is working)

**Checking the routing table:**
```bash
ip route show    # or: ip r
```
- A line starting with **`default`** = the default gateway — where traffic goes if no more specific route matches
- Addresses ending in `.0` describe entire **networks**, not individual hosts
- `169.254.0.0/16` showing up is **APIPA** (Automatic Private IP Addressing) — a self-assigned fallback address used when no DHCP server is available; seeing this on an interface that should have a normal LAN address is itself a diagnostic clue that DHCP failed

---

## Transporting Files Over a Network

### `ftp` — the classic, insecure file transfer client
```bash
ftp fileserver
```
🚨 **Critical security fact:** plain FTP transmits **usernames and passwords in cleartext** — anyone sniffing the network traffic can read them. This is exactly why almost all public FTP today is **anonymous** (login as `anonymous`, any/no real password) rather than using real credentials over FTP.

Common interactive `ftp` session commands:
| Command | Meaning |
|---|---|
| `cd path` | change directory **on the remote server** |
| `lcd path` | change directory **on your local machine** |
| `ls` | list remote directory |
| `get filename` | download a file |
| `bye` / `quit` / `exit` | end the session |

`lftp` is mentioned as a more modern, feature-rich alternative (multi-protocol, tab completion, auto-retry) — worth knowing the name exists, not essential to memorize its usage yet.

### `curl` — transfer data from/to a URL
```bash
curl https://linuxcommand.org
```
Outputs the page directly to stdout by default. Supports a huge range of protocols (HTTP, HTTPS, FTP, SFTP, SMB, and more) — this versatility is why `curl` shows up constantly in scripting and security tooling, not just "downloading a webpage."

| Option | Meaning |
|---|---|
| `-o file` | save output to a named file |
| `-O` | save using the remote file's own name |
| `-s` | silent — suppress progress meter and errors |
| `-v` | verbose — show detailed request/response info |

### `wget` — non-interactive downloader
```bash
wget http://linuxcommand.org/index.php
```
Good for straightforward downloads, including recursive site downloads and resuming partial/interrupted downloads. Simpler and more "fire and forget" than `curl` for basic file grabbing.

---

## Secure Communication with Remote Hosts

### Why SSH exists — the problem it solves
Older remote-login tools (`rlogin`, `telnet`) — like plain `ftp` — send **everything in cleartext**, including login credentials. **SSH (Secure Shell)** was built to fix two specific problems:
1. **Authentication** — confirms the remote host is really who it claims to be (prevents man-in-the-middle attacks)
2. **Encryption** — encrypts all traffic between local and remote systems

Architecture: an **SSH server** listens on the remote host (default **port 22**); an **SSH client** (the `ssh` command) connects to it from your local machine.

### Basic Usage
```bash
ssh remote-sys                # connect as your current local username
ssh bob@remote-sys              # connect as a different username
```

### First-Time Connection: the Host Authenticity Prompt
```
The authenticity of host 'remote-sys (192.168.1.4)' can't be established.
RSA key fingerprint is 41:ed:7a:df:...
Are you sure you want to continue connecting (yes/no)?
```
This appears because your machine has never seen this host's key before. Accepting ("yes") adds it to `~/.ssh/known_hosts` for future verification.

### 🚨 The "REMOTE HOST IDENTIFICATION HAS CHANGED" Warning — read this carefully
```
WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
```
This means the key SSH remembers for this host **doesn't match** what it's presenting now. Two possible causes:
1. **A legitimate change** — the remote system was reinstalled, its SSH server reconfigured, etc. (the far more common case)
2. **An actual man-in-the-middle attack** in progress (rare, but this warning exists specifically to catch it)

**The correct response is never to blindly dismiss it** — always verify with the remote system's administrator before proceeding. Once confirmed benign, the fix is:
```bash
ssh-keygen -f "/home/me/.ssh/known_hosts" -R "remote-sys"
```
(Or manually delete the specific offending line number from `~/.ssh/known_hosts`, as indicated in the warning message.)

### Running a Single Remote Command (without a full interactive session)
```bash
ssh remote-sys free                     # runs `free` on the remote host, shows result locally
ssh remote-sys 'ls *' > dirlist.txt       # remote `ls`, output saved to a LOCAL file
```
⚠️ **Why the single quotes matter here — a direct callback to Ch7 (Quoting):** without quotes, pathname expansion (`*`) would happen on your **local** machine *before* the command is even sent to the remote host — expanding against the wrong filesystem entirely. Single-quoting `'ls *'` forces the expansion to happen on the **remote** side instead, against the correct directory.

Same logic applies to redirecting the output remotely instead of locally:
```bash
ssh remote-sys 'ls * > dirlist.txt'    # redirection happens ON THE REMOTE SYSTEM
```

### SSH Tunneling (brief overview)
The SSH connection is fundamentally an **encrypted tunnel** — and that tunnel can carry more than just your typed commands. It can carry other network traffic too (the book's example: forwarding graphical X Window System output back to your local display via `ssh -X`). Good to know this capability exists; not something you need to use yet.

### `scp` — secure copy over SSH
Works like `cp`, but the source or destination can be prefixed with a remote host name:
```bash
scp remote-sys:document.txt .              # download
scp bob@remote-sys:document.txt .           # download as a different remote user
```

### `sftp` — secure, interactive alternative to `ftp`
```bash
sftp remote-sys
```
Same interactive feel as `ftp` (`ls`, `lcd`, `get`, `bye`), but tunneled through SSH — meaning it needs **only an SSH server** on the remote end, not a separate dedicated FTP server. This is a real practical advantage: any machine reachable via SSH can serve files this way, no extra service required.

---

## 🔐 Why This Chapter Matters for Security Work
- `ping`/`traceroute`/`ip` are baseline **reconnaissance and network-mapping tools** — but remember a non-response doesn't prove a host is down, just that it might be filtering ICMP
- **Cleartext protocols (`ftp`, `telnet`, `rlogin`) are exactly what you should never use for anything sensitive** — this chapter's clearest security lesson, and the direct motivation for SSH's existence
- The SSH host-key-changed warning is a **real, actionable security control** — understanding what it means (and that it's not just noise to click through) is a core defensive skill
- `ssh host 'command'` with correct quoting is a common pattern in automation/scripting for remote reconnaissance or administration — ties directly back to the Quoting rules from Ch7
- `scp`/`sftp` are the standard secure replacements any time you'd be tempted to reach for plain `ftp`

---

## ⚠️ Intentionally Left Out (not needed right now)
- `netstat` — listed in the chapter's command list up front but not actually covered in the body text provided; worth learning when you specifically need connection/socket inspection (its modern replacement, `ss`, is also worth knowing about)
- Full `traceroute` option set (`-T`, `-I`) beyond knowing they exist for bypassing blocked routing info
- `lftp`'s full feature set — know it exists as a better `ftp`, not essential to use yet
- SSH tunneling / `-X` forwarding in practical depth — conceptually noted, not something to practice yet
- PuTTY (Windows SSH client) — irrelevant if you're working natively in Linux

---

## 🎯 What You Should Be Able to Recall After Today
1. `ping` tests basic reachability via ICMP — but blocked ICMP ≠ host is down
2. `traceroute` shows the hop-by-hop path traffic takes to a destination
3. `ip address show` (`ip a`) — check interface state (`UP`) and assigned IP; `ip route show` (`ip r`) — check the routing table and default gateway
4. Seeing a `169.254.x.x` address means DHCP failed and the system fell back to APIPA
5. **Plain FTP sends credentials in cleartext — this is why anonymous FTP is the norm and why SSH-based alternatives exist**
6. `curl` and `wget` both fetch URLs from the command line; `curl` is more protocol-versatile, `wget` is simpler for straightforward/recursive downloads
7. SSH solves two problems: authenticating the remote host, and encrypting the whole session
8. The "host identification has changed" warning must always be verified with the admin before proceeding — never dismissed reflexively
9. `ssh host 'command with *'` — single-quote to force expansion to happen on the remote side, not locally (direct application of Ch7 quoting rules)
10. `scp` = secure `cp` over SSH; `sftp` = secure, interactive `ftp` over SSH — both only require an SSH server, not a dedicated FTP server
