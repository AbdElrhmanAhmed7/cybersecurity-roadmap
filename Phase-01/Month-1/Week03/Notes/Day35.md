# Summary Ch 8 — Advanced Keyboard Tricks
> The book itself calls this chapter **optional** ("consider them optional and potentially helpful"). It's about typing speed, not new concepts — so this summary is intentionally short. Pick a few habits, don't try to memorize the whole table.

---

## The One Thing Actually Worth Making a Habit: Tab Completion
```bash
ls D<Tab>
```
- If only one match exists → auto-completes instantly
- If multiple matches exist → nothing happens on the first press; **press Tab again** to see the list of possibilities
- Works for filenames, and also for variables (`$`), usernames (`~`), and commands (first word on the line)

**This alone will save you more time than everything else in this chapter combined.** Use it constantly, especially with long filenames.

---

## Worth Knowing: History Search
```bash
Ctrl-r
```
Starts a **reverse incremental search** — type any part of a command you used before, and bash finds it live as you type.
```
(reverse-i-search)`ssh': ssh user@server
```
- Press **Enter** → runs it immediately
- Press **Ctrl-j** → copies it to your prompt so you can edit it first
- Press **Ctrl-r** again → jump to the next older match
- Press **Ctrl-c** or **Ctrl-g** → cancel the search

**Why this matters more than memorizing commands:** instead of retyping a long command (like a complex `find` or `grep` pipeline you built earlier), just search for a fragment of it and reuse it.

```bash
history | grep /usr/bin     # alternative: search history as plain text
```

---

## Handy But Optional: A Few Cursor/Edit Shortcuts
Only worth learning if you actually type long commands often. Don't force-memorize the full table — pick what's useful to you.

| Key | Action |
|---|---|
| `Ctrl-a` | Jump to beginning of the line |
| `Ctrl-e` | Jump to end of the line |
| `Ctrl-l` | Clear screen (same as typing `clear`) |
| `Ctrl-u` | Delete from cursor to beginning of line |
| `Ctrl-k` | Delete from cursor to end of line |

---

## ⚠️ Intentionally Left Out (genuinely not worth your time right now)
- Full cursor movement table (Alt-f, Alt-b, Ctrl-f, Ctrl-b) — the arrow keys already do this
- Kill-ring/yank details beyond `Ctrl-u`/`Ctrl-k` (Alt-d, Alt-Backspace, Ctrl-y) — diminishing returns
- Text case conversion (Alt-l, Alt-u) — rarely used
- The "Meta key" history/terminal trivia
- `!!`, `!number`, `!string` history expansion syntax — error-prone and easy to misfire; `Ctrl-r` does the same job more safely
- Programmable completion internals
- The `script` command (session recording) — situational, look it up if you ever specifically need it

---

## 🎯 What You Should Be Able to Recall After Today
1. **Tab** completes filenames/commands — press twice if nothing happens, to see the options
2. **Ctrl-r** searches your command history live — faster and safer than retyping or using `!` history expansion
3. Everything else in this chapter is optional convenience — revisit only if curious, not required for the roadmap