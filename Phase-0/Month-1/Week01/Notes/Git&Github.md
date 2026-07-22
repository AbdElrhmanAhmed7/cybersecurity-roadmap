# Day 4 - W01 (26/06) - Git & GitHub

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Version Control, Git Commands, Branching, Merging, Stashing

---

## 1. What is Git?

**Distributed Version Control System.** Tracks what changed, when, and where in your files.

**GitHub:** Cloud server to store, share, and collaborate on repositories.

**Repository:** Place where all versions and their history are stored.

---

## 2. Git Architecture: Local vs Remote

### Local (3 Stages)

| Stage | Description |
|-------|-------------|
| **Working Directory** | Folder where you edit files |
| **Staged** | Files marked and prepared for next commit |
| **Commit** | Saved snapshot in local repo |

### Remote
- Push local files to cloud (GitHub)
- Share, access from anywhere, collaborate

---

## 3. Essential Commands

### Repository Setup
```bash
git clone <url>          # Download remote repo
git init                 # Initialize new local repo
```

### Daily Workflow
```bash
git status               # What's changed?
git add -A               # Stage all changes
git add .                # Stage current dir only
git add *                # Stage visible files (no deletions)
git commit -m "msg"      # Save staged changes
git push origin <branch> # Upload to remote
git pull                 # Download and merge remote changes
```

### Undoing Changes
```bash
git reset                # Unstage all (keep changes)
git reset HEAD~          # Roll back 1 commit (keep files)
git reset --hard         # Roll back + discard all changes

git restore <file>       # Discard uncommitted changes
git restore --staged <f> # Unstage file
```

### Removing Files
```bash
git rm <file>            # Remove and stage
git rm -f <file>         # Force remove (even modified)
git rm --cached <file>   # Remove from staging only
git rm -r <folder>       # Remove folder recursively
```

### History & Comparison
```bash
git log                  # Full commit history
git log --oneline        # Compact history
git diff                 # Show changes between states
```

---

## 4. Branching

```bash
git branch <name>        # Create new branch
git checkout <name>      # Switch to branch
git checkout <commit>    # Switch to specific commit
git merge <branch> -m "msg"  # Merge branch into current
```

### Merge Conflict
Happens when branches modify the same line. Git can't auto-decide.

**Fix:** Manually edit file, choose which changes to keep, delete conflict markers.

---

## 5. Stashing

```bash
git stash                # Save uncommitted changes temporarily
git stash pop            # Restore and remove from stash
git stash apply          # Restore but keep in stash (safer)
```

---

## 6. Reset vs Revert

| Command | Effect | Use When |
|---------|--------|----------|
| `git reset` | Rewrites history (moves branch pointer) | Local fixes, never pushed |
| `git revert` | Creates new commit with inverse changes | Undo pushed commits safely |

```bash
git revert <commit-id>   # Safe undo — creates new commit
```

---

## 7. Rebase

```bash
git rebase <branch>      # Reapply current branch commits on top of <branch>
```

**Result:** Clean, linear history (no merge commits). Rewrites commit history.

---

## 8. Fetch vs Pull

| Command | Does |
|---------|------|
| `git fetch` | Download remote changes without merging |
| `git pull` | Download + merge into current branch (`fetch` + `merge`) |

---

## 9. Quick Cheat Sheet

```bash
# Setup
git clone <url>
git init

# Daily
git status
git add -A
git commit -m "msg"
git push origin main
git pull

# Branching
git branch feat-x
git checkout feat-x
git merge feat-x

# Undo
git reset HEAD~          # soft undo
git reset --hard         # hard undo
git revert <commit>      # safe undo (pushed)
git restore <file>       # discard changes
git restore --staged <f> # unstage

# Stash
git stash
git stash pop
git stash apply

# History
git log --oneline
git diff
```

---

✅ **Status:** Git & GitHub fundamentals mastered  
🚀 **Next:** Python basics (Variables, Types, Control Flow)
