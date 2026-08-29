# Summary Ch 14 — Package Management
> This chapter explains how Linux distributes, installs, updates, and removes software through package managers and repositories. Directly relevant to security work: understanding package provenance, repository trust, and dependency resolution is essential for maintaining a secure and auditable system.

---

## How Package Management Works — The Big Picture

### The Problem It Solves
In the early days of Linux, installing software meant downloading **source code** and compiling it manually. Today, **package management** automates this: pre-compiled software is distributed as **packages** through central **repositories**, and tools handle installation, updates, and dependency resolution for you.

### The Package File
The basic unit of software distribution. A package file is a compressed archive containing:
- The actual program binaries and data files
- **Metadata**: name, version, description, maintainer info
- **Pre/post-installation scripts**: configuration tasks run before/after installation
- **Dependency information**: what other packages this package needs to function

### Repositories
Centralized storage locations (servers) maintained by distribution vendors or third parties. Your system subscribes to a list of repositories and queries them when you request software.

| Repository Type | Purpose |
|---|---|
| **Main/Stable** | Core, well-tested packages for general use |
| **Testing** | Newer packages for bug hunting before stable release |
| **Development** | Work-in-progress packages for the next major release |
| **Third-party** | Software that can't be included for legal reasons (patents, DRM) |

### Dependencies
Programs rarely run alone. They rely on **shared libraries** and other components. A package that requires another package is said to have a **dependency**. Modern package managers **automatically resolve and install dependencies**.

---

## Packaging System Families

Most Linux distributions fall into one of two camps:

| Packaging System | File Extension | Example Distributions |
|---|---|---|
| **Debian Style** | `.deb` | Debian, Ubuntu, Linux Mint, Raspberry Pi OS, Parrot OS |
| **Red Hat Style** | `.rpm` | Fedora, CentOS, Red Hat Enterprise Linux, OpenSUSE |
| **Exceptions** | Custom | Gentoo, Slackware, Arch (use their own systems) |

> ⚠️ **A `.deb` package is NOT compatible with an `.rpm` system and vice versa.** They are built for different packaging ecosystems.

---

## High-Level vs Low-Level Package Tools

Package management systems provide two layers of tools:

| Level | Purpose | Debian | Red Hat |
|---|---|---|---|
| **Low-level** | Install/remove package files directly; no dependency resolution | `dpkg` | `rpm` |
| **High-level** | Search repositories, resolve dependencies, manage the full lifecycle | `apt`, `apt-get`, `aptitude` | `dnf`, `yum` |

### Why the distinction matters
- **Low-level tools** (`dpkg`, `rpm`) work with actual package files you downloaded manually. They install what's in the file — if dependencies are missing, they fail with an error.
- **High-level tools** (`apt`, `dnf`) talk to repositories. You give them a package *name*, they find it, download it, and **automatically fetch all dependencies**.

---

## Common Package Management Tasks

> All install/remove/upgrade operations require **superuser privileges** (`sudo`).
> 
> On Debian systems, run `apt update` before operations to sync your local package database with the repositories. `dnf` does this automatically.

### Finding a Package

| Style | Command |
|---|---|
| Debian | `apt update; apt search search_string` |
| Red Hat | `dnf search search_string` |

### Installing from a Repository

| Style | Command |
|---|---|
| Debian | `apt update; apt install package_name` |
| Red Hat | `dnf install package_name` |

**Example:**
```bash
sudo apt update && sudo apt install emacs
sudo dnf install emacs
```

### Installing from a Downloaded Package File

| Style | Command | Notes |
|---|---|---|
| Debian | `dpkg -i package_file.deb` | No dependency resolution |
| Red Hat | `rpm -i package_file.rpm` | No dependency resolution |

> ⚠️ If dependencies are missing, the installation will fail. To fix broken dependencies after a failed `dpkg` install, Debian users can run: `sudo apt --fix-broken install`

### Removing a Package

| Style | Command | Effect |
|---|---|---|
| Debian | `apt remove package_name` | Removes the package, keeps config files |
| Debian | `apt purge package_name` | Removes the package **and** config files |
| Red Hat | `dnf erase package_name` | Removes the package |

### Updating Packages

| Style | Command |
|---|---|
| Debian | `apt update; apt upgrade` |
| Red Hat | `dnf update` |

### Upgrading from a Package File

| Style | Command |
|---|---|
| Debian | `dpkg -i package_file.deb` (same as install) |
| Red Hat | `rpm -U package_file.rpm` |

### Listing Installed Packages

| Style | Command |
|---|---|
| Debian | `dpkg -l` |
| Red Hat | `rpm -qa` |

### Checking if a Package is Installed

| Style | Command |
|---|---|
| Debian | `dpkg -s package_name` |
| Red Hat | `rpm -q package_name` |

### Displaying Package Information

| Style | Command |
|---|---|
| Debian | `apt show package_name` |
| Red Hat | `dnf info package_name` |

