# Python Regex Cheat Sheet (Day 23+)

Personal review notes from *Automate the Boring Stuff with Python* (3rd Edition, Ch. 9) and the HackerRank Regex practice track. Every entry below has a one-line reminder plus a runnable example — skim the table of contents to jump straight to whatever you forgot.

All examples assume `import re` has already been run, unless the block shows its own import.

## Table of Contents
1. [Setup](#1-setup)
2. [Matching a Specific String](#2-matching-a-specific-string)
3. [Escaping Special Characters](#3-escaping-special-characters)
4. [Matching Start and End](#4-matching-start-and-end)
5. [Matching Anything But a Newline](#5-matching-anything-but-a-newline)
6. [Matching Digits and Non-Digits](#6-matching-digits-and-non-digits)
7. [Matching Whitespace and Non-Whitespace](#7-matching-whitespace-and-non-whitespace)
8. [Matching Word and Non-Word Characters](#8-matching-word-and-non-word-characters)
9. [Matching Specific Characters](#9-matching-specific-characters)
10. [Excluding Specific Characters](#10-excluding-specific-characters)
11. [Matching Character Ranges](#11-matching-character-ranges)
12. [Matching Exact Repetitions](#12-matching-exact-repetitions)
13. [Matching Range Repetitions](#13-matching-range-repetitions)
14. [Matching Zero or More](#14-matching-zero-or-more)
15. [Matching One or More](#15-matching-one-or-more)
16. [Matching an Optional Pattern](#16-matching-an-optional-pattern)
17. [Greedy vs Non-Greedy Matching](#17-greedy-vs-non-greedy-matching)
18. [Matching Ending Items](#18-matching-ending-items)
19. [Matching Word Boundaries](#19-matching-word-boundaries)
20. [Capturing and Non-Capturing Groups](#20-capturing-and-non-capturing-groups)
21. [Alternative Matching](#21-alternative-matching)
22. [Matching Same Text Again](#22-matching-same-text-again)
23. [Backreferences to Failed Groups](#23-backreferences-to-failed-groups)
24. [Lookahead](#24-lookahead)
25. [Lookbehind](#25-lookbehind)
26. [Pattern Object Methods](#26-pattern-object-methods)
27. [Useful Flags](#27-useful-flags)
28. [Putting It Together](#28-putting-it-together)
29. [Bonus: Humre](#29-bonus-humre)
30. [Quick Reference Table](#30-quick-reference-table)

---

## 1. Setup
Four steps to use any regex in Python.

```python
import re                                    # 1. import the module
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')   # 2. compile the regex string
match = pattern.search('Call 415-555-1234')  # 3. search a string
match.group()                                # 4. read the matched text
# '415-555-1234'
```
Always use a raw string (`r'...'`) so backslashes aren't treated as Python escape codes.

## 2. Matching a Specific String
Plain characters with no special symbols just match themselves, literally, anywhere in the text.

```python
re.search(r'cat', 'concatenate').group()
# 'cat'
```

## 3. Escaping Special Characters
These characters are regex metacharacters: `. ^ $ * + ? { } [ ] \ ( ) |`. To match one of them literally, put a backslash in front of it.

```python
re.search(r'\(\d{3}\) \d{3}-\d{4}', '(212) 555-9876').group()
# '(212) 555-9876'   -- \( and \) match literal parentheses
```
A stray unescaped `(` or `)` is the most common cause of a `missing ), unterminated subpattern` error.

## 4. Matching Start and End
`^` anchors the match to the start of the string; `$` anchors it to the end. Used together, they force the *whole* string to match.

```python
re.search(r'^Hello', 'Hello world')          # matches
re.search(r'world$', 'Hello world')          # matches
re.search(r'^\d+$', '12345')                 # matches (all digits, start to end)
re.search(r'^\d+$', '123 45') == None        # True -- the space breaks it
```

## 5. Matching Anything But a Newline
`.` (dot) matches any single character except `\n`.

```python
re.findall(r'.at', 'cat hat sat flat')
# ['cat', 'hat', 'sat', 'lat']   -- "flat" only contributes "lat"; dot is ONE character
```

## 6. Matching Digits and Non-Digits
`\d` = a digit (0-9). `\D` = anything that is **not** a digit.

```python
re.findall(r'\d', 'Room 42B')   # ['4', '2']
re.findall(r'\D', 'Room 42B')   # ['R', 'o', 'o', 'm', ' ', 'B']
```

## 7. Matching Whitespace and Non-Whitespace
`\s` = space, tab, or newline. `\S` = anything that isn't whitespace.

```python
re.split(r'\s', 'one two  three')
# ['one', 'two', '', 'three']   -- the double space creates an empty split
```

## 8. Matching Word and Non-Word Characters
`\w` = letters, digits, or underscore. `\W` = anything else (punctuation, spaces, symbols).

```python
re.findall(r'\w+', "Hi there, it's Al!")
# ['Hi', 'there', 'it', 's', 'Al']   -- the apostrophe splits "it's" into "it" and "s"
```

## 9. Matching Specific Characters
Square brackets `[...]` define a character class: match **any one** character from the set.

```python
re.findall(r'[aeiou]', 'HELLO world')
# ['o']   -- only lowercase vowels match here; add re.IGNORECASE to catch both cases
```

## 10. Excluding Specific Characters
A caret `^` right after the opening bracket negates the class: match any character **not** listed.

```python
re.findall(r'[^aeiou ]', 'hello world')
# ['h', 'l', 'l', 'w', 'r', 'l', 'd']
```

## 11. Matching Character Ranges
A hyphen inside `[...]` defines a range, e.g. `a-z`, `A-Z`, `0-9`.

```python
re.findall(r'[a-zA-Z0-9]', 'Room #42B!')
# ['R', 'o', 'o', 'm', '4', '2', 'B']
```

> **Watch out:** `[A-Za-z]` and `\w` only cover plain ASCII letters. Accented letters, apostrophes, and hyphens in real names (Sinéad, O'Connor, Jean-Paul) will slip past a regex that assumes "letters only" — see Patrick McKenzie's essay *"Falsehoods Programmers Believe About Names"* for more of these.

## 12. Matching Exact Repetitions
`{n}` after a qualifier means "match exactly n times."

```python
re.findall(r'\d{3}', '123456')
# ['123', '456']
```

## 13. Matching Range Repetitions
`{n,m}` means "match between n and m times" (inclusive), greedily.

```python
re.findall(r'\d{2,4}', '1 22 333 4444 55555')
# ['22', '333', '4444', '5555']
# -- lone '1' is too short; '55555' gives up its max (4) and leaves one '5' unmatched
```
`{n,}` means "n or more"; `{,m}` means "up to m."

## 14. Matching Zero or More
`*` means the preceding qualifier can appear any number of times, including not at all.

```python
re.search(r'ha*', 'h').group()        # 'h'
re.search(r'ha*', 'haaaa').group()    # 'haaaa'
```

## 15. Matching One or More
`+` is like `*` but requires **at least one** occurrence.

```python
re.findall(r'ha+', 'h ha haa haaa')
# ['ha', 'haa', 'haaa']   -- the bare 'h' doesn't count, it needs at least one 'a'
```

## 16. Matching an Optional Pattern
`?` means "zero or one" — the preceding qualifier (or group) is optional.

```python
re.findall(r'colou?r', 'color colour')
# ['color', 'colour']
```
Wrap several characters in a group before the `?` to make the whole group optional: `(\d{3}-)?\d{3}-\d{4}` matches a phone number with or without an area code.

## 17. Greedy vs Non-Greedy Matching
By default, quantifiers are **greedy**: they match as much text as possible. Add a `?` after the quantifier to make it **lazy** (match as little as possible).

```python
re.search(r'<.*>', '<a><b>').group()     # '<a><b>'   (greedy)
re.search(r'<.*?>', '<a><b>').group()    # '<a>'      (lazy)
```

## 18. Matching Ending Items
A practical use of `$`: pulling out only the last item in a string.

```python
re.findall(r'\w+$', 'My favorite fruits: apple, banana, cherry')
# ['cherry']
```
By default `^`/`$` only apply to the whole string. Pass `re.MULTILINE` to make them match the start/end of **every line** instead:

```python
text = 'apple,banana\ncherry,date'
re.findall(r'\w+$', text, re.MULTILINE)
# ['banana', 'date']
```

## 19. Matching Word Boundaries
`\b` matches the invisible edge between a word character and a non-word character (or the start/end of the string). `\B` matches anywhere that is **not** a word boundary.

```python
re.findall(r'\bcat\b', 'cat catalog concatenate')
# ['cat']            -- only the standalone word matches

re.findall(r'\Bcat\B', 'concatenate')
# ['cat']            -- \B finds "cat" sitting in the middle of a word
```

## 20. Capturing and Non-Capturing Groups
`(...)` captures whatever it matches so you can retrieve it later. `(?:...)` groups characters (for a quantifier, for example) without creating a numbered group.

```python
m = re.search(r'(\d{3})-(\d{4})', '555-1234')
m.group(1)      # '555'
m.group(2)      # '1234'
m.groups()      # ('555', '1234')

re.findall(r'(?:ab)+c', 'ababc')
# ['ababc']      -- matched as one block; no separate captured group
```

## 21. Alternative Matching
The pipe `|` matches one of several options.

```python
re.search(r'cat|dog', 'I have a dog').group()
# 'dog'
```
Put alternatives inside a group to share a common prefix:

```python
re.search(r'cat(nap|fish|walk)', 'I went for a catwalk').group()
# 'catwalk'
```

## 22. Matching Same Text Again
A backreference (`\1`, `\2`, ...) matches whatever text an earlier group *already* matched — not the group's pattern again, the literal text.

```python
re.search(r'(\w+) \1', 'hello hello world').group()
# 'hello hello'
```

## 23. Backreferences to Failed Groups
If an optional group never participates in a match, a backreference to it can never succeed either — there's nothing to compare against.

```python
re.search(r'(a)?b\1', 'b') == None
# True -- group 1 never matched anything, so \1 can't match anything

re.search(r'(a)?b\1?', 'b').group()
# 'b' -- making the backreference itself optional (\1?) fixes it
```

## 24. Lookahead
Lookaheads check what comes **next** without including it in the match.
- Positive `(?=...)` — must be followed by the pattern.
- Negative `(?!...)` — must **not** be followed by the pattern.

```python
re.findall(r'\d+(?=px)', '10px 20em 30px')
# ['10', '30']    -- only numbers immediately before "px"

re.findall(r'foo(?!bar)', 'foobar foobaz')
# ['foo']         -- only the "foo" that ISN'T followed by "bar"
```

## 25. Lookbehind
Lookbehinds check what comes **before**, also without consuming it. Python requires lookbehind patterns to be a fixed length.
- Positive `(?<=...)` — must be preceded by the pattern.
- Negative `(?<!...)` — must **not** be preceded by the pattern.

```python
re.findall(r'(?<=\$)\d+', 'Price: $50 and 30 dollars')
# ['50']          -- only the number that follows a $ sign

re.findall(r'(?<!wild)cat', 'housecat wildcat')
# ['cat']         -- only the "cat" that ISN'T preceded by "wild"
```

## 26. Pattern Object Methods
The three methods you'll use constantly, side by side:

```python
pattern = re.compile(r'\d+')
text = 'I have 5 apples and 12 oranges'

pattern.search(text).group()   # '5'              -- first match only
pattern.findall(text)          # ['5', '12']       -- every match
pattern.sub('N', text)         # 'I have N apples and N oranges'
```
`sub()` can also reuse captured groups in the replacement with `\1`, `\2`, etc.:

```python
re.sub(r'Agent (\w)\w*', r'\1***', 'Agent Smith met Agent Jones.')
# 'S*** met J***.'
```

## 27. Useful Flags
Pass these as the second argument to `re.compile()` (or `search`/`findall`/etc.). Combine multiple flags with `|`.

```python
re.search(r'python', 'I love PYTHON', re.IGNORECASE).group()
# 'PYTHON'   -- ignores letter case

re.search(r'a.b', 'a\nb', re.DOTALL).group()
# 'a\nb'     -- makes . also match newlines

re.compile(r'''
    \d{3}    # area code
    -        # dash
    \d{4}    # number
''', re.VERBOSE)
# lets you spread a regex over multiple lines and add comments

re.compile(r'\d{3}', re.IGNORECASE | re.DOTALL)
# combining two flags at once with the pipe operator
```
`re.MULTILINE` (see [Matching Ending Items](#18-matching-ending-items)) makes `^`/`$` apply per line instead of to the whole string.

## 28. Putting It Together
A trimmed-down version of the phone number + email extractor project, combining groups, alternation, character classes, and quantifiers:

```python
import re

phone_pattern = re.compile(r'''
    (\d{3}|\(\d{3}\))?    # area code, optional, with or without parens
    [\s.-]?               # separator
    \d{3}                 # first three digits
    [\s.-]                # separator
    \d{4}                 # last four digits
''', re.VERBOSE)

email_pattern = re.compile(r'''
    [\w.%+-]+             # username
    @
    [\w.-]+                # domain name
    \.[a-zA-Z]{2,4}        # .com / .net / etc.
''', re.VERBOSE)

text = 'Reach me at 415-555-0199 or hi@example.com'
phone_pattern.findall(text)   # finds the phone number
email_pattern.findall(text)   # finds the email address
```

## 29. Bonus: Humre
Humre is a third-party module that builds regex strings out of readable Python function calls instead of raw symbols.

```python
from humre import *
digits_pattern = exactly(3, DIGIT) + '-' + exactly(4, DIGIT)
# same regex as r'\d{3}-\d{4}', just spelled out in plain English
```
Useful functions: `group()`, `optional()`, `either()`, `exactly()`, `between()`, `at_least()`, `zero_or_more()`, `one_or_more()`, `chars()`, `nonchars()`. Humre doesn't replace `re` — it just builds the regex string you pass to `re.compile()`.

## 30. Quick Reference Table

| Symbol | Meaning |
|---|---|
| `.` | any character except newline |
| `\d` / `\D` | digit / non-digit |
| `\w` / `\W` | word character / non-word character |
| `\s` / `\S` | whitespace / non-whitespace |
| `^` | start of string (or line, with `re.MULTILINE`) |
| `$` | end of string (or line, with `re.MULTILINE`) |
| `\b` / `\B` | word boundary / not a word boundary |
| `[...]` | character class — match one of these |
| `[^...]` | negative character class — match none of these |
| `(...)` | capturing group |
| `(?:...)` | non-capturing group |
| `|` | alternation (OR) |
| `?` | 0 or 1 of the preceding item |
| `*` | 0 or more |
| `+` | 1 or more |
| `{n}` | exactly n |
| `{n,m}` | between n and m |
| `{n,}` / `{,m}` | n or more / up to m |
| `*?`, `+?`, `{n,m}?` | lazy (non-greedy) versions |
| `\1`, `\2`, ... | backreference to group 1, 2, ... |
| `(?=...)` | positive lookahead |
| `(?!...)` | negative lookahead |
| `(?<=...)` | positive lookbehind |
| `(?<!...)` | negative lookbehind |