### Finding Which Package Owns a File

| Style | Command |
|---|---|
| Debian | `dpkg -S /path/to/file` |
| Red Hat | `rpm -qf /path/to/file` |

**Example:**
```bash
rpm -qf /usr/bin/vim
```

---

## Distribution-Independent Package Formats

Universal formats designed to work across any Linux distribution:

| Format | Developed By | Concept |
|---|---|---|
| **Snap** | Canonical (Ubuntu) | App + dependencies bundled; distributed via Snap Store |
| **Flatpak** | Red Hat / Community | App + dependencies bundled; sandboxed |
| **AppImage** | Community | Single executable file; run without installation |

### Benefits
- **Write once, run anywhere**: Developers build one package for all distributions.
- **Sandboxing**: Some formats run in isolated containers for extra security.

### Downsides
- **Bloated size**: Each app bundles its own dependencies, consuming significant disk space.
- **Slow load times**: Large bundles take longer to start.
- **Poor system integration**: They don't use the distribution's native libraries or facilities.
- **Philosophical concern**: Primarily benefits proprietary vendors; does little to enhance the open-source community.

> 💡 **Current recommendation**: Until performance issues are resolved, prefer native `.deb` / `.rpm` packages from trusted repositories.

---

## The Linux Software Installation Myth

### Myth
> "Installing software on Linux is hard because there are too many different packaging systems."

### Reality
- For **open-source software**, a distribution maintainer usually packages it and places it in the official repository. Users enjoy **one-stop shopping** — this is the model modern app stores copied.
- **Drivers** are part of the Linux kernel itself. There is no "driver disk" concept. Either the kernel supports the device, or it doesn't.

### If a device isn't supported, it's usually one of three reasons:
1. **Too new**: The hardware vendor doesn't support Linux development; the community needs time to write a driver.
2. **Too exotic**: The distribution's kernel build didn't include that specific driver.
3. **Vendor is hiding something**: No source code or technical documentation released. **Avoid such products.**

---

## 🔐 Why This Chapter Matters for Security Work

- **Repository trust is everything**: Installing from official repositories means the packages are signed, verified, and maintained by the distribution. Installing random `.deb` / `.rpm` files from the internet bypasses this trust model.
- **Dependency resolution prevents "dependency hell"**: Manually resolving dependencies (using low-level tools) increases the risk of installing conflicting or vulnerable library versions.
- **Third-party repositories**: Adding untrusted repositories to your sources list can expose you to supply-chain attacks. Only add repositories you explicitly trust and need.
- **Universal formats (Snap/Flatpak/AppImage)**: While convenient, their sandboxing isn't perfect, and they bundle potentially outdated libraries that won't receive distribution security updates.
- **Package verification**: High-level tools verify package signatures from repositories. Low-level manual installs (`dpkg -i`, `rpm -i`) do not automatically verify authenticity unless you manually check GPG keys.
- **System updates**: Regularly running `apt upgrade` or `dnf update` is a fundamental security hygiene practice — it patches vulnerabilities in installed software.

---

## ⚠️ Intentionally Left Out (not needed right now)
- Building packages from source code (covered in Chapter 23)
- Full `dpkg` and `rpm` option reference — `man dpkg` and `man rpm` have exhaustive lists
- GUI package managers (Synaptic, GNOME Software, etc.) — the chapter focuses on CLI tools because they are more powerful and scriptable
- Deep internals of repository metadata formats (Packages.gz, repodata, etc.)
- Creating your own packages — outside the scope of an introductory chapter

---

## 🎯 What You Should Be Able to Recall After Today
1. **Package management** = the system for installing, updating, and removing software via pre-compiled packages from repositories.
2. The two major packaging families: **Debian (`.deb`)** and **Red Hat (`.rpm`)** — they are not cross-compatible.
3. **Low-level tools** (`dpkg`, `rpm`) handle package files directly but **do NOT resolve dependencies**.
4. **High-level tools** (`apt`, `dnf`) search repositories, download packages, and **automatically resolve dependencies**.
5. **`apt update`** syncs the local package database with repositories (required explicitly on Debian; `dnf` does it automatically).
6. Key commands: `install`, `remove`/`erase`, `upgrade`/`update`, `search`, `show`/`info`, `list` (`dpkg -l` / `rpm -qa`).
7. **Installing from a file**: `dpkg -i file.deb` or `rpm -i file.rpm` — beware of missing dependencies.
8. **Finding file ownership**: `dpkg -S file` or `rpm -qf file` tells you which package installed a specific file.
9. **Universal formats** (Snap, Flatpak, AppImage) bundle apps with dependencies but have trade-offs in size, speed, and integration.
10. **Linux driver model**: Drivers are in the kernel; there are no "driver disks." If hardware isn't supported, it's usually too new, too exotic, or the vendor is withholding documentation.
