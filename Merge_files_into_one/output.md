# 📁 تقرير تجميع الملفات
> تم إنشاؤه في: 2026-07-17 19:54:07
> المجلد الجذري: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1`

---

## 📄 الملف: `Week01\Learning\Jupiter\Day1.ipynb`
- **الامتداد**: `.ipynb`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week01\Learning\Jupiter\Day1.ipynb`

### 📓 Jupyter Notebook
**كود (Code Cells):**
```python
from pathlib import Path, PosixPath

Path(r"C:\Users\abdel\Downloads\Automate_the_Boring_Stuff_3e_onlinematerials\__MACOSX")

my_files = ['accounts.txt', 'details.csv', 'invite.docx']

for filename in my_files:
    print(Path(r'C:\Users\Al', filename))

Path("egg") / Path("ham") / "i" / "o"

import os

Path.cwd()

os.chdir(r"D:\Cypersecurity Roadmap")
Path.cwd()

os.getcwd()

Path.home()

Path.cwd().is_absolute()

Path("spam/egg").is_relative_to("spam/egg")

Path("Just a test", "welcone")

 Path("Just a test", "welcone").absolute()

Path.home() / Path("Just a test", "welcone")

os.chdir(r"D:\DECI notes\start")

Path("Just a test", "welcone").absolute()

Path(r"D:/DECI notes/start/Test")

t = Path(r"C:\Users\abdel\Downloads\Automate_the_Boring_Stuff_3e_onlinematerials\Automate_the_Boring_Stuff_3e_onlinematerials")

t.is_dir()

list(t.glob("*.txt"))

for j in list(t.glob("*.txt")):
    j.read_text()

b = Path(r"C:/Users/abdel/Downloads/Automate_the_Boring_Stuff_3e_onlinematerials/Automate_the_Boring_Stuff_3e_onlinematerials/dictionary.txt")

b.read_text()

b.write_text("Welcome home")

(Path.cwd() / "regex_test_file.txt").exists()

f = open("regex_test_file.txt", encoding="UTF-8")
f.readline()
f.close()

f = open(Path("learnt.txt"), "w", encoding="UTF-8")
f.write("That is a Test1\n\n")
f.close()

f = open(Path("learns.txt"), "a", encoding="UTF-8")
f.write("Append is really good!")
f.write("\n")
f.close()

import shelve
shelf_file = shelve.open("keyss")
shelf_file["cats"] = ["zombie", "cow", "dog"]
shelf_file["cows"] = ["zombie", "cow", "dog", "1"]
shelf_file.close()

shelf_file = shelve.open("keyss")
list(shelf_file.items())

shelf_file = shelve.open("keyss")
shelf_file.close()
```
**نص (Markdown Cells):**
```markdown
| _*Chapter 10 Learning*_


========================================================================


Part2


---


PART 3


---

```

---

## 📄 الملف: `Week01\Learning\Jupiter\Day2.ipynb`
- **الامتداد**: `.ipynb`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week01\Learning\Jupiter\Day2.ipynb`

### 📓 Jupyter Notebook
**كود (Code Cells):**
```python
x = 5  # Variable

# char_counter.py

text = input("Input: ")
letter = 0
digit = 0
space = 0
others = 0
for ch in text:
    if ch.isalpha():
        letter += 1
    elif ch.isspace():
        space += 1
    elif ch.isdigit():
        digit += 1
    else:
        others += 1
print(
    f"Output: Letters: {letter}, Digits: {digit}, Spaces: {space}, Others: {others}")

"hello"

# if_elif.py
while True:
    try:
        age = int(input("Age: "))
        assert age > 0 and age < 120, "Please Write a positive integer and correct age"
        break
    except ValueError:
        print("pls write an int")
if age < 13:
    print("child")
elif age > 12 and age < 18:
    print("Teen")
elif age > 17 and age < 65:
    print("Adult")
else:
    print("Very old")

while True:
    try:
        age = int(input("Age: "))
        assert 0 < age < 120, "Invalid age"
        break
    except ValueError:
        print("Please write an integer")
    except AssertionError as e:
        print(e)

if age < 13:
    print("Child")
elif 13 <= age <= 17:
    print("Teen")
elif 18 <= age <= 64:
    print("Adult")
else:
    print("Senior")
```
**نص (Markdown Cells):**
```markdown
Day 2 - Some Mit stupid rev


---

```

---

## 📄 الملف: `Week01\Learning\Jupiter\Day3.ipynb`
- **الامتداد**: `.ipynb`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week01\Learning\Jupiter\Day3.ipynb`

### 📓 Jupyter Notebook
**كود (Code Cells):**
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


factorial(int(input("n: ")))

def fibonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(int(input("n: ")))

def is_palindrome(s):
    while True:
        if len(s) == 1:
            return True
        elif s[0] == s[-1]:
            s = s[1:-1]
        else:
            return False


is_palindrome(input("Enter: "))
```
**نص (Markdown Cells):**
```markdown
Day 3

```

---

## 📄 الملف: `Week01\Learning\Jupiter\Day4.ipynb`
- **الامتداد**: `.ipynb`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week01\Learning\Jupiter\Day4.ipynb`

### 📓 Jupyter Notebook
**كود (Code Cells):**
```python
def binary_search(lst, target, low, high):
    """
    Search an element and returns its index
    """
    # Validation
    if not lst:
        print("Please contain numbers in the list")
        return None

    # ✅ التحقق من النوع BEFORE أي حسابات
    if not isinstance(low, int) or not isinstance(high, int):
        print("Please enter integers")
        return None

    # ✅ التحقق من الحدود
    if low > high:
        return None

    mid = (low + high) // 2

    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search(lst, target, mid + 1, high)
    else:
        return binary_search(lst, target, low, mid - 1)

# activity 2
from time import gmtime


def power(base, exp):
    if not (isinstance(base, int) and isinstance(exp, int)):
        return False

    # ✅ أساس الضرب: أي حاجة⁰ = 1
    if exp == 0:
        return 1

    # ✅ الأساس: أي حاجة¹ = نفسها
    if exp == 1:
        return base

    # ✅ الأس الموجب
    return base * power(base, exp - 1)


first = gmtime().tm_sec
print(power(int(input("Base: ")), int(input("Expo: "))))
print(gmtime().tm_sec - first)

def if_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Finished at 6 min:37 seconds
if_prime(11)

def remove_duplicates(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst
# Finished at 2 min: 37seconds

def reverse_string(string):
    new_string = ""
    for ch in string:
        new_string = ch + new_string
    return new_string

# Finished at 1min : 42 seconds

def factorial_iter(n):
    ans = 1
    if n < 0:
        raise ValueError
    elif n == 1 or n == 0:
        return 1

    for i in range(1, n + 1):
        ans *= i
    return ans

# Finished at 5min: 14sec

def binary_search(lst, target, low, high):

    if not lst:
        return False
    if low > high:
        return False

    mid = (low + high) // 2

    try:
        if target == lst[mid]:
            return mid
        elif lst[mid] > target:
            return binary_search(lst, target, low, mid - 1)
        else:
            return binary_search(lst, target, mid + 1, high)
    except RecursionError:
        return False


# Finished in 9min: 35sec
binary_search([1, 3, 5, 7, 9], 15, 0, 5)
```
**نص (Markdown Cells):**
```markdown
## **Day 4**


## 25/06 الخميس


#### _📝 PS0-A امتحان 60 دقيقة_


##### السؤال 1: Prime Check (12 دق)


##### السؤال 2: Remove Duplicates (12 دق)


##### السؤال 3: Reverse String (12 دق)


##### السؤال 4: Factorial Iterative (12 دق)


##### السؤال 5: Binary Search Recursive (12 دق)

```

---

## 📄 الملف: `Week01\Notes\Day1.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week01\Notes\Day1.md`

```markdown

# اليوم 1 — 18/06/2026

## Phase 0 · Warm-Up


### **Built-in function**   
- 'open()' علشان افتح ملف جديد
- 'close()' علشان اقفل الملف وميعملش overflow
- 'read()' بتقرا كل الي موجود في الملف
- 'readline()' بتقرا سطر سطر ممكن تحطها جوا لوب وبتحرك الcursor معاها
- 'readlines()' بتقرا الملف كلوا وبتسقموا علي سطور في صيغة ليست وبتحرك الcursor معاها
    - يعني انا مقدرش اعمل 'readline()' بعديها علشان هيكون وصل EOF نهاية الملف يعني
- 'with open() as f:' بيفتح ويقفل الملف طول ما انا موجود في indented block


  ### *Modes for 'open()'*
  - 'r'دا الوضع الافتراضي بيقرا الملف
  - 'w' دا بكتب علي الملف وبيعمل resource leak
  - 'a' 
# اليوم 1 — 18/06/2026


## Reading and Writing files


## Phase 0 · Warm-Up


### **Built-in function**   
- 'open()' علشان افتح ملف جديد
- 'close()' علشان اقفل الملف وميعملش overflow
- 'read()' بتقرا كل الي موجود في الملف
- 'readline()' بتقرا سطر سطر ممكن تحطها جوا لوب وبتحرك الcursor معاها
- 'readlines()' بتقرا الملف كلوا وبتسقموا علي سطور في صيغة ليست وبتحرك الcursor معاها
    - يعني انا مقدرش اعمل 'readline()' بعديها علشان هيكون وصل EOF نهاية الملف يعني
- 'with open() as f:' بيفتح ويقفل الملف طول ما انا موجود في indented block


  ### *Modes for 'open()'*
  - 'r'دا الوضع الافتراضي بيقرا الملف
  - 'w' دا بكتب علي الملف وبيعمل resource leak
  - 'a' دا apppend بيعمل اضافة للملف عكس 'w'
    
    دول الي هستخدمهم عمتا والأساس
  - 'rb' & 'wb' دول نفس حوار الي فوق بس دا تبع ملغات ال binary  

#
## from pathlib import Path 

     'help()' is always your friend!!
- 'mkdir(exist_ok=True)' علشان لو الملف كان موجود ميعمبش ايرور
- 'touch()' علشان نعمل ملف نفس لينكس
- Path("a") / "b" / "c" → دمج مسارات
- read_text() / write_text() → قراءة/كتابة سريعة
- exists() / is_file() / is_dir() → فحص الملف
- glob("*.txt") → بحث عن ملفات
- rename() / replace() → نقل ملفات

## ❌ الغلطات
- rename() فشل لأن الملف موجود → استخدم replace() أو افحص exists()
- glob("*") جاب المجلدات كمان → استخدم is_dir() أو glob("*.*")
دا apppend بيعمل اضافة للملف عكس 'w'
    
    دول الي هستخدمهم عمتا والأساس
  - 'rb' & 'wb' دول نفس حوار الي فوق بس دا تبع ملغات ال binary  

#
## from pathlib import Path 

     'help()' is always your friend!!
- 'mkdir(exist_ok=True)' علشان لو الملف كان موجود ميعمبش ايرور
- 'touch()' علشان نعمل ملف نفس لينكس
```

---

## 📄 الملف: `Week01\Notes\Day2.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week01\Notes\Day2.md`

```markdown

# اليوم 2 — 19/06/2026


## MIT 6.001x week 1 review

## Phase 0 · Warm-Up


### Some Notes 
- Using between " >= age >= "
- using list comprehension "new_list = [expression for item in iterable if condition]" 
- using flag variable 
  -    A flag variable in Python is a programming concept where a variable (typically a Boolean holding True or False) acts as a signal to notify your program that a specific condition or event has occurred. It is widely used to control program flow, manage loops, or track the state of an operation.
- Think in the most simplest Solution

```

---

## 📄 الملف: `Week01\Notes\Day3.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week01\Notes\Day3.md`

```markdown
# اليوم 3 — 25/06/2026

## Phase 0 · Warm-Up - W01

### **Some Notes**
- In binary search exclude the number u got and use (mid - 1)(mid + 1) instead of (low = number)
- Don't use preseved keywords as it's a bad style
- Exceptions for **debugging** and unexceptected bugs while if condtions for **validations**
- Think about the **simplest solution**
- Try thinking better
```

---

## 📄 الملف: `Week01\Notes\Day4.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week01\Notes\Day4.md`

```markdown
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

```

---

## 📄 الملف: `Week01\Resources\resources.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week01\Resources\resources.md`

```markdown
## Resources for Week 01

- [Automate the Boring Stuff with Python 3rd edition chapter 10](https://automatetheboringstuff.com/3e/chapter10.html)

- [MIT 6.00.1x Study Notes](https://docs.google.com/document/d/1oMYRnogRrGgCtz-26E8hJYLp7Bm99JS1SP4lhdXvqpw/edit?usp=sharing)

- [Git & GitHub Crash Course for Beginners [2026]](https://www.youtube.com/watch?v=mAFoROnOfHs)
```

---

## 📄 الملف: `Week02\Learning\Jupiter\Day5-7.ipynb`
- **الامتداد**: `.ipynb`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week02\Learning\Jupiter\Day5-7.ipynb`

### 📓 Jupyter Notebook
**كود (Code Cells):**
```python
# First and most used
import os

# Second and used when knowing what are you using
from math import sin

""" 
Third and used when you want to make an alias for something 
and use it later with that name 
"""
import numpy as np

# Fourth importing everything from a library (Never used acually)
from random import *

f = open(FILEPATH, MODE, encoding="UTF-8")

f.read()  # Reads the entire file
f.readline()  # Reads only the first line (You can use a loop and print each line)
f.readlines()  # Reads the entire file and save each line in a list
f.write()  # Write on a file what do you want

"""
with open(FILEPATH, MODE) as file:
    What do you want to do

We use with statement instead of opening a file and closing it in diff line
which is a bad approach. with opens a file for you and
closes it once u are not in the idented block
"""

format(0.1, ".20f")

format(0.5, ".20f")

0.1 + 0.2 == 0.3

from decimal import Decimal

Decimal('0.1') + Decimal('0.2') == Decimal('0.3')

# Exercise 1

"""
A tuple is like a list but the only diff it's immutable ("hi",)
"""
s = ("hello", 1, [1, 2], {"1", "one"})

# Exercise 2

my_tuple = (10, 20, 30, 40, 50)

my_tuple[2]
my_tuple[-1]
my_tuple[1:4]

# Exercise 3

x, y, z = (1, 2, 3)  # x = 1, y= 2, z = 3

# Exercise 4

s = ("hello", 1, [1, 2], {"1", "one"})

len(s)
sums = s + ("hello bro",)
s * 3
[1, 2] in s
```
**نص (Markdown Cells):**
```markdown
### Day 5 Reviewing Mit 6.001x **(Modules & File I/O)** Morning 🌞


##### Open() modes


| Modes |         Meaning          | If file exists | If file doesn't exist |
| :---- | :----------------------: | -------------: | :-------------------- |
| 'r'   |      Reading a file      |           runs | Error                 |
| "rb"  |  Reading a binary file   |           runs | Error                 |
| "w"   |    Writing on a file     |           runs | creates the file      |
| "wb"  | Writing on a binary file |           runs | creates the file      |
| "a"   |    Append to the file    |           runs | creates the file      |


##### Reading and Writing files


#### Using with statement


#### Intro to py popular modules


| Module name |                                                                                                                     Its function                                                                                                                      |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| datetime    |                                                                                                        To work with dates and times in Python                                                                                                         |
| sys         |                                                            A built-in module that provides access to system-specific parameters, functions, and the Python interpreter runtime environment                                                            |
| os          |        The os module in Python is a built-in library that lets you interact with your operating system directly from your code. It provides portable, cross-platform functions to manage files, directories, paths, and environment variables.        |
| json        |                                                              Python handles JSON data using its built-in json module, which allows you to convert Python objects to JSON and vice-versa.                                                              |
| decimal     | In Python, decimal is a built-in module that provides the Decimal data type for exact, base-10 floating-point arithmetic. It is specifically designed to eliminate the precision and rounding errors commonly caused by the standard float data type. |


---


#### Day 6 - Evening & Morning Session (W02 - 28/06): Binary & Float Precision


---


#### Day 7 - W02 (29/06) - Tuples: Theory & Practice

```

---

## 📄 الملف: `Week02\Learning\Jupiter\Day8-9.ipynb`
- **الامتداد**: `.ipynb`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week02\Learning\Jupiter\Day8-9.ipynb`

### 📓 Jupyter Notebook
**كود (Code Cells):**
```python
my_list = [10, 20, 30, 40, 50]

# Way 1
my_list + [10]

# Way 2
my_list.append(10)

# ------------
# way 1
my_list + [10]

# way 2
my_list.extend([10])

# ------

my_list.remove(10)
# -----
del my_list[2]

# -----------------------------------------------------------

dir(list)

def func(lst, values):
    for i in lst:
        print(list(map(i, values)))


func([abs, str], [-4, 3, -5])

list(filter(lambda x: x > 0, [0, 5]))

# Extra Exercise

logs = [
    "192.168.1.10:admin:FAILED",
    "10.0.0.5:root:SUCCESS",
    "192.168.1.10:guest:FAILED",
    "10.0.0.5:admin:FAILED",
    "172.16.0.1:user:FAILED",
    "192.168.1.10:root:FAILED",
    "8.8.8.8:test:SUCCESS"
]

whitelist = ["10.0.0.5", "192.168.1.10"]


failed_logs = list(filter(lambda x: "FAILED" in x, logs))
ip_failed_logs = list(map(lambda x: x.split(":")[0], failed_logs))
filtred = list(filter(lambda x: x not in whitelist, ip_failed_logs))

# --------

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x > 50, map(lambda x: x**3, filter(lambda x: x % 2 == 0, nums))))

server = {
    "name": "web-server-01",
    "ip": "192.168.1.10",
    "status": "active",
    "uptime": 365
}

server["ip"]
server["status"] = "maintenance"
server["location"] = "Cairo"
del server["uptime"]

user = {"name": "Ahmed", "role": "analyst", "level": 3}

for key in user:
    user[key]

for key, value in user.items():
    print(value)
{x: x ** 2 for x in range(6)}

from csv import DictReader

with open(r"D:\vs code\cybersecurity-roadmap\Phase-1\Month-1\Week02\Learning\Python\sample_data.csv", "r") as f:
    content = list(DictReader(f))
    for i in content:
        print(i["age"])
    print(content)
```
**نص (Markdown Cells):**
```markdown
### Day 8 - W02 (30/06) - Python Lists, Mutability & Functional Tools


#### lambada , filter() and map()


##### Extra Exercise


---


### Day 9 - W02 (01/07) - Dictionaries & Frequency Analysis

```

---

## 📄 الملف: `Week02\Learning\Python\csv_analyzer.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week02\Learning\Python\csv_analyzer.py`

```python
# Day 10

from sys import argv
from os import path
from csv import DictReader
from json import dump

def detect_encoding(file_path):
    """
    تحاول تفتح الملف بأكتر من ترميز عشان متقفش قدام UTF-16 أو UTF-8.
    """
    encodings = ['utf-8', 'utf-16']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                f.read()
            return enc
        except UnicodeDecodeError:
            continue
    return None

def read_csv(file_path):
    """
    تقرأ ملف CSV وتحوله لـ list of dicts.
    لو حصل أي مشكلة، ترجع None عشان البرنامج ميكسرش.
    """
    try:
        encoding = detect_encoding(file_path)
        if encoding is None:
            print("Error: Unable to detect file encoding (tried UTF-8 and UTF-16).")
            return None

        with open(file_path, 'r', encoding=encoding) as f:
            return list(DictReader(f))
    
    except Exception as e:
        print(f"Error: Invalid CSV format or corrupted file. Details: {e}")
        return None

def calculate_stats(rows, column_name):
    """
    تحسب التكرارات، القيم الفريدة، والقيمة الأكثر تكراراً.
    """
    freq = {}
    
    for row in rows:
        value = row[column_name]
        # الطريقة الاحترافية (بتاعت .get) عشان توفر السطور
        freq[value] = freq.get(value, 0) + 1

    # القيم الفريدة = عدد المفاتيح في القاموس (أسهل من الـ loop اللي كنت بتعمله)
    unique_count = len(freq)
    
    # العنصر الأكثر تكراراً باستخدام max (اختصر الـ loop الطويل بتاعك)
    most_common = max(freq, key=freq.get) if freq else None

    return {
        "total_rows": len(rows),
        "column_analyzed": column_name,
        "unique_values": unique_count,
        "most_common": most_common,
        "frequency": freq
    }

def save_to_json(data):
    """
    تحفظ النتيجة في ملف JSON.
    """
    with open("analysis_report.json", "w", encoding='utf-8') as f:
        dump(data, f, indent=4)
    print("✅ Report saved successfully to analysis_report.json")

def main():
    # 1. استقبال اسم الملف
    if len(argv) != 2:
        file_path = input("Please enter the CSV file name: ")
    else:
        file_path = argv[1]

    # 2. التحقق من وجود الملف ونوعه (إصلاح الـ AND لـ OR)
    if not path.exists(file_path):
        print("Error: File not found.")
        return
    if not path.isfile(file_path) or not file_path.lower().endswith(".csv"):
        print("Error: The provided path is not a valid CSV file.")
        return

    # 3. قراءة الملف (مع Try/Except)
    rows = read_csv(file_path)
    if rows is None:
        return  # لو حصل خطأ، نقف هنا

    # 4. التحقق من وجود العمود المطلوب (عشان ميحصلش KeyError)
    column = "age"
    if rows and column not in rows[0]:
        print(f"Error: Column '{column}' not found in CSV. Available columns: {list(rows[0].keys())}")
        return

    # 5. حساب الإحصائيات وحفظها
    stats = calculate_stats(rows, column)
    save_to_json(stats)

if __name__ == "__main__":
    main()
```

---

## 📄 الملف: `Week02\Learning\Python\file_analyzer.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week02\Learning\Python\file_analyzer.py`

```python
# Day 5 Exercise

import sys
import os
import json

def analyze_file(file_path):
    """تحليل ملف نصي وإرجاع إحصائياته."""
    if not os.path.exists(file_path):
        print(f"❌ خطأ: الملف '{file_path}' مش موجود.")
        return None
    if not os.path.isfile(file_path):
        print(f"❌ خطأ: '{file_path}' مش ملف صحيح.")
        return None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ خطأ أثناء القراءة: {e}")
        return None

    return {
        "filename": os.path.basename(file_path),
        "lines": len(content.splitlines()),
        "words": len(content.split()),
        "characters": len(content)
    }

def save_to_json(data, output_path="analysis.json"):
    """حفظ البيانات في ملف JSON."""
    if data is None:
        return
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✅ تم حفظ النتيجة في: {output_path}")

if __name__ == "__main__":
    # استقبال اسم الملف
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("ادخل مسار الملف النصي: ")

    result = analyze_file(file_path)
    save_to_json(result)
```

---

## 📄 الملف: `Week02\Learning\Python\letter_frequency.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week02\Learning\Python\letter_frequency.py`

```python
# Day 9

from sys import argv
from os import path
from json import dump

def calc_frequency(content):
    freq = {}
    for ch in content:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] = freq.get(ch, 0) + 1
    return {char: count for char, count in sorted(freq.items(), key=lambda x: -x[1])}



def save_json(my_dict):
    with open("answer.json", "w") as f:
        dump(my_dict, f, indent= 4)


def main():
    if len(argv) != 2:
        file_path = input("Please enter the file name: ")
    else:
        file_path = argv[1]

    if not path.exists(file_path):
        print("The file not exist")
        return None
    elif not path.isfile(file_path):
        print("That is not a file")
        return None
    with open(file_path, "r", encoding="UTF-8") as f:
        content = f.read()

    my_dict = calc_frequency(content)
    save_json(my_dict)

if __name__ == "__main__":
    main()
```

---

## 📄 الملف: `Week02\Learning\Python\reverse_tuple.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week02\Learning\Python\reverse_tuple.py`

```python
# Day 7

def reverse_tuple(my_tuple):
    return my_tuple[::-1]

reverse_tuple((10, 20, 30, 40, 50))
```

---

## 📄 الملف: `Week02\Notes\Day5-7.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week02\Notes\Day5-7.md`

```markdown
# Week 02 (27/06 - 29/06) - File I/O, Float Precision & Tuples

---

### Day 5 - Evening & Morning Session (W02 - 27/06): Practical File I/O & CLI Scripting

#### 1. Key Modules & Functions I Used Today

- **`sys.argv`**: 
  - A list that stores command-line arguments.
  - `argv[0]` = script name, `argv[1]` = first argument (the file path).
  - **Use case**: Makes the script flexible without hardcoding file names.

- **`os.path`**:
  - `os.path.exists(path)`: Returns `True` if the file/folder exists.
  - `os.path.isfile(path)`: Returns `True` if it's a file (not a folder). Prevents reading directories by mistake.
  - `os.path.basename(path)`: Extracts the file name from the full path. (e.g., `C:/docs/file.txt` -> `file.txt`).

- **`json.dump()`**:
  - Writes a Python dictionary directly into a `.json` file.
  - Better than `json.dumps()` + `f.write()` because it's more direct and memory-efficient.
  - **Key args**: `indent=4` (for readability), `ensure_ascii=False` (to preserve Arabic characters).

---

#### 2. Mistakes I Made & How I Fixed Them

| Mistake | What I did wrong | The Fix |
| :--- | :--- | :--- |
| **Modifying `sys.argv`** | I tried to append a user input directly to `argv` if the user forgot the argument. | Never modify `sys.argv`. Use a separate variable (e.g., `file_path`) to handle the logic. |
| **Reading the file twice** | Used `f.readlines()` then used `''.join(content)` twice to count words and characters. | Used `f.read()` once to get the full text as a single string. This saves memory and time (best practice). |
| **Filename in report** | Saved the full path (e.g., `/home/user/projects/data.txt`) as the filename. | Used `os.path.basename()` to save only `data.txt` for a cleaner JSON report. |

---

#### 3. Best Practices I Applied Today

1. **Separation of Concerns**:
   - I separated the analysis logic (`analyze_file`) from the saving logic (`save_to_json`). 
   - If I want to use this analyzer in a web app or another project later, I can just `import` it without running the CLI part automatically.

2. **The `if __name__ == "__main__":` Guard**:
   - Wrapped the script execution inside this block.
   - **Why?** If someone imports my script, it won't run automatically. It only runs when I execute the script directly from the terminal.

3. **Defensive Programming (Validations)**:
   - Check if the file exists.
   - Check if the path points to a file, not a folder.
   - Wrap the file reading in a `try/except` block to catch unexpected errors (e.g., permission denied).

---

#### 4. Test Cases Results (Validation)

| # | Scenario | Command | Expected Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Normal text file | `python file_analyzer.py test.txt` | JSON with correct counts | ✅ Passed (Counted 26 chars including newline) |
| 2 | Empty file | `python file_analyzer.py empty.txt` | `lines: 0, words: 0, chars: 0` | ✅ Passed |
| 3 | File with empty lines | `python file_analyzer.py blank.txt` | Correctly counted empty rows | ✅ Passed |
| 4 | File does NOT exist | `python file_analyzer.py missing.txt` | Prints error message, doesn't crash | ✅ Passed |
| 5 | Path is a folder | `python file_analyzer.py ./` | Prints error message, doesn't crash | ✅ Passed |

---

#### 5. Final Code Architecture (Mental Model)

1. **Input**: `sys.argv` OR `input()`.
2. **Validation**: `os.path.exists` + `os.path.isfile`.
3. **Processing**: 
   - `with open(...) as f: content = f.read()`
   - `splitlines()` for lines.
   - `split()` for words.
   - `len()` for characters.
4. **Output**: 
   - Build dictionary.
   - `json.dump()` to `analysis.json`.

---

#### 6. Summary (What I learned today)

- Writing a CLI tool is not scary. `sys.argv` is my friend.
- Always assume the user will make a mistake (Defensive Programming).
- Using `read()` is more efficient than `readlines()` when I need the whole text.
- Clean code = reusable code (Separation of functions).

---

### Day 6 - Evening & Morning Session (W02 - 28/06): Binary & Float Precision

#### 1. The Shocking Fact

- In Python, `0.1 + 0.2 == 0.3` returns **`False`**.
- The result of `0.1 + 0.2` is actually `0.30000000000000004`.

#### 2. The Simple Reason (Why?)

- Computers only speak **Binary (0s and 1s)**.
- In binary, the decimal number `0.1` is a **repeating fraction** (just like `1/3 = 0.33333...` in our decimal system).
- Because computer memory is limited, it cuts off the repeating number and stores a **rounded approximation**.
- So, `0.1` stored in memory is actually `0.10000000000000000555` (a tiny bit more than 0.1).

#### 3. The Rule of Thumb (When does it end?)

- A decimal fraction has an **exact** binary representation **only if** the denominator (in its simplest form) is a power of `2`.
    - `0.5` (1/2) -> Exact (Power of 2).
    - `0.75` (3/4) -> Exact (Power of 2).
    - `0.1` (1/10) -> **NOT** exact (10 = 2 × 5). -> Repeating (Rounded).

#### 4. The Hidden Truth: `str()` vs `repr()`

- **`str()`** (String): Shows the **pretty/readable** version for humans. (Prints `0.1`).
- **`repr()`** (Representation): Shows the **exact/raw** version for programmers. (Prints `0.10000000000000000555`).
- *Lesson:* Use `repr()` whenever you want to see what the computer *actually* stored.

#### 5. The Safe Fix (How to code properly)

- **Don't** use `==` (equals) to compare two floats directly.
- **Do** check if the **difference** between them is very tiny.
- **The Solution Code:**

"```python
#### Safe comparison function
def is_close(a, b):
    return abs(a - b) < 1e-9"

#### Test it
print(is_close(0.1 + 0.2, 0.3))  # Output: True

---------------------------

### Day 7 - W02 (29/06) - Tuples: Theory & Practice

#### 1. What is a Tuple?

- A Tuple is a collection type in Python, similar to a List, but **Immutable** (cannot be changed after creation).
- **Syntax:** Defined using parentheses `()`.
- **Example:** `my_tuple = (10, 20, 30, 40, 50)`
- **Note:** They can hold mixed data types (e.g., `("hello", 1, [1, 2])`).

#### 2. Indexing & Slicing (Accessing Data)

- **Indexing:** Access specific items using `[index]` (starts at 0).
  - `my_tuple[2]` → `30` (Third element).
  - `my_tuple[-1]` → `50` (Last element, using negative indexing).
- **Slicing:** Access a range of items using `[start:end]` (end is exclusive).
  - `my_tuple[1:4]` → `(20, 30, 40)`.

#### 3. Unpacking (Assigning to variables)

- You can assign Tuple elements to multiple variables in one line.
- **Correct:** `x, y, z = (1, 2, 3)` → `x=1, y=2, z=3`.
- **Error (Discovered Practically):** `x, y, z = my_tuple` (where my_tuple has 5 elements).
  - Result: `ValueError: too many values to unpack (expected 3, got 5)`.
  - **Lesson:** The number of variables MUST match the number of elements.

#### 4. Tuple Operations (Allowed)

Since Tuples are immutable, we cannot modify them, but we can perform these actions:

- **Length:** `len(my_tuple)` → `5`.
- **Concatenation:** `my_tuple + (50,)` → `(10, 20, 30, 40, 50, 50)`. 
  - *(Note: Must add a trailing comma `,` to create a single-element tuple).*
- **Repetition:** `my_tuple * 3` → Repeats the tuple 3 times.
- **Membership:** `30 in my_tuple` → `True`.

#### 5. Reversing a Tuple (Slicing Trick)

- **Syntax:** `my_tuple[::-1]`.
- **Result:** `(50, 40, 30, 20, 10)`.
- **Function created:**

```python
def reverse_tuple(t):
    return t[::-1]
```

---

## 📄 الملف: `Week02\Notes\Day8-10.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week02\Notes\Day8-10.md`

```markdown
# Week 02 (30/06 - 1/07 - 2/07) - Python Lists, Dictionaries, PS0-B


## Day 8 - W02 (30/06) - Python Lists, Mutability & Functional Tools

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Lists, Tuples, Mutability, Aliasing, `enumerate()`, `map()`, `filter()`, `lambda`

---

## 1. List vs Tuple

| Feature | `list` | `tuple` |
|---------|--------|---------|
| Mutability | Mutable (`[]`) | Immutable (`()`) |
| Memory | Larger (~104 bytes) | Smaller (~88 bytes) |
| Use Case | Dynamic data (logs, scan results) | Fixed data (port numbers, protocols) |

**Rule:** Use `tuple` for constants, `list` for data that changes.

```python
# Fixed port list (tuple)
COMMON_PORTS = (22, 80, 443, 3389)

# Dynamic scan results (list)
open_ports = [22, 80]
```

---

## 2. Adding: In-Place vs New

| Method | Modifies Original? | Behavior |
|--------|-------------------|----------|
| `append(x)` | ✅ Yes | Adds one element to end |
| `extend([x,y])` | ✅ Yes | Merges another list (flattens) |
| `+` | ❌ No | Returns a **new** list |

```python
# In-place (modifies original)
ports = [22, 80]
ports.append(443)          # [22, 80, 443]
ports.extend([3306, 5432]) # [22, 80, 443, 3306, 5432]

# New object (original unchanged)
ports = [22, 80]
new_ports = ports + [443]  # ports is still [22, 80]
```

**Trap:** `ports + [443]` does nothing if you don't save it!

```python
ports + [443]  # BUG: result is created then discarded
```

---

## 3. Removing

```python
ips = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]

ips.remove("10.0.0.1")     # Removes first occurrence
del ips[0]                  # Removes by index
ips.pop()                   # Removes & returns last item
ips.clear()                 # Empties the list
```

**Note:** `remove()` raises `ValueError` if item doesn't exist. Check first:

```python
if "bad_ip" in blocklist:
    blocklist.remove("bad_ip")
```

---

## 4. Sorting: `sort()` vs `sorted()`

| Method | Returns | Modifies Original? | Use When |
|--------|---------|-------------------|----------|
| `list.sort()` | `None` | ✅ Yes | You don't need the old order |
| `sorted(list)` | New list | ❌ No | You need to preserve original |

```python
# sort() - destroys original order
nums = [3, 1, 4, 1, 5]
nums.sort()           # nums is now [1, 1, 3, 4, 5]

# sorted() - keeps original
nums = [3, 1, 4, 1, 5]
new_nums = sorted(nums)  # nums unchanged, new_nums is [1, 1, 3, 4, 5]
```

---

## 5. Aliasing: The Silent Security Risk 🚨

```python
# DANGER: This is NOT a copy!
original = ["10.0.0.99", "192.168.1.100"]
backup = original        # ALIAS - same object, two names

backup.append("8.8.8.8")
print(original)          # ["10.0.0.99", "192.168.1.100", "8.8.8.8"] - OOPS!
```

**Safe copy methods:**

```python
copy1 = original[:]        # Slice copy
copy2 = original.copy()    # Method copy
copy3 = list(original)     # Constructor copy
```

**Security Impact:** Modifying an aliased blocklist by mistake can open holes in your SOC automation.

---

## 6. Looping with `enumerate()`

```python
# The old way (verbose)
i = 0
for ip in ip_list:
    print(i, ip)
    i += 1

# The professional way
for index, ip in enumerate(ip_list):
    print(f"[{index}] {ip}")

# Start from 1 (for reports)
for line_num, ip in enumerate(bad_ips, start=1):
    print(f"{line_num}. {ip} - FLAGGED")
```

---

## 7. `map()`, `filter()`, `lambda` (Extra)

| Tool | Purpose | Output Size |
|------|---------|-------------|
| `map(func, iterable)` | Apply function to every element | Same as input |
| `filter(func, iterable)` | Keep only `True` elements | Less or equal |
| `lambda args: expr` | One-line anonymous function | — |

**SOC Log Analysis (what you solved):**

```python
logs = [
    "192.168.1.10:admin:FAILED",
    "10.0.0.5:root:SUCCESS",
    "172.16.0.1:guest:FAILED",
    "8.8.8.8:admin:FAILED",
]
whitelist = {"10.0.0.5", "192.168.1.10"}

# Pipeline: Filter FAILED → Extract IP → Remove whitelisted
threats = list(
    filter(
        lambda ip: ip not in whitelist,
        map(
            lambda log: log.split(":")[0],
            filter(lambda log: log.endswith("FAILED"), logs)
        )
    )
)
# Result: ['172.16.0.1', '8.8.8.8']
```

**The One-Liner (even → cube → >50):**

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x > 50, map(lambda x: x**3, filter(lambda x: x % 2 == 0, nums))))
# [64, 216, 512, 1000]
```

---

## 8. Errors I Made Today

| Mistake | Why It Was Wrong | Correct Way |
|---------|-----------------|-------------|
| `"FAILED" in log` | Matches "FAILED" anywhere in string | `log.endswith("FAILED")` — checks last field only |
| `my_list + [50]` | Creates new list, original unchanged | `my_list.append(50)` or `my_list = my_list + [50]` |
| `copy = original` | Creates alias, not a copy | `copy = original[:]` or `copy = original.copy()` |

---

## 9. Quick Cheat Sheet

```python
# Adding
append(x)       # Add one item (in-place)
extend([x,y])   # Merge list (in-place)
+               # New list (concatenation)

# Removing
remove(value)   # First occurrence
del list[i]     # By index
pop()           # Last item (returns it)

# Sorting
sort()          # Modifies original
sorted()        # Returns new list

# Copying
[:]             # Shallow copy
.copy()         # Shallow copy

# Looping
enumerate(list, start=1)  # Index + value

# Functional
map(func, iter)     # Transform all
filter(func, iter)  # Select subset
lambda x: x**2      # Inline function
```

---

- ✅ **Status:** Day 8 Complete — Lists, Mutability, Aliasing, `enumerate`, `map`, `filter`, `lambda`  
- 🚀 **Next:** W03 — Dictionaries & Sets
-----------------------
# Day 9 - W02 (01/07) - Dictionaries & Frequency Analysis

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Dictionaries, Key-Value Storage, `get()`, `.items()`, Sorting, `lambda`, Dict Comprehension

---

## 1. Dictionary Basics

A dictionary is a mutable collection of **key-value** pairs. Access values by **key**, not index.

```python
server = {"name": "web-01", "ip": "192.168.1.10", "status": "active"}

# Access
print(server["ip"])           # "192.168.1.10"

# Update
server["status"] = "maintenance"

# Add
server["location"] = "Cairo"

# Delete
del server["name"]

# Check existence
if "ip" in server:
    print("Key exists!")
```

---

## 2. Dict vs List

| Feature | List | Dictionary |
|---------|------|------------|
| Structure | Ordered sequence | Key-Value pairs |
| Access | By index `[0]` | By key `["name"]` |
| Search | O(n) | O(1) |
| Use Case | Sequences, queues | Lookups, configs, counting |

---

## 3. Safe Access: `get()` vs `[]`

| Method | Key Exists | Key Missing |
|--------|-----------|-------------|
| `dict["key"]` | Returns value | **KeyError** (crashes) |
| `dict.get("key")` | Returns value | Returns `None` |
| `dict.get("key", default)` | Returns value | Returns `default` |

**Rule:** Always use `get()` when processing external data (logs, user input).

```python
# Safe lookup with default
port = config.get("ssh_port", 22)   # Returns 22 if key missing
```

---

## 4. Looping with `.items()`

```python
user = {"name": "Ahmed", "role": "analyst", "level": 3}

# Keys only
for key in user.keys():
    print(key)

# Values only
for value in user.values():
    print(value)

# Both (most common)
for key, value in user.items():
    print(f"{key}: {value}")
```

---

## 5. Frequency Counting (The Pro Trick)

**Old way (verbose):**
```python
if ch not in freq:
    freq[ch] = 1
else:
    freq[ch] += 1
```

**Professional way (one-liner):**
```python
freq[ch] = freq.get(ch, 0) + 1
```

**Why it works:** `get(ch, 0)` returns `0` for new keys, so `0 + 1 = 1` on first occurrence.

---

## 6. Sorting Dictionaries by Value

Dictionaries are designed for lookups, not order. Use `sorted()` with `.items()` and `lambda`.

```python
freq = {"a": 5, "b": 2, "c": 8}

# Sort by value descending (highest first)
sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
# Result: [("c", 8), ("a", 5), ("b", 2)]

# Alternative: negative trick (no reverse=True needed)
sorted_items = sorted(freq.items(), key=lambda x: -x[1])
```

**Breaking down `lambda x: x[1]`:**
- `x` is a tuple like `("a", 5)`
- `x[0]` is the key (`"a"`)
- `x[1]` is the value (`5`)
- So we sort by the **count**, not the character

---

## 7. Dict Comprehension

Build dictionaries in one line, just like list comprehensions.

```python
# Squares
squares = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Sort and convert back to dict (your extra task)
result = {char: count for char, count in sorted(freq.items(), key=lambda x: -x[1])}
```

---

## 8. Script Architecture (Mental Model)

A clean script structure for your `letter_frequency.py`:

```
main()              → Input, validation, file reading
calc_frequency()    → Counting logic, returns sorted dict
save_json()         → Write result to file
__main__ guard      → Prevents execution on import
```

**Best practice:** Keep functions **pure** — take inputs as arguments, return outputs. Avoid global variables.

---

## 9. Errors I Made Today

| Mistake | Why It Was Wrong | Correct Way |
|---------|-----------------|-------------|
| `dict["key"]` on unknown key | Crashes with `KeyError` | `dict.get("key", default)` |
| Looping without `.items()` | Only gets keys, not values | `for k, v in dict.items():` |
| Assuming dict order | Dictionaries are for lookups, not sequence | Use `sorted()` when order matters |
| Modifying dict while looping | Raises `RuntimeError` | Build a new dict, or loop over `list(dict.items())` |

---

## 10. Quick Cheat Sheet

```python
# Create
d = {"a": 1, "b": 2}
d = dict(a=1, b=2)

# Access
d["a"]              # -> 1 (KeyError if missing)
d.get("c")          # -> None (safe)
d.get("c", 0)       # -> 0 (safe with default)

# Add / Update
d["new"] = 100

# Delete
del d["a"]

# Iterate
for k, v in d.items():
    print(k, v)

# Check
if "a" in d: ...

# Comprehension
{x: x**2 for x in range(3)}     # {0: 0, 1: 1, 2: 4}

# Sort by value
sorted(d.items(), key=lambda x: x[1], reverse=True)
```

---

##### ✅ **Status:** Day 9 Complete — Dictionaries, `get()`, `.items()`, Frequency Analysis, Sorting with `lambda`, Dict Comprehension  
##### 🚀 **Next:** W03 — Nested Dictionaries & Sets (Threat Intelligence logs)
----
# Day 10 - W02 (02/07) - PS0-B Exam: CSV Data Analyzer

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** CSV Parsing, `DictReader`, File Encodings, Frequency Counting, Error Handling, `sys.argv`, JSON Export  
> **Status:** ✅ Exam Completed (Time-boxed: 60 minutes)

---

## 1. The Mission

Build `csv_analyzer.py` that:
1. Reads a CSV file (CLI arg or `input()`).
2. Converts it to a **list of dictionaries** via `csv.DictReader`.
3. Calculates column statistics (`age`):
   - Total rows
   - Unique values
   - Most common value
   - Frequency distribution
4. Saves results to `analysis_report.json`.
5. Handles errors gracefully with `try/except`.

---

## 2. Key Libraries

| Library | Purpose |
|---------|---------|
| `sys` | Command-line arguments (`sys.argv`) |
| `os.path` | File validation (`exists`, `isfile`) |
| `csv.DictReader` | Maps CSV headers to dict keys |
| `json.dump` | Saves report with `indent=4` |

---

## 3. Technical Deep Dive

### A. The Encoding Problem (UTF-8 vs UTF-16)

**Issue:** Output showed `` between characters (`bob`) — signature of **UTF-16 LE**, not UTF-8.

**Why:** File saved in UTF-16 (common in Windows exports).

**Fix:**
```python
def detect_encoding(file_path):
    for enc in ['utf-8', 'utf-16']:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                f.read()
            return enc
        except UnicodeDecodeError:
            continue
    return None
```

**Lesson:** Always assume encoding might not be UTF-8. `` bytes = UTF-16.

---

### B. Frequency Counting

**Old way:**
```python
if value not in freq:
    freq[value] = 1
else:
    freq[value] += 1
```

**Professional way:**
```python
freq[value] = freq.get(value, 0) + 1
```

---

### C. Finding Most Common Value

**Old way:**
```python
most_common = None
max_count = 0
for key, count in freq.items():
    if count > max_count:
        max_count = count
        most_common = key
```

**Optimized:**
```python
most_common = max(freq, key=freq.get)
```

---

### D. Error Handling

```python
def read_csv(file_path):
    try:
        with open(file_path, 'r', encoding=detect_encoding(file_path)) as f:
            return list(csv.DictReader(f))
    except Exception as e:
        print(f"Error: {e}")
        return None
```

---

## 4. Mistakes & Fixes

| Mistake | What Happened | Fix |
|---------|--------------|-----|
| **Encoding Error** | `` bytes in output | Added encoding detection for UTF-16 |
| **`and` vs `or`** | `txt` files slipped through validation | Changed to `or`: `if not isfile or not endswith(".csv")` |
| **Missing `try/except`** | Script crashed on corrupted CSV | Wrapped file reading in `try/except` |
| **Verbose Logic** | 4 lines for frequency counting | Replaced with `freq.get(value, 0) + 1` |

---

## 5. Code Architecture

```
detect_encoding()   → Try UTF-8, then UTF-16
read_csv()          → DictReader with correct encoding
calculate_stats()   → Frequencies, unique count, most common
save_to_json()      → Write analysis_report.json
main()              → sys.argv, validation, orchestration
```

---

## 6. Quick Cheat Sheet

```python
# Read CSV
reader = csv.DictReader(f)
rows = list(reader)  # [{"name": "Ali", "age": 25}, ...]

# Count Frequency
freq = {}
for row in rows:
    val = row["column"]
    freq[val] = freq.get(val, 0) + 1

# Most Common
most_common = max(freq, key=freq.get)

# Unique Count
unique_count = len(freq)

# Save JSON
with open("report.json", "w") as f:
    json.dump(data, f, indent=4)
```

---

## 7. Self-Assessment

**What went well:**
- Parsed CSV to dictionaries successfully
- Calculated all statistics correctly
- Clean modular structure (separate functions)
- Handled UTF-16 encoding surprise

**Needs improvement:**
- Add `try/except` *before* it breaks (reactive → proactive)
- Remember `and`/`or` logic under time pressure

**Progress vs Week 1:**
- Breaking code into functions (not monolithic)
- Thinking about edge cases (file not found, wrong encoding)
- Using advanced features (`max` with `key`, `.get()`) more naturally

---

✅ **Status:** PS0-B Complete  
🚀 **Next:** `os.walk` and advanced file system operations (W03)
```

---

## 📄 الملف: `Week02\Resources\resources.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week02\Resources\resources.md`

```markdown
## Resources for Week 02

- [Automate the Boring Stuff with Python 3rd edition chapter 7 [R] ](https://automatetheboringstuff.com/3e/chapter7.html)

- [MIT 6.00.1x Study Notes](https://docs.google.com/document/d/1oMYRnogRrGgCtz-26E8hJYLp7Bm99JS1SP4lhdXvqpw/edit?usp=sharing)

```

---

## 📄 الملف: `Week03\Learning\Python\bank.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Learning\Python\bank.py`

```python
# Some Exersices (Day 13)
from random import randint


class Bank:
    account_id = 0
    def __init__(self, name,password,balance):
        self.name = name
        self._password = password
        self.balance = balance
        self.account_id = str(Bank.account_id).zfill(4)

        account_number = str(randint(1,9999))
        for i in range(3):
           account_number += "-" + str(randint(1,9999)) 
        self.__account_number = account_number

        Bank.account_id += 1

    def __str__(self):
        return f"Your name is {self.name}. You have in your credit card {self.balance}."
    
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_pass):
        self._password = new_pass
    
test = Bank("hi", "ok", 0)
print(test.password)

print(test)

test.password = "Aliens"
print(test.password)

```

---

## 📄 الملف: `Week03\Learning\Python\debug_practice.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Learning\Python\debug_practice.py`

```python
# Day 11

# -*- coding: utf-8 -*-
"""
Practice script with several intentional subtle bugs.
Find them without running... then run to check yourself.
"""
from random import choice

# Done
def remove_duplicates(lst):
    result = lst[:]
    for item in lst:
        if result.count(item) > 1:
            result.remove(item)
    return result

# Done
def get_average(numbers):
    return sum(numbers) / len(numbers)

# Done
def find_max_index(lst):
    max_value = lst[0]
    max_idx = 0
    for i in range(len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
            max_idx = i
    return max_idx

# Done
def merge_dicts(d1, d2):
    result = d1.copy()
    for key in d2:
        result[key] = d2[key]
    return result

# Done
def count_words(sentence):
    words = sentence.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

# Done
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True

def main():
    nums = [1, 1, 1]
    print("Original:", nums)
    print("No duplicates:", remove_duplicates(nums))
    print("Still original after removing dups?:", nums)

    print("Average:", get_average([1, 2, 3]))
    print("Average again (same call):", get_average([1, 2, 3]))

    print(find_max_index([-5, -2, -9, -1]))

    d1 = {'a': 1}
    d2 = {'b': 2}
    merged = merge_dicts(d1, d2)
    print("d1 after merge:", d1)

    print(count_words("the cat sat on the mat the cat ran"))

    print(is_sorted([1, 2, 3, 4, 5]))

main()
```

---

## 📄 الملف: `Week03\Learning\Python\employee.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Learning\Python\employee.py`

```python
# Some Exercises Day 15


"""
Comprehensive exercise: Employee management system for a cybersecurity
company (CyberShield Inc.)
========================================================================
Each TODO covers one concept from the video. Complete them in order,
then run this file (python security_agency_exercise.py) to check your 
solutions against the expected output.
"""


class Department:
    """Simple class that gets embedded inside Employee -> this is "Combining Objects" """

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def __str__(self):
        return f"{self.name} (Budget: ${self.budget:,})"


class Employee:
    # TODO 1 (Static attribute): shared value across ALL employees, not per-instance
    company_name = "Aliens Inc."  # set to "CyberShield Inc."

    # TODO 2 (Static attribute): running total of employees created
    employee_count = 0

    def __init__(self, name, department: Department, salary, ssn):
        self.name = name                       # public attribute
        self.department = department           # combining objects
        self._years_of_service = 0             # TODO 3: make this protected (single underscore)
        self.__salary = None                    # TODO 4: private attribute (filled via the setter below)
        self.salary = salary                    # this will call the setter you write in TODO 7
        self.__ssn = self.__encrypt_ssn(ssn)    # private attribute + calling a private method

        # TODO 5: increment Employee.employee_count by 1
        Employee.employee_count += 1

    # ---------------- Property: salary getter/setter ----------------
    @property
    def salary(self):
        # TODO 6: return the private __salary value
        return self.__salary

    @salary.setter
    def salary(self, value):
        # TODO 7: if value <= 0, raise ValueError("Salary must be positive")
        # otherwise, store it in __salary
        if value <= 0:
            raise ValueError("Salary must be positive")
        else:
            self.__salary = value

    # ---------------- Protected method ----------------
    def _calculate_bonus(self):
        """
        Protected method: an implicit agreement that this is for internal use /
        meant to be overridden by subclasses (see SecurityAnalyst below).
        Default behavior: 5% of salary.
        """
        # TODO 8
        return self.__salary * 0.05

    # ---------------- Private method ----------------
    def __encrypt_ssn(self, ssn):
        """
        Private method (name-mangled): masks the national ID number.
        Example: replace every digit except the last 4 with '*'
        "29001011234567" -> "**********4567"
        """
        # TODO 9
        return  "*" * (len(ssn) - 4) + ssn[len(ssn) - 4:]

    # ---------------- Static method ----------------
    @staticmethod
    def is_valid_department_budget(budget):
        """Doesn't need self or cls -- just checks the number is positive"""
        # TODO 10
        return budget > 0

    def give_raise(self, percentage):
        # TODO 11: increase salary by a percentage -- use self.salary = ... (i.e. the setter)
        # do NOT touch __salary directly
        self.salary += self.salary * (percentage / 100)

    def __str__(self):
        return (f"{self.name} | {self.department.name} | "
                f"${self.salary:,.2f} | Bonus: ${self._calculate_bonus():,.2f}")


class SecurityAnalyst(Employee):
    """
    TODO 12 (Inheritance + Overriding a protected method):
    A security analyst gets a 10% bonus instead of 5% if they hold
    a certification (is_certified=True).
    """

    def __init__(self, name, department, salary, ssn, is_certified=False):
        super().__init__(name, department, salary, ssn)
        self.is_certified = is_certified

    def _calculate_bonus(self):
        # TODO 13: if is_certified, return 10% of salary
        # otherwise, fall back to the parent's behavior (you can call super()._calculate_bonus())
        if self.is_certified: 
            return self.salary * 0.1
        else:
            return super()._calculate_bonus()


# ========================= Tests =========================
if __name__ == "__main__":
    soc_dept = Department("Security Operations", 500_000)

    emp1 = Employee("Ahmed Hassan", soc_dept, 15000, "29001011234567")
    analyst1 = SecurityAnalyst("Sara Youssef", soc_dept, 22000, "29505051234567", is_certified=False)

    print(emp1)
    print(analyst1)

    print(f"Employee count (static attribute): {Employee.employee_count}")
    print(f"Company name (static attribute): {Employee.company_name}")

    try:
        emp1.salary = -500
    except ValueError as e:
        print(f"Negative salary correctly rejected: {e}")

    print(f"Is 10000 a valid budget? {Employee.is_valid_department_budget(10000)}")
    print(f"Is -500 a valid budget? {Employee.is_valid_department_budget(-500)}")

    emp1.give_raise(10)
    print(f"After raise: {emp1}")

    # Try accessing private/protected attributes from outside the class
    # (this is Python's "Consenting Adults" philosophy in action)
    print(emp1._years_of_service)     # works fine (but shouldn't be done in real code)
    # print(emp1.__salary)            # raises AttributeError (name mangling)
    print(emp1._Employee__salary)     # this works -- now you see the mangling in action
```

---

## 📄 الملف: `Week03\Learning\Python\exception_handling.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Learning\Python\exception_handling.py`

```python
# Day 12

class SecurityError(object):
    pass




def safe_divide(a, b):
    if a < 0:
        raise SecurityError("Negative numbers are not allowed in this operation.")
    try:
        divide = a / b 
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Invalid input type. Please enter numbers.")
        return None
    except SecurityError as e:
        print(e)
        return None
    else:
        print(f"Result: {divide}.")
        return divide
    finally:
        print("Division attempt finished.")


safe_divide(-2,5)
```

---

## 📄 الملف: `Week03\Learning\Python\OOP_everything.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Learning\Python\OOP_everything.py`

```python
# Exercising on everything i learnt in OOP
# Mini Home-Network Security Toolbox

from abc import ABC, abstractmethod

class NetworkDevice:
    total_devices = 0

    def __init__(self, name, ip_address, mac_address):
        self.name = name
        self._ip_address = ip_address
        self.__mac_address = mac_address
        self.last_log = None

        NetworkDevice.total_devices += 1

    @property
    def ip_address(self):
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self, new_value):
        if new_value.count(".") == 3 and new_value:
            self._ip_address = new_value
        else:
            raise ValueError("Wrong Ip address format.")

    def get_mac_address(self):
        return self.__mac_address
    
    def set_mac_address(self, new_value):
        if len(new_value) == 17:
            self.__mac_address = new_value
        else:
            raise ValueError("Wrong Mac address format.")
        
    @staticmethod
    def is_valid_ip(ip):
        if ip.count(".") == 3 and ip:
            return True
        return False
    
    @classmethod
    def from_string(cls, value):
        new_class = value.split(",")
        return cls(new_class[0], new_class[1], new_class[2])
    
    def __str__(self):
        return f"Name : '{self.name}', Ip address : '{self.ip_address}', Mac address : '{self.get_mac_address()}'"

    def __eq__(self, other):
        if self.get_mac_address() == other.get_mac_address():
            return True
        else:
            return False
        
    def update_log(self, timestamp, status):
        self.last_log = self.ConnectionLog(timestamp, status)
        
    def status_report(self):
        return f"All nice in NetworkDevice class"

    class ConnectionLog:
        def __init__(self, timestamp, status):
            self.timestamp = timestamp
            self.status = status

class Scannable(ABC):
    @abstractmethod
    def scan(self):
        pass

class Firewall:
    def __init__(self):
        self.blocked_ip = ["123.456.9.1"]

    def is_blocking(self, ip):
        if ip in self.blocked_ip:
            return True
        return False

class Laptop(NetworkDevice):
    def __init__(self, name, ip_address, mac_address, os_name):
        super().__init__(name, ip_address, mac_address)
        self.os_name = os_name

    def __str__(self):
        return super().__str__() + f", Os_name: '{self.os_name}'"
    
    def status_report(self):
        return f"Our os {self.os_name} is good."
    
class Router(NetworkDevice):
    def __init__(self, name, ip_address, mac_address):
        super().__init__(name, ip_address, mac_address)
        self.firewall = Firewall()

    def status_report(self):
        return f"Our router is nice."

class SmartCamera(NetworkDevice, Scannable):
    def __init__(self, name, ip_address, mac_address):
        super().__init__(name, ip_address, mac_address)

    def scan(self):
        return f"No thing is found."
    
    def status_report(self):
        return self.scan()
    
class NetworkMonitorDashboard:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def list_all(self):
        for device in self.devices:
            print(device)

def run_security_scan(devices):
    for device in devices:
        print(device.scan())
            

if __name__ == "__main__":
    laptop = Laptop("Hp-678", "134.928.1.4", "AA:CC:DDA", "win12")
    router = Router("We - Fast", "134.928.1.1", "AA:CC:DDC")
    smart_camera = SmartCamera("FHD Sony 4.8", "134.928.1.7", "AA:CC:DDD")
    from_string = NetworkDevice.from_string("New Phone,134.928.1.8,AA:CC:DDD:FF")
    laptop.update_log("10:20pm", "Connected")
    print(laptop.last_log.status)
    print(NetworkDevice.total_devices)
    devices = [laptop, router, smart_camera]
    for device in devices:
        print(device.status_report())

    NetworkMonitor = NetworkMonitorDashboard()
    for device in devices:
        NetworkMonitor.add_device(device)

    NetworkMonitor.list_all()
    run_security_scan(devices= [smart_camera])
    try:
        run_security_scan(devices= [laptop])
        error = Scannable()
    except Exception as e:
        pass
    new_laptop = Laptop("Hp-6788", "134.928.1.3", "AA:CC:DDA", "win12")
    print( new_laptop == laptop)


```

---

## 📄 الملف: `Week03\Learning\Python\password_entry.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Learning\Python\password_entry.py`

```python
# Day 13 (Added some in start of Week 4)

from datetime import datetime

class PasswordEntry:
    entry_count = 0
    
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password
        self.date_created = datetime.now().date()
        self.id = PasswordEntry.entry_count
        PasswordEntry.entry_count += 1

    def __str__(self):
        return f"{self.website} : {self.username}"
    
    def __repr__(self):
        return f"PasswordEntry('{self.website}', '{self.username}', '{self.password}')"
    
    def __eq__(self, other):
        return self.website == other.website
    
    def __lt__(self, other):
        return self.date_created < other.date_created
    
    def __len__(self):
        return len(self.password)
    
    def validate(self):
        if len(self.password) > 8:
            return True
        else:
            return False
        


```

---

## 📄 الملف: `Week03\Learning\Python\SecurityTool_experiment.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Learning\Python\SecurityTool_experiment.py`

```python
# Day 15 Exercise


class SecurityTool:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __str__(self):
        return f"{self.name} v{self.version}"
    
    def __repr__(self):
        return f"{type(self).__name__}('{self.name}', '{self.version}')"
    
    def run(self):
        raise NotImplementedError("Subclasses must implement its run().")
    
class Scanner(SecurityTool):
    def __init__(self, name, version, target):
        super().__init__(name, version)
        self.target = target

    def run(self):
        return f"Scanning {self.target}....."

class PortScanner(Scanner):
    def __init__(self, name, version, target, ports):
        super().__init__(name, version, target)
        self.ports = ports

    def run(self):
        return f"Scanning ports {self.ports} on {self.target}..."


p = PortScanner("Nmap", "7.0", "192.168.1.1", [22, 80, 443])

# 1. Test isinstance
print(isinstance(p, SecurityTool))  # True (لأن PortScanner ابن Scanner ابن SecurityTool)
print(isinstance(p, Scanner))       # True
print(isinstance(p, PortScanner))   # True

# 2. Test issubclass
print(issubclass(PortScanner, SecurityTool))  # True
print(issubclass(PortScanner, Scanner))       # False (الأب مش ابن لابنه)
    

```

---

## 📄 الملف: `Week03\Learning\Python\security_toolkit.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Learning\Python\security_toolkit.py`

```python
# PS0-C Day 16
from json import dumps,dump,load,JSONDecodeError

class SecurityToolkit:
    def __init__(self,name, version):
        self.name = name
        self.version = version
        self._logs = []
        
    def __str__(self):
        return f"{self.name} v{self.version}"
    
    def __repr__(self):
        return f"{type(self).__name__}('{self.name}', '{self.version}')"
    
    def __len__(self):
        return len(self.logs)
    
    @property
    def logs(self):
        return self._logs

    @logs.setter
    def logs(self, log):
        self._logs = log


    def scan(self, target):
        if not target:
            return None
        message = f"Scanning {target}..."
        self.log(message)
        print("Scanned.")

    def log(self, message):
        self.logs.append(message)
    
    def report(self, fmt="text"):
        if fmt == "text":
            return "\n".join(self.logs)
        elif fmt == "json":
            return dumps(self.logs, indent=4)

    def save_results(self, path):
        try:
            with open(path, "w") as f:
                dump(self.logs, f, indent=4)
        except IOError:
            print("An Error occured.")
            return False
        else:
            return True
        
    def load_results(self, path):
        try:
            with open(path, "r", encoding="UTF-8") as f:
                self.logs = load(f)
        except FileNotFoundError:
            print("The File not exist.")
            return False
        except JSONDecodeError:  # <--- ده المهم!
            print("Error: The file is empty or contains invalid JSON.")
            return False
        else:
            return True
        

tool = SecurityToolkit("Scanner", "3.2")

corrupt_file = "corrupt.json"
with open(corrupt_file, 'w') as f:
    f.write("This is NOT valid JSON! {")      
result = tool.load_results(corrupt_file)


```

---

## 📄 الملف: `Week03\Learning\Python\soc_incident_system.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Learning\Python\soc_incident_system.py`

```python
## Day 16 A-(Exercise everything i learnt in OOP)
# (https://www.youtube.com/watch?v=iLRZi0Gu8Go&t=4380s)

from json import dumps

class Analyst:
    def __init__(self, name, email):
        self.name = name
        self._email = email
        self._active_cases = []

    def assign_case(self, case):
        """
        Adds a case name to self._active_cases
        """
        self._active_cases.append(case)

    def get_email(self):
        "Return the self.email"
        return self._email
    
    def set_email(self, value):
        """
        Sets the self.email to the new value
        """
        if not "@" in value:
            raise ValueError("Invalid email.")
        self._email = value

class SecurityIncident:
    total_incidents_logged = 1
    organization_name = "Alien Inc."

    def __init__(self, incident_title, assigned_analyst): 
        self.incident_title = incident_title
        self._severity = None
        self.assigned_analyst = assigned_analyst
        self.__incident_id = self.__generate_incident_id()

        SecurityIncident.total_incidents_logged += 1

    @property
    def severity(self):
        return self._severity
    
    @property
    def incident_id(self):
        return self.__incident_id
    
    @severity.setter
    def severity(self, value):
        if not SecurityIncident.is_valid_severity(value):
            raise ValueError("Incorrect severity type.")
        self._severity = value

    def __generate_incident_id(self):
        return "INC-" + str(self.total_incidents_logged).zfill(4)
    
    @staticmethod
    def is_valid_severity(level):
        valid_values = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
        if level not in valid_values:
            return False
        return True
    
    # Review (Abstract methods)
    def _base_priority_score(self):
        priority = {"LOW": 2.0, "MEDIUM": 4.5, "HIGH": 7.5, "CRITICAL": 10}
        return priority[self.severity]
    
class PhishingIncident(SecurityIncident):
    def __init__(self, incident_title, assigned_analyst, num_emails_sent):
        super().__init__(incident_title, assigned_analyst)
        self.num_emails_sent = num_emails_sent

    def _base_priority_score(self):
        priority = {"LOW": 2.0, "MEDIUM": 4.5, "HIGH": 7.5, "CRITICAL": 10, "NONE": 0}
        self.assess_severity()
        return priority[self.severity]

    def assess_severity(self):
        if 0 <= self.num_emails_sent <= 50:
            self.severity = "LOW"
        elif 50 <= self.num_emails_sent <= 200:
            self.severity = "MEDIUM"
        elif 200 <= self.num_emails_sent <= 1000:
            self.severity = "HIGH"
        elif 1000 <= self.num_emails_sent:
            self.severity = "CRITICAL"
            
    def generate_report(self):
        return dumps([self._base_priority_score(), self.num_emails_sent])


class MalwareIncident(SecurityIncident):
    def __init__(self, incident_title, assigned_analyst, is_ransomware):
        super().__init__(incident_title, assigned_analyst)
        self.is_ransomware = is_ransomware

    def _base_priority_score(self):
        priority = {"LOW": 2.0, "MEDIUM": 4.5, "HIGH": 7.5, "CRITICAL": 10, "NONE": 0}
        self.assess_severity()
        return priority[self.severity]

    def assess_severity(self):
        if self.is_ransomware:
            self.severity = "HIGH"
        else:
            self.severity = "MEDIUM"

    def generate_report(self):
        return dumps(self._base_priority_score())



class UnauthorizedAccessIncident(SecurityIncident):
    def __init__(self, incident_title, assigned_analyst, affected_system):
        super().__init__(incident_title, assigned_analyst)
        self.affected_system = affected_system

    def _base_priority_score(self):
        priority = {"LOW": 2.0, "MEDIUM": 4.5, "HIGH": 7.5, "CRITICAL": 10, "NONE": 0}
        self.assess_severity()
        return priority[self.severity]

    def assess_severity(self):
        if "db" in self.affected_system.lower() or "admin" in (self.affected_system).lower():
            self.severity = "CRITICAL"
        else:
            self.severity = "MEDIUM"

    def generate_report(self):
        return dumps(self._base_priority_score())




    

```

---

## 📄 الملف: `Week03\Notes\Day11-12.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Notes\Day11-12.md`

```markdown
# Day 11 - W03 (04/07) - Debugging, Defensive Programming & Practice

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Error Types, Overt/Covert, Defensive Programming, `assert`, `try/except`, Debugging, Aliasing, Edge Cases

---

## 1. The 3 Main Error Types

| Type | What It Is | How to Spot |
|------|-----------|-------------|
| **Syntax** | Spelling mistakes (`If` instead of `if`, missing `:`) | Python stops immediately, red error |
| **Runtime** | Crashes while running (division by zero, file not found) | Exception thrown (`ValueError`, `FileNotFoundError`) |
| **Logic** | Code runs, but output is **wrong** | **Hardest to fix** — no error messages, test manually |

---

## 2. MIT Classifications (Security Perspective)

| Classification | Definition | Cybersecurity Example |
|---------------|-----------|----------------------|
| **Overt** | Visible — crashes or clear error | Web server returns `500 Internal Server Error` |
| **Covert** | **Silent** — runs "normally" but wrong | Antivirus marks malware as "safe" with no error ⚠️ |
| **Persistent** | Happens every time under same conditions | Firewall always blocks port 80 |
| **Intermittent** | Random, hard to reproduce | Sniffer drops packets only during peak traffic |

---

## 3. Defensive Programming

**Golden rule:** Never trust the user or the input.

- Assume the file is corrupted.
- Assume the user types letters when you asked for numbers.
- Assume the system clock is wrong.

> *Philosophy:* If something **can** go wrong, assume it **will**.

---

## 4. `assert` vs `try/except`

| Feature | `assert` | `try/except` |
|---------|---------|-------------|
| **Purpose** | Catches logic errors (developer mistakes) | Handles runtime errors (external factors) |
| **Behavior** | **Crashes** if condition fails | **Recovers** and continues |
| **Use Case** | "This value must never be negative here" | "This file might not exist" |

```python
# assert — for internal logic validation
assert ip_address, "IP cannot be empty"
assert 1 <= port <= 65535, f"Invalid port: {port}"
assert len(password) >= 8, "Password must be at least 8 characters"
```

---

## 5. Debugging Practice — 6 Functions Fixed

### Function 1: `remove_duplicates` (Aliasing)

**Bug:** `result = lst` — alias, mutates original.

**Fix:**
```python
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
```

**Takeaway:** Always copy when you need to preserve original data.

---

### Function 2: `get_average` (Mutable Default)

**Bug:** `def get_average(numbers, default=[])` — list persists between calls!

**Fix:** Remove mutable default: `def get_average(numbers):`

**Takeaway:** Never use `[]` or `{}` as default arguments.

---

### Function 3: `find_max_index` (Logic Error)

**Bug:** Logic looked for last "drop", not maximum value.

**Fix:**
```python
def find_max_index(lst):
    max_value = lst[0]
    max_idx = 0
    for i in range(len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
            max_idx = i
    return max_idx
```

**Takeaway:** Reset tracking variables correctly. Use `float('-inf')` if you don't want to rely on `lst[0]`.

---

### Function 4: `merge_dicts` (Aliasing)

**Bug:** `result = d1` — mutates `d1`.

**Fix:** `result = d1.copy()`

**Takeaway:** `.copy()` dictionaries when merging if you need originals.

---

### Function 5: `count_words` (Logic + `get` Trick)

**Bug:** Reset `counts[word] = 1` at end of loop, losing count.

**Fix:** `counts[word] = counts.get(word, 0) + 1`

**Takeaway:** `.get()` trick is now in the toolkit.

---

### Function 6: `is_sorted` (Index Error)

**Bug:** `range(len(lst))` → `IndexError` at last element (`lst[i+1]` out of bounds).

**Fix:** `range(len(lst) - 1)`

**Takeaway:** Check loop boundaries when accessing `i+1`.

---

## 6. Errors I Made Today

| Mistake | Why It Was Wrong | Correct Approach |
|---------|-----------------|----------------|
| Used alias `result = lst` | Mutated original list | `result = []` or `lst[:]` |
| Mutable default `[]` | Shared across function calls | Use `None` as default, create list inside |
| Off-by-one in loop | `IndexError` on last element | `range(len(lst) - 1)` when checking `i+1` |
| Reset count in loop | Lost accumulated frequency | `counts.get(word, 0) + 1` |

---

## 7. Key Lessons for Cybersecurity

1. **Aliasing is dangerous** — Mutating a blocklist loses original evidence.
2. **Silent errors are the enemy** — Test with edge cases (empty lists, negatives, duplicates).
3. **`print()` is your best friend** — Oldest and most reliable debugging tool.

---

## 8. Quick Cheat Sheet

```python
# Error Types
SyntaxError      # Code won't run
ValueError       # Wrong value type
FileNotFoundError # File missing
IndexError       # List index out of range
KeyError         # Dict key missing
ZeroDivisionError # Division by zero

# assert (development only)
assert condition, "message"

# try/except (production)
try:
    risky_operation()
except SpecificError as e:
    handle_error(e)

# Safe patterns
if key in dict: ...           # Check before access
dict.get(key, default)        # Safe lookup
lst[:]                        # Shallow copy
```

---

#### ✅ **Status:** W03 Day 1 Complete — Debugging, Defensive Programming, 6 Functions Fixed  
#### 🚀 **Next:** `os.walk` and file system automation.
----
# Day 12 - W03 (05/07) - Exception Handling & Custom Exceptions

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** `try/except/else/finally`, Built-in Exceptions, `raise`, Custom Exceptions, OOP Inheritance

---

## 1. The Complete `try` Block

```python
try:
    # Risky code
except SpecificError:
    # Runs ONLY if that error occurs
else:
    # Runs ONLY if NO error happened
finally:
    # Runs ALWAYS (cleanup: close files, connections)
```

| Block | When It Runs |
|-------|-------------|
| `try` | The risky code |
| `except` | Only if a specific error occurs |
| `else` | Only if NO errors occur |
| `finally` | Always — even if `return` is used |

---

## 2. Common Built-in Exceptions

| Exception | Why It Happens | Example |
|-----------|---------------|---------|
| `ValueError` | Wrong **value** (type is correct) | `int("hello")` |
| `TypeError` | Wrong **type** | `"5" + 5` |
| `KeyError` | Key not found in dict | `my_dict["missing"]` |
| `IndexError` | Index out of range | `my_list[10]` (list has 5 items) |
| `ZeroDivisionError` | Dividing by zero | `10 / 0` |

---

## 3. `raise` — Manual Trigger

```python
# Enforce business rules or security constraints
if a < 0:
    raise SecurityError("Negative numbers are not allowed.")
```

**Why use it?** To stop execution when a security rule is violated.

---

## 4. Custom Exceptions

```python
class SecurityError(Exception):
    pass

def safe_divide(a, b):
    try:
        if a < 0:
            raise SecurityError("Negative numbers not allowed.")
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Invalid input type.")
        return None
    except SecurityError as e:
        print(f"Security Error: {e}")
        return None
    else:
        print(f"Result: {result}")
        return result
    finally:
        print("Division attempt finished.")
```

### Why `class SecurityError(Exception):`?

**The Hierarchy:**
```
object
  └── BaseException
        └── Exception  ← Always inherit from this
              └── SecurityError  ← Your custom exception
```

**Rule:** If you inherit from `object` instead of `Exception`, you **cannot** `raise` it. Python requires exceptions to derive from `BaseException`.

### How `raise` Works

1. `SecurityError("msg")` → calls `__init__` (inherited from `Exception`), stores message
2. `raise` → stops execution, looks for matching `except`
3. `except SecurityError as e:` → catches it, `e` holds the message

**Security Use Cases:**
- `InvalidIPError` — malformed IP address
- `MaliciousFileError` — suspicious file detected
- `BlocklistViolationError` — blocked IP attempted access

---

## 5. Key Differences Summary

| Concept | Definition |
|---------|-----------|
| `try` | Block that might raise an exception |
| `except` | Runs if specific exception occurs |
| `else` | Runs if NO exceptions occur |
| `finally` | Runs regardless (cleanup) |
| `raise` | Manually triggers an exception |
| Custom Exception | Inherits from `Exception` for app-specific errors |

---

## 6. Quick Cheat Sheet

```python
# Full try block
try:
    result = risky_operation()
except ValueError as e:
    print(f"Bad value: {e}")
except (TypeError, KeyError) as e:
    print(f"Multiple errors: {e}")
else:
    print("Success!")
finally:
    cleanup()

# raise
raise ValueError("Invalid input")

# Custom exception
class MyError(Exception):
    pass

raise MyError("Something went wrong")
```

---

✅ **Status:** W03 Day 2 Complete — `try/except/else/finally`, Built-in Exceptions, `raise`, Custom Exceptions  
🚀 **Next:** File system automation (`os.walk`)
```

---

## 📄 الملف: `Week03\Notes\Day13-14.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Notes\Day13-14.md`

```markdown
# Day 13 - W03 (06/07) - OOP Basics: Classes, Objects, and `self`

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Classes, Objects, `__init__`, `self`, Instance Attributes, Class Variables, `__str__`, `__repr__`

---

## 1. Class vs Object

| Concept | Definition | Analogy |
|---------|-----------|---------|
| **Class** | Blueprint/template | Cookie-cutter |
| **Object** | Concrete instance | Actual cookie |

```python
class FirewallRule:           # Class (blueprint)
    pass

rule1 = FirewallRule()        # Object (instance)
rule2 = FirewallRule()        # Another object
```

---

## 2. The `__init__` Constructor

Runs **automatically** when creating an object. Initializes data.

```python
class ThreatAlert:
    def __init__(self, severity, source_ip):
        self.severity = severity      # instance attribute
        self.source_ip = source_ip

alert = ThreatAlert("HIGH", "10.0.0.99")
print(alert.severity)     # "HIGH"
```

---

## 3. Understanding `self`

- `self` = the **current instance**
- Python passes it automatically as the first argument
- Use it to access/modify the object's data

```python
class PasswordEntry:
    def __init__(self, website, username):
        self.website = website        # self = this specific object
        self.username = username

    def get_info(self):
        return f"{self.website}: {self.username}"   # access via self

e1 = PasswordEntry("gmail.com", "ahmed")
print(e1.get_info())      # "gmail.com: ahmed"
```

---

## 4. Class Variables vs Instance Variables

| Feature | Instance Variable | Class Variable |
|---------|------------------|----------------|
| Defined where? | Inside `__init__` via `self.attr` | Directly in class body |
| Belongs to | Specific object | Class (shared by ALL) |
| Changes affect | Only that object | All instances |
| Use case | Object-specific data | Counters, defaults, constants |

```python
class PasswordEntry:
    entry_count = 0           # class variable (shared)

    def __init__(self, website, username, password):
        self.website = website       # instance variable
        self.username = username
        self.password = password

        PasswordEntry.entry_count += 1   # increment shared counter
        self.id = PasswordEntry.entry_count   # assign unique ID

e1 = PasswordEntry("gmail.com", "ahmed", "pass123")
e2 = PasswordEntry("github.com", "ali", "secure456")

print(PasswordEntry.entry_count)   # 2
print(e1.id)                       # 1
print(e2.id)                       # 2
```

**Trap:** Code outside methods runs **once** when the file loads, not per object.

```python
class Wrong:
    count = 0
    count += 1        # Runs ONCE when class is defined — useless!
```

---

## 5. `__str__` vs `__repr__`

| Method | Called By | Purpose |
|--------|----------|---------|
| `__str__` | `print(obj)`, `str(obj)` | User-friendly output |
| `__repr__` | `repr(obj)`, interactive shell | Debug/recreate output |

```python
class PasswordEntry:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def __str__(self):
        return f"{self.website} : {self.username}"

    def __repr__(self):
        return f"PasswordEntry('{self.website}', '{self.username}', '{self.password}')"

e1 = PasswordEntry("gmail.com", "ahmed", "pass123")
print(e1)           # gmail.com : ahmed
print(repr(e1))     # PasswordEntry('gmail.com', 'ahmed', 'pass123')
```

---

## 6. Errors I Made Today

| Mistake | Why It Was Wrong | Correct Way |
|---------|-----------------|-------------|
| `entry_count += 1` outside `__init__` | Runs once on class load, not per object | Put it inside `__init__` |
| `self.entry_count += 1` | Creates instance variable, shadows class variable | `PasswordEntry.entry_count += 1` |
| Confusing `self.count` vs `Class.count` | `self.count` creates copy, doesn't update shared counter | Use `ClassName.variable` for class vars |

---

## 7. Quick Cheat Sheet

```python
# Class definition
class MyClass:
    class_var = 0               # class variable

    def __init__(self, x):
        self.x = x              # instance variable
        MyClass.class_var += 1  # update class variable

    def method(self):
        return self.x           # access via self

    def __str__(self):
        return f"Value: {self.x}"

    def __repr__(self):
        return f"MyClass({self.x})"

# Creating objects
obj = MyClass(10)
print(obj)                      # uses __str__
print(repr(obj))                # uses __repr__
print(MyClass.class_var)        # access class variable
```

---

#### **Status:** Day 1 Complete — Classes, Objects, `self`, Class/Instance Variables, `__str__`, `__repr__`  
#### **Next:** Getters, Setters, and Validation
---
# Day 14 - W03 (07/07) - Getters, Setters, Validation & Encapsulation

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Access Modifiers, Getters/Setters, `@property`, Validation, `datetime`, Encapsulation

---

## 1. Access Modifiers in Python

| Modifier | Syntax | Meaning |
|----------|--------|---------|
| **Public** | `self.name` | Accessible anywhere (default) |
| **Protected** | `self._name` | Convention: "Don't touch outside class" |
| **Private** | `self.__name` | Name mangling: `_ClassName__name` |

**Python Philosophy:** "We're all consenting adults." Python trusts you — use conventions responsibly.

---

## 2. Why Getters & Setters?

| Without | With |
|---------|------|
| `obj.password = "123"` — no validation | `obj.set_password("123")` — validated |
| Anyone can corrupt data | Controlled access, system stays valid |

**The Bouncer Analogy:**
- **Public attr** = Unlocked back door
- **Getter** = Bouncer checking IDs (safe read)
- **Setter** = Bouncer validating guests (safe write)

---

## 3. The Python Way: `@property`

```python
class PasswordEntry:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self._password = password       # protected

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if self._validate(value):
            self._password = value
        else:
            raise ValueError("Weak password!")

    def _validate(self, pwd):
        return (len(pwd) > 8 and 
                any(c.isdigit() for c in pwd) and 
                any(not c.isalnum() for c in pwd))

# Usage — looks like attribute, runs methods behind the scenes
e = PasswordEntry("gmail.com", "ahmed", "Strong1!")
e.password = "Weak"        # ValueError!
```

---

## 4. `datetime` Handling

```python
from datetime import datetime

# ✅ Correct: extract date from datetime
self.date_created = datetime.now().date()

# ❌ Wrong: passing datetime object to date()
self.date_created = datetime.date(datetime.now())   # TypeError!

# Calculate age in days
age = (datetime.now().date() - self.date_created).days
```

---

## 5. Complete PasswordEntry Class

```python
from datetime import datetime

class PasswordEntry:
    entry_count = 0

    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self._password = password
        self.date_created = datetime.now().date()
        self.id = PasswordEntry.entry_count
        PasswordEntry.entry_count += 1

    # --- Getters/Setters (Java-style) ---
    def get_password(self):
        return self._password

    def set_password(self, new_password):
        if self.validate_password(new_password):
            self._password = new_password
        else:
            raise ValueError("Weak password: >8 chars, digit + symbol required.")

    # --- Validation ---
    def validate_password(self, password):
        return (len(password) > 8 and 
                any(c.isdigit() for c in password) and 
                any(not c.isalnum() for c in password))

    def is_expired(self, days=90):
        age = (datetime.now().date() - self.date_created).days
        return age > days

    # --- String representation ---
    def __str__(self):
        return f"{self.website} : {self.username}"

    def __repr__(self):
        return f"PasswordEntry('{self.website}', '{self.username}', '***')"
```

---

## 6. The Danger of Bypassing

| Approach | Result |
|----------|--------|
| `e._password = "123"` | ⚠️ Bypasses validation — weak password accepted |
| `e.set_password("123")` | ✅ Validation runs — `ValueError` raised |

**Encapsulation is not about hiding data — it's about controlling how data changes to keep the system valid.**

---

## 7. Errors I Made Today

| Mistake | Why It Was Wrong | Correct Way |
|---------|-----------------|-------------|
| `datetime.date(datetime.now())` | `date()` expects 3 ints, not a datetime object | `datetime.now().date()` |
| Direct assignment `e._password = "123"` | Bypasses validation | Always use setter/interface |
| Confusing protected vs private | `_` is convention, `__` is enforced | Use `_` for internal, `__` only when necessary |

---

## 8. Quick Cheat Sheet

```python
# Access modifiers
self.public        # public
self._protected    # protected (convention)
self.__private     # private (name mangling)

# Java-style getters/setters
def get_attr(self): return self._attr
def set_attr(self, val): self._attr = val

# Pythonic @property
@property
def attr(self): return self._attr

@attr.setter
def attr(self, val): self._attr = val

# datetime
from datetime import datetime
now = datetime.now().date()          # today's date
delta = now - created_date           # timedelta object
delta.days                           # days difference
```

---

✅ **Status:** Day 13 Complete — Encapsulation, Validation, `@property`, `datetime`  
🚀 **Next:** Inheritance (`class Child(Parent)`), `super()`, Method Overriding
```

---

## 📄 الملف: `Week03\Notes\Day15-16.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Notes\Day15-16.md`

```markdown
# Day 15 - W03 (08/07) - Inheritance, `super()`, and Method Overriding

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Inheritance, Subclasses, `super()`, MRO, Method Overriding, `NotImplementedError`, `isinstance()`, `issubclass()`

---

## 1. What is Inheritance?

A **child class (subclass)** inherits all attributes and methods from a **parent class (superclass)**.

**Why use it:**
- **DRY:** Write logic once, reuse everywhere
- **Maintainability:** Fix parent = fix all children
- **"is-a" relationship:** A `Scanner` **is a** `SecurityTool`

---

## 2. The Hierarchy We Built

```
SecurityTool (Parent)
    └── Scanner (Child)
            └── PortScanner (Grandchild)
```

```python
class SecurityTool:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __str__(self):
        return f"{self.name} v{self.version}"

    def __repr__(self):
        # Dynamic: adapts to child class name
        return f"{type(self).__name__}('{self.name}', '{self.version}')"

    def run(self):
        # Forces children to implement this
        raise NotImplementedError("Subclasses must implement run().")

class Scanner(SecurityTool):
    def __init__(self, name, version, target):
        super().__init__(name, version)   # call parent's __init__
        self.target = target

    def run(self):
        return f"Scanning {self.target}....."

class PortScanner(Scanner):
    def __init__(self, name, version, target, ports):
        super().__init__(name, version, target)
        self.ports = ports

    def run(self):
        return f"Scanning ports {self.ports} on {self.target}..."
```

---

## 3. Key Components

### `super()` — The Parent Caller

```python
# Instead of repeating:
self.name = name
self.version = version

# Use super() to hand off to parent:
super().__init__(name, version)
```

**Result:** Cleaner, DRY code. Parent handles what it knows, child adds what it needs.

### `NotImplementedError` — The Contract

```python
def run(self):
    raise NotImplementedError("Subclasses must implement run().")
```

**Meaning:** *"Any child MUST override this, or the program crashes."* — Design contract.

### Method Overriding — The Lookup Chain

Python follows **MRO** (Method Resolution Order):
1. Check current class
2. Check parent (left to right)
3. Check grandparent

```python
p = PortScanner("Nmap", "7.0", "192.168.1.1", [22, 80, 443])
p.run()   # PortScanner.run() → found first → executed
```

---

## 4. `print` vs `return`

| `print` | `return` |
|---------|----------|
| Displays to console | Sends value back to caller |
| Returns `None` | Returns actual value |
| Can't store result | Can store, manipulate, report |

**Fix:** `run()` returns a string so output can be saved to file or sent to GUI.

---

## 5. `isinstance` and `issubclass`

```python
p = PortScanner("Nmap", "7.0", "192.168.1.1", [22, 80, 443])

# isinstance: object → class (or parent)
isinstance(p, SecurityTool)   # True
isinstance(p, Scanner)        # True
isinstance(p, PortScanner)    # True
isinstance(p, str)            # False

# issubclass: class → class
issubclass(PortScanner, SecurityTool)   # True
issubclass(Scanner, PortScanner)         # False
```

---

## 6. Pro-Tip: Dynamic `__repr__`

```python
# ❌ BAD (hardcoded)
def __repr__(self):
    return f"SecurityTool('{self.name}', '{self.version}')"
# Scanner inherits this → prints "SecurityTool(...)" WRONG

# ✅ GOOD (dynamic)
def __repr__(self):
    return f"{type(self).__name__}('{self.name}', '{self.version}')"
# PortScanner → "PortScanner(...)"
# Scanner → "Scanner(...)"
```

---

## 7. Errors I Made Today

| Mistake | Why It Was Wrong | Correct Way |
|---------|-----------------|-------------|
| Hardcoded class name in `__repr__` | Child prints parent's name | Use `type(self).__name__` |
| Using `print` instead of `return` | Can't use output programmatically | `return` the string |
| Forgetting `super().__init__()` | Missing parent attributes | Always call parent constructor |

---

## 8. Quick Cheat Sheet

```python
# Inheritance
class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)     # call parent __init__
        self.y = y

    def method(self):
        # override parent method
        return "child version"

# Force override
raise NotImplementedError("Must implement!")

# Check relationships
isinstance(obj, Class)      # obj is Class or subclass?
issubclass(Child, Parent)   # Child inherits from Parent?

# Dynamic class name
type(self).__name__         # gets actual class name
```

---

#### ✅ **Status:** Inheritance mastered — `super()`, overriding, `isinstance`, dynamic `__repr__`  
#### 🚀 **Next:** Dunder Methods (`__eq__`, `__lt__`, `__len__`, `__add__`) & Generators
---
# Day 16 - W03 (09/07) - PS0-C: SecurityToolkit Base Class

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Base Class Design, Encapsulation, File I/O, Error Handling, Dynamic `__repr__`  
> **Status:** ✅ Completed (8.8/10). Fixed critical edge-case bugs.

---

## 1. The Mission

Build a foundational `SecurityToolkit` class from scratch — parent for all future security tools.

**Requirements:**
- `__init__`, `__str__`, `__repr__`, `__len__`
- `scan(target)`, `log(message)`, `report(fmt)`
- `save_results(path)`, `load_results(path)`
- Proper error handling

---

## 2. Key Design Decisions

### Dynamic `__repr__`
```python
def __repr__(self):
    return f"{type(self).__name__}('{self.name}', '{self.version}')"
```
**Why:** Child classes inherit this — prints `PortScanner(...)` automatically, no override needed.

### Encapsulation with `@property`
```python
@property
def logs(self):
    return self._logs

@logs.setter
def logs(self, log):
    if not isinstance(log, list):
        raise TypeError("Logs must be a list.")
    self._logs = log
```
**Why:** Protects `_logs` from being set to string/int accidentally.

---

## 3. Critical Errors & Fixes

| Error | Bug | Fix |
|-------|-----|-----|
| **JSONDecodeError** | File exists but empty/corrupt → `json.load()` crashes | Added `except json.JSONDecodeError` |
| **Restrictive Setter** | Blocked empty lists → crashed on empty JSON `[]` | Check type only, allow empty lists |

---

## 4. The Golden Rule: `.load()` vs `.loads()`

| Function | Ends with `s`? | Input | Use Case |
|----------|---------------|-------|----------|
| `json.load` | ❌ No | File object `f` | Read JSON from file |
| `json.loads` | ✅ Yes | String `data` | Parse JSON from variable |

**Memory trick:**
- `load` = **F**ile (no 's', think 'F')
- `loads` = **S**tring (has 's', think 'S')

---

## 5. Production-Ready Code

```python
from json import dump, load, dumps, JSONDecodeError

class SecurityToolkit:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self._logs = []

    def __str__(self):
        return f"{self.name} v{self.version}"

    def __repr__(self):
        return f"{type(self).__name__}('{self.name}', '{self.version}')"

    def __len__(self):
        return len(self.logs)

    @property
    def logs(self):
        return self._logs

    @logs.setter
    def logs(self, log):
        if not isinstance(log, list):
            raise TypeError("Logs must be a list.")
        self._logs = log

    def scan(self, target):
        if not target:
            return None
        self.log(f"Scanning {target}...")

    def log(self, message):
        self.logs.append(message)

    def report(self, fmt="text"):
        if fmt == "text":
            return "\n".join(self.logs)
        elif fmt == "json":
            return dumps(self.logs, indent=4)

    def save_results(self, path):
        try:
            with open(path, "w") as f:
                dump(self.logs, f, indent=4)
        except IOError:
            print("An Error occurred.")
            return False
        return True

    def load_results(self, path):
        try:
            with open(path, "r", encoding="UTF-8") as f:
                self.logs = load(f)
        except FileNotFoundError:
            print("The file does not exist.")
            return False
        except JSONDecodeError:
            print("Error: Invalid JSON.")
            return False
        return True
```

---

## 6. Self-Assessment

**What went well:**
- Wrote entire class from memory under time pressure
- Applied OOP principles (Encapsulation, Abstraction)
- Used advanced features (`@property`, `type(self).__name__`)

**Lessons learned:**
1. Always test edge cases (empty file?)
2. Read the error message — `JSONDecodeError` tells you exactly what's wrong
3. `json.load` = File, `json.loads` = String

---

✅ **Status:** PS0-C Complete  
🚀 **Next:** Audit Week 1 (Review Phase 0)


```

---

## 📄 الملف: `Week03\Notes\OOP.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Notes\OOP.md`

```markdown
# Python OOP — From "What Is It?" to the Last Concept

One short explanation per idea, in teaching order, each with exactly
one easy example.

---

## 0. What is OOP?

**Object-Oriented Programming** is a way of organizing code around
**objects** — bundles of data and the behavior that belongs with that
data — instead of writing one long list of separate variables and
functions.

**Procedural style** (before OOP): data and functions are separate.
```python
name = "Rex"
age = 3

def describe(name, age):
    return f"{name} is {age} years old"
```

**OOP style**: the data and the function that uses it live together in
one unit.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old"
```

Why bother? Once you have many "things" in your program (dogs,
employees, network devices...), OOP keeps each thing's data and
behavior organized together, instead of scattered across loose
variables and functions that all need to be passed around manually.

---

## 1. Classes and Objects

A **class** is the blueprint. An **object** (instance) is one real
thing built from that blueprint.
```python
class Dog:
    pass

rex = Dog()      # rex is an object (instance) of class Dog
buddy = Dog()     # a completely separate object
```

## 2. Attributes, Methods, and `self`

**Attributes** = the data an object stores. **Methods** = functions
that belong to the class. **`self`** = "this particular object,"
automatically passed into every method.
```python
class Dog:
    def __init__(self, name):
        self.name = name        # attribute

    def bark(self):              # method
        return f"{self.name} says Woof!"

rex = Dog("Rex")
print(rex.bark())                # Rex says Woof!
```

## 3. Combining Objects

An object can hold another object as one of its attributes.
```python
class Engine:
    def start(self):
        return "Vroom!"

class Car:
    def __init__(self):
        self.engine = Engine()   # Car "has an" Engine

my_car = Car()
print(my_car.engine.start())     # Vroom!
```

## 4. Accessing and Modifying Object Data

By default, you can read and change an object's attributes directly
with a dot, from anywhere.
```python
rex.name = "Max"       # changed directly, no restrictions yet
print(rex.name)        # Max
```
This is convenient but risky — nothing stops you from setting a
nonsense value. That's the problem the next few concepts solve.

## 5. Protected Attributes (`_name`)

A single leading underscore is a **convention**: "please don't touch
this from outside the class." Python doesn't actually block it — it's
a signal, not a lock.
```python
class Dog:
    def __init__(self, name):
        self._name = name   # "protected" by convention only
```
**When to use it:** whenever the attribute is meant for internal use
or for subclasses, but you don't need to strictly forbid outside
access.

## 6. Private Attributes (`__name`) and "Consenting Adults"

A double leading underscore triggers **name mangling** — Python
renames it internally to `_ClassName__name`, making outside access
much harder (though never fully impossible).

Python's **"Consenting Adults"** philosophy: the language trusts
programmers to respect conventions rather than locking everything down
with strict enforcement like some other languages do.
```python
class Dog:
    def __init__(self, name):
        self.__name = name   # harder to reach from outside

d = Dog("Rex")
# d.__name        -> would raise an AttributeError
print(d._Dog__name)  # still technically reachable, but ugly on purpose
```
**Protected vs private, in short:** use protected (`_x`) for "internal,
but subclasses may still need it." Use private (`__x`) for "truly just
this class's business, nobody else should touch it."

## 7. Getters and Setters (Classic Style)

Plain methods used to read/write a value indirectly, so you can add
validation logic.
```python
class Dog:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0:
            raise ValueError("Age can't be negative")
        self.__age = value
```
**Why bother**, instead of just making the attribute public? Because
this way, nobody can sneak in a bad value (like a negative age) without
going through your check first.

## 8. Properties (`@property`)

The modern version of getters/setters — it looks like a normal
attribute from the outside, but still runs your validation code.
```python
class Dog:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age can't be negative")
        self._age = value

d = Dog(3)
d.age = 5        # looks like a plain attribute, but the setter runs
```
**Properties vs classic getters/setters:** same purpose (controlled
access), but properties use normal-looking dot syntax (`d.age = 5`)
instead of explicit method calls (`d.set_age(5)`) — cleaner to read
and write.

## 9. Static Attributes (Class Attributes)

A value shared by **every** object of the class, not copied per
instance — e.g. a running total.
```python
class Dog:
    total_dogs = 0            # shared by ALL dogs

    def __init__(self, name):
        self.name = name        # unique per dog (instance attribute)
        Dog.total_dogs += 1

Dog("Rex")
Dog("Max")
print(Dog.total_dogs)         # 2
```

## 10. Static Methods (`@staticmethod`)

A method that doesn't need `self` (or the class) at all — it's just a
regular function grouped inside the class because it's related.
```python
class Dog:
    @staticmethod
    def is_valid_name(name):
        return len(name) > 0

print(Dog.is_valid_name("Rex"))   # True, no Dog object needed
```
**When to use it:** anytime the logic doesn't need any of the object's
or class's own data to do its job.

## 11. Class Methods (`@classmethod`)

A method that receives the **class itself** (`cls`) instead of an
object. The most common use: an alternate way to build an object.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, text):
        name, age = text.split(",")
        return cls(name, int(age))

rex = Dog.from_string("Rex,3")
```

## 12. Protected and Private Methods

The same underscore rules from attributes also apply to methods.
`_helper()` signals "internal use"; `__helper()` gets name-mangled.
Often used for logic meant to be overridden by subclasses, or internal
steps the outside world shouldn't call directly.
```python
class Dog:
    def make_sound(self):
        return self._sound_effect()   # public method uses a helper

    def _sound_effect(self):           # protected helper
        return "Woof!"
```

## 13. Encapsulation

The umbrella principle behind everything from sections 5–12: keep data
and the methods that manage it bundled together, and hide internal
details so outside code can only interact through a safe, controlled
interface.

**Why it matters:** it prevents invalid states (like a negative age)
and lets you change how something works internally later without
breaking code that uses it — as long as the public interface stays the
same.

## 14. Abstraction

A class marked as **abstract** can never be turned into an object
directly — it only exists to define a contract: "every subclass of me
must implement these specific methods."
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Shape()   -> TypeError: can't instantiate an abstract class
```

## 15. Inheritance

A class can inherit attributes and methods from another class,
avoiding repeated code and modeling "is-a" relationships.
```python
class Animal:
    def eat(self):
        return "Eating..."

class Dog(Animal):     # Dog "is an" Animal
    pass

rex = Dog()
print(rex.eat())        # inherited from Animal
```

## 16. `super()`

Lets a subclass call its parent's version of a method — useful for
*extending* the parent's behavior instead of fully replacing it.
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # let Animal handle "name"
        self.breed = breed
```

## 17. Multiple Inheritance

A class can inherit from **more than one** parent class at once.
```python
class Swimmer:
    def swim(self):
        return "Swimming"

class Walker:
    def walk(self):
        return "Walking"

class Duck(Swimmer, Walker):    # gets both abilities
    pass
```

## 18. Polymorphism

Different classes can implement the *same* method name in their own
way, and you can call it on any of them without checking which type it
is first.
```python
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

for animal in [Cat(), Dog()]:
    print(animal.speak())   # each one speaks differently
```
**Small bonus tip:** you can use type hints to document that a list
should only contain one base type, e.g. `def inspect(vehicles: list[Vehicle])`
— Python won't enforce it at runtime, but it helps readers (and your
editor) understand the intent.

## 19. Duck Typing

"If it walks like a duck and quacks like a duck, treat it as a duck."
Python doesn't check an object's exact type before calling a method —
it just tries. If the method exists, it works; if not, you get a
natural `AttributeError`.
```python
def make_it_speak(thing):
    return thing.speak()   # works on ANY object with a .speak() method
```

## 20. Composition

One object **creates and owns** another object internally — the inner
object's life is tied to the outer one.
```python
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()   # Car creates its own Engine
```

## 21. Aggregation

One object **holds a reference** to other objects that already existed
on their own — the container doesn't own their lifecycle.
```python
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)   # song already existed before this

song1 = "Bohemian Rhapsody"        # created independently
my_playlist = Playlist()
my_playlist.add_song(song1)         # just referenced, not owned
```
**Composition vs aggregation, in short:** composition = "I made you,
you're mine." Aggregation = "I just know about you; you existed
before me and you'll exist after me."

## 22. Nested Classes

A class defined **inside** another class — usually a small helper
structure that only makes sense in that context.
```python
class Device:
    class LogEntry:
        def __init__(self, timestamp, status):
            self.timestamp = timestamp
            self.status = status

    def __init__(self):
        self.last_log = None

    def log(self, timestamp, status):
        self.last_log = Device.LogEntry(timestamp, status)
```

## 23. Magic (Dunder) Methods

Special methods surrounded by double underscores that let your objects
work with Python's built-in syntax (`print()`, `==`, etc.) instead of
needing custom-named methods for everything.
```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):                 # controls print(obj)
        return f"({self.x}, {self.y})"

    def __eq__(self, other):           # controls obj1 == obj2
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
print(p1)              # (1, 2)  <- uses __str__ automatically
```

---

## Conclusion: The Big Picture

Everything above builds toward four pillars:

| Pillar | Built from |
|---|---|
| **Encapsulation** | protected/private attributes & methods, getters/setters, properties |
| **Abstraction** | abstract classes (`ABC`, `@abstractmethod`) |
| **Inheritance** | inheritance, `super()`, multiple inheritance |
| **Polymorphism** | polymorphism, duck typing |

And two extra practical skills that sit alongside the four pillars:
**object relationships** (composition, aggregation, nested classes,
combining objects) and **class-level tools** (static attributes/
methods, class methods, magic methods) that make classes more powerful
and convenient to use.
```

---

## 📄 الملف: `Week03\Resources\resources.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week03\Resources\resources.md`

```markdown
## Resources for Week 03

- [Python Object Oriented Programming (OOP) - Full Course for Beginners](https://www.youtube.com/watch?v=iLRZi0Gu8Go)

- [Python Object Oriented Programming Full Course 🐍](https://www.youtube.com/watch?v=IbMDCwVm63M)

- [MIT 6.00.1x Study Notes](https://docs.google.com/document/d/1oMYRnogRrGgCtz-26E8hJYLp7Bm99JS1SP4lhdXvqpw/edit?usp=sharing)

```

---

## 📄 الملف: `Week04\Learning\Python\Binary_search_iter.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week04\Learning\Python\Binary_search_iter.py`

```python
# Day 21 (Binary Search iterative)

from math import log2

def binary_search_iter(target, lst):
    low = 0
    high = len(lst) - 1
    for _ in range(len(lst)):
        if low > high:
            return False
        
        mid = (low + high) // 2

        if lst[mid] == target:
            return True
        elif lst[mid] > target:
            high = mid - 1
        elif lst[mid] < target:
            low = mid + 1
    return False


lst = [1, 3, 5, 7, 9, 10, 12, 15, 17, 20]
for i in lst:
    print(binary_search_iter(i, lst = lst))
print("----------")
print(binary_search_iter(10, [1, 3, 5]))


```

---

## 📄 الملف: `Week04\Learning\Python\Binary_search_recursive.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week04\Learning\Python\Binary_search_recursive.py`

```python
# Day 21 (Binary Search recursive)

from random import randint


def binary_search_recursive(target, lst, high = None, low = 0):

    if high is None:
        high = len(lst) - 1
    if low > high:
        return False
    
    mid = (low + high) // 2

    if lst[mid] == target:
        return True
    
    if lst[mid] > target:
        return binary_search_recursive(target, lst, low = low , high = mid - 1)
    elif lst[mid] < target:
        return binary_search_recursive(target, lst, low = mid + 1, high = high)
        

lst = [1,3, 5, 7, 8, 9, 11, 13, 14 , 19 , 22, 25, 27 , 29 , 35, 55, 78, 80, 97, 101, 105, 107]
# for item in lst:
#     print(binary_search_recursive(item, lst, high= len(lst)))

print("----------")

for i in range(10):
    print(binary_search_recursive(randint(120, 1000), lst))


print(binary_search_recursive(5, []))
```

---

## 📄 الملف: `Week04\Learning\Python\Bubble_sort.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week04\Learning\Python\Bubble_sort.py`

```python
# Day 20 (Bubble sort)
from time import time
import random

def bubble_sort(lst):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(lst) - 1):
            if lst[i + 1] < lst[i]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                is_sorted = False

# start = time()
# bubble_sort([random.randint(1, 1000000) for _ in range(25000)])
# print("Bubble sort:")
# print(f"{time() - start:.7f}")

```

---

## 📄 الملف: `Week04\Learning\Python\generate_passwords.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week04\Learning\Python\generate_passwords.py`

```python
# Day 18 (Task 2)

import random
import string

def generate_passwords(count, length):
    n = length // 3
    for i in range(count):
        chars = "".join(random.choices(string.ascii_letters, k=n))
        digits = "".join(random.choices(string.digits, k=n))
        symbols = "".join(random.choices("!@$%^&*.", k=n))
        extra = []
        lst = [chars, digits, symbols]
        length_copy = length
        if length % 3 != 0:
            while length_copy > len(chars + digits + symbols):
                extra.append(random.choice(string.ascii_letters + string.digits + "!@$%^&*."))
                length_copy -= 1
        lst = list("".join(lst + extra))
        random.shuffle(lst)
        result = "".join(lst)
        yield result


```

---

## 📄 الملف: `Week04\Learning\Python\Linear_search.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week04\Learning\Python\Linear_search.py`

```python
# Day 21 (Linear Search)

def linear_search(target, lst):
    for item in lst:
        if item == target:
            print(f"The item '{target}' is in the list.")
            return True
    print(f"The item '{target}' isn't in the list.")
    return False


# linear_search(0, [9, 2, 15, 7, 1, 0])
```

---

## 📄 الملف: `Week04\Learning\Python\Merge_sort.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week04\Learning\Python\Merge_sort.py`

```python
# Day 20 (Merge sort)

from time import time
import random

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        return merging(merge_sort(lst[:len(lst) // 2]), merge_sort(lst[len(lst) // 2:]))
           
def merging(lst1, lst2):
    result = []
    j = 0
    i = 0
    while i < len(lst1) and j < len(lst2):
            if lst1[i] > lst2[j]:
                result.append(lst2[j])
                j += 1
            else:
                result.append(lst1[i])
                i += 1
    result.extend(lst1[i:] + lst2[j:])
    return result


# start = time()
# merge_sort([random.randint(1, 1000000) for _ in range(25000)])
# print("Merge Sort:")
# print(f"{time() - start:.2f}")

```

---

## 📄 الملف: `Week04\Learning\Python\read_lines.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week04\Learning\Python\read_lines.py`

```python
# Day 18 (Task 1)

def read_log_lines(filename):
    with open(filename, "r", encoding="UTF-8") as f:
        for file in f:
            yield file


# x = read_log_lines(r"D:\vs code\cybersecurity-roadmap\hello.txt")
# for i in range(1000):
#     print(next(x))

# print([line for line in open(r'D:\vs code\cybersecurity-roadmap\hello.txt', "r", encoding="UTF-8") if 'FAILED' in line])
```

---

## 📄 الملف: `Week04\Learning\Python\Selection_sort.py`
- **الامتداد**: `.py`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week04\Learning\Python\Selection_sort.py`

```python
# Day 20 (Selection sort)
from time import time
import random

def selection_sort(lst):
    lst_len = len(lst)
    for k in range(lst_len):
        flag = True
        smallest = k
        for i in range(k, len(lst) - 1):
            if lst[smallest] > lst[i + 1]:
                smallest = i + 1
                flag = False
        if flag:
            break
        lst[k] , lst[smallest] = lst[smallest], lst[k]


# start = time()
# selection_sort([random.randint(1, 1000000) for _ in range(25000)])
# print("Selection Sort: ")
# print(f"{time() - start:.2f}")

```

---

## 📄 الملف: `Week04\Notes\Day17-18.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week04\Notes\Day17-18.md`

```markdown
# W04 - Dunder Methods & Generators (Days 17-18)

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Dunder Methods, Operator Overloading, Generators, `yield`, Iterator vs Generator, Memory Efficiency

---

## Day 17 (Sat, 11 July): Advanced Dunder (Magic) Methods

### What Are Dunder Methods?

Special methods surrounded by double underscores `__method__`. They make your class behave like native Python types.

Instead of `entry.get_website()`, you write `entry == other` or `len(entry)`.

---

### Applied to `PasswordEntry`

#### 1. `__eq__` — Equality Comparison

```python
def __eq__(self, other):
    return self.website == other.website
```

- **Usage:** `entry1 == entry2`
- **Logic:** Compare `website` to check if entries are for the same site.
- **Benefit:** Search for a specific site's entry with `if entry == target_website`.

---

#### 2. `__lt__` — Less Than (for Sorting)

```python
def __lt__(self, other):
    return self.created_at < other.created_at
```

- **Usage:** `entry1 < entry2`, or `sorted(list_of_entries)`
- **Logic:** Compare `created_at` dates. Older entry = smaller.
- **Benefit:** Python sorts entries automatically from oldest to newest (or reverse with `reverse=True`).

---

#### 3. `__len__` — Length

```python
def __len__(self):
    return len(self.password)
```

- **Usage:** `len(entry)`
- **Logic:** Returns actual password length.
- **Benefit:** Check password length quickly without writing `len(entry.password)`.

---

#### 4. `__iter__` & `__next__` — Making an Iterator

```python
class PasswordVaultIterator:
    def __init__(self, entries):
        self.entries = entries
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.entries):
            raise StopIteration
        entry = self.entries[self.index]
        self.index += 1
        return entry
```

- **Usage:** `for entry in vault:` or `next(vault_iterator)`
- **Logic:** Makes `PasswordVault` iterable. Helper class holds `entries` and `index`, walks through one by one.

---

### The Golden Point

Adding `__lt__` lets Python do `sort()`, `min()`, and `max()` without writing complex comparison functions. This is **Operator Overloading** — one of Python OOP's most powerful features.

---

## Day 18 (Sun, 12 July): Generators — The Magic of `yield`

### `return` vs `yield`

| `return` | `yield` |
|----------|---------|
| Exits function permanently | Pauses function temporarily |
| Destroys all memory/state | Preserves variables in memory |
| Returns everything at once | Returns one item, resumes on next call |

---

### Application 1: `read_log_lines(filename)` — File Reader

**Problem:** Read a 10GB file line by line without crashing.

**Correct Logic:**
1. Open with `with open(...) as f` (auto-closes).
2. Use `for line in f` (reads line by line, not all at once).
3. `yield line` to hand over the line and wait.

```python
def read_log_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
```

**Result:** Memory usage stays constant (one line at a time), regardless of file size.

---

### Application 2: `generate_passwords(count, length)` — Password Generator

**Evolution of thinking:**

1. **First idea:** Split length by 3 to guarantee letters, numbers, and symbols.
2. **Mistake 1:** Used `random.sample` (no duplicates) — breaks for large lengths. **Fixed** with `random.choices` (allows duplicates).
3. **Mistake 2:** Built `lst` (final list) before adding `extra`, so extra characters were lost. **Fixed** by adding `extra` first, then building and shuffling `lst`.

**Final logic:** Generate parts → add extras → shuffle → `yield` password.

```python
import random
import string

def generate_passwords(count, length):
    for _ in range(count):
        letters = random.choices(string.ascii_letters, k=length // 3)
        digits = random.choices(string.digits, k=length // 3)
        symbols = random.choices(string.punctuation, k=length // 3)
        extra = random.choices(string.ascii_letters + string.digits + string.punctuation,
                               k=length - len(letters) - len(digits) - len(symbols))
        lst = letters + digits + symbols + extra
        random.shuffle(lst)
        yield "".join(lst)
```

---

### Memory Experiment (`sys.getsizeof`)

```python
import sys

# List comprehension (stores everything)
print(sys.getsizeof([x for x in range(1_000_000)]))  # Millions of bytes

# Generator expression (stores recipe only)
print(sys.getsizeof((x for x in range(1_000_000))))  # ~104 bytes (constant!)
```

**Why:** A generator keeps the "recipe," not the result. A list keeps all results in RAM.

---

### Extra: Generator Expression

Instead of writing `def` and `yield`, write in one line:

```python
gen = (line for line in open('file.log') if 'ERROR' in line)
```

Same functionality as a function, but suitable for simple operations without complex logic.

---

## Final Comparison: Custom Iterator vs Generator

| Feature | Custom Iterator (Class) | Generator (Function) |
|---------|------------------------|----------------------|
| **Definition** | Class with `__iter__` and `__next__` | Regular function with `yield` |
| **State** | Variables in `self` (lives as long as object exists) | Local variables (persist between `yield` calls) |
| **Complexity** | More code, manual `StopIteration` management | Simple, Python handles `StopIteration` behind the scenes |
| **Use Case** | When you need `reset()`, `peek()`, or complex data storage | For 90% of cases iterating over large datasets |

---

## Key Takeaways

1. **Dunder Methods** make your classes behave like native Python types (compare, sort, iterate).
2. **Generators** save RAM when dealing with massive datasets.
3. **`yield`** is your best friend for reading logs and network data in cybersecurity (you'll process huge logs daily).

---

✅ **Status:** W04 Complete — Dunder Methods, Generators, Memory Efficiency  
🚀 **Next:** W05 — Regex & Applied OOP

```

---

## 📄 الملف: `Week04\Notes\Day19.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week04\Notes\Day19.md`

```markdown
# Day 17 - W04 (13/07) - Big O Notation & Complexity Analysis

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Time Complexity, Space Complexity, Big O Hierarchy, Laws of Big O

---

## 1. What is Big O?

Mathematical way to describe **how fast an algorithm runs** (time) or **how much memory it uses** (space) as input size `n` grows.

**Core idea:** Ignore constants, focus on the **dominant term** (fastest-growing part).

**Why it matters in Cybersecurity:**
- O(n²) IDS scanning 10K logs = seconds
- O(n²) IDS scanning 100K logs = minutes/hours
- Choosing O(n log n) over O(n²) = tool works vs tool crashes

---

## 2. The Hierarchy (Fastest → Slowest)

| Complexity | Name | Speed | Example |
|------------|------|-------|---------|
| **O(1)** | Constant | 🚀 Fastest | `my_list[0]` |
| **O(log n)** | Logarithmic | ⚡ Very fast | Binary search |
| **O(n)** | Linear | ✅ Good | Single loop |
| **O(n log n)** | Linearithmic | 👍 Decent | Merge sort |
| **O(n²)** | Quadratic | 🐢 Slow | Nested loops |
| **O(2ⁿ)** | Exponential | 💀 Deadly | Naive Fibonacci |

---

## 3. Deep Dive with Examples

### O(1) — Constant
```python
def get_first(lst):
    return lst[0]   # 1 step, always
```

### O(n) — Linear
```python
def find_max(lst):
    max_val = lst[0]
    for num in lst:     # n times
        if num > max_val:
            max_val = num
    return max_val
```

### O(n²) — Quadratic (Nested Loops)
```python
def has_duplicates(lst):
    for i in lst:           # n
        for j in lst:       # n
            if i == j:
                return True
    return False
```

### O(log n) — Logarithmic (Divide by 2)
```python
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
```

### O(n log n) — Merge Sort
```python
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])    # log n divisions
    right = merge_sort(lst[mid:])
    return merge(left, right)       # n merges per level
```

### O(2ⁿ) — Exponential
```python
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)      # 2 branches per call
```

---

## 4. Laws of Big O

### Addition Rule (Sequential Steps)
```python
# O(n) + O(n²) = O(n²)
# Dominant term wins
```

### Multiplication Rule (Nested Loops)
```python
# O(n) * O(n) = O(n²)
for i in lst:       # n
    for j in lst:   # n
        print(i, j)
```

---

## 5. My Functions Analyzed

| Function | Complexity | Why |
|----------|-----------|-----|
| `factorial(n)` | O(n) | Loop 1 to n |
| `linear_search(lst, target)` | O(n) | Scan each element |
| `binary_search(lst, target)` | O(log n) | Halve each iteration |
| `remove_duplicates` (no set) | O(n²) | `.count()` inside loop |
| `bubble_sort(lst)` | O(n²) | Nested loops |
| `merge_sort(lst)` | O(n log n) | Divide + merge |

---

## 6. Measuring Time

```python
import time

def measure(func, data):
    start = time.time()
    func(data)
    return time.time() - start

# O(n²) vs O(n log n) — gap grows fast as n increases
```

---

## 7. Quick Cheat Sheet

| Operation | Big O |
|-----------|-------|
| Index access `lst[i]` | O(1) |
| List search `x in lst` | O(n) |
| Dict access `d[key]` | O(1) |
| List sort `.sort()` | O(n log n) |
| Nested loops | O(n²) |
| Binary search | O(log n) |

---

## 8. Key Takeaway

> **Recognize when you're writing O(n²) and ask: can I optimize to O(n log n) or O(n)?**

---

✅ **Status:** Day 17 Complete — Big O mastered  
🚀 **Next:** Sorting Algorithms (Bubble, Selection, Merge)

```

---

## 📄 الملف: `Week04\Notes\Day20.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week04\Notes\Day20.md`

```markdown
# Day 20 - W05 (14/07) - Sorting Algorithms

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Bubble Sort, Selection Sort, Merge Sort, Divide and Conquer, Recursion, Two Pointers

---

## 1. Bubble Sort

### Idea
Compare every two adjacent elements. If left > right, swap them. After each pass, the largest element "bubbles" to the end.

```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst
```

### Complexity

| Case | Time |
|------|------|
| Best | O(n) *(with optimization)* |
| Average | O(n²) |
| Worst | O(n²) |

**Space:** O(1)

### Pros & Cons
- ✅ Easy to understand
- ❌ Very slow for large datasets

---

## 2. Selection Sort

### Idea
Find the smallest element, swap it with the first unsorted position. Repeat until sorted.

```python
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst
```

### Complexity

| Case | Time |
|------|------|
| Best | O(n²) |
| Average | O(n²) |
| Worst | O(n²) |

**Space:** O(1)

### Pros & Cons
- ✅ Fewer swaps than Bubble Sort
- ❌ Still O(n²), scans remaining list every iteration

---

## 3. Merge Sort — Divide and Conquer

### Main Idea
Instead of sorting a large list directly:
1. Divide into two halves
2. Keep dividing until every list has one element
3. Merge sorted lists back together

```python
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Complexity

| Case | Time |
|------|------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |

**Space:** O(n)

### Why O(n log n)?
- `log n` = number of times we divide the list
- `n` = during every merge level we visit every element once
- Total: `O(n log n)`

---

## 4. Recursion Essentials

Every recursive function needs:

### Base Case
```python
if len(lst) <= 1:
    return lst
```
Without it → infinite calls → `RecursionError`

### Recursive Case
```python
left = merge_sort(lst[:mid])
right = merge_sort(lst[mid:])
return merge(left, right)
```

---

## 5. Two Pointers Technique

Instead of `pop(0)` (slow, shifts elements):

```python
i = j = 0
while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1
```

**Advantages:**
- Faster (no element shifting)
- Cleaner implementation
- O(1) extra space per merge step

---

## 6. Algorithm Comparison

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) |
| Selection | O(n²) | O(n²) | O(n²) | O(1) |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) |

---

## 7. Interview Notes

| Algorithm | Key Points |
|-----------|-----------|
| **Bubble** | Adjacent swaps; optimize with swap flag |
| **Selection** | Finds minimum each pass; fewer swaps |
| **Merge** | Divide and Conquer; recursion; extra memory; best for large datasets |

---

## 8. Errors I Made Today

| Mistake | Why It Was Wrong | Correct Way |
|---------|-----------------|-------------|
| Used `pop(0)` in merge | Shifts all elements → O(n) per pop | Use Two Pointers (`i`, `j`) |
| Forgot to return merged list | Function returns `None` | Always `return result` |
| Thought Two Pointers were complex | Actually simpler than `pop(0)` | Just increment indices |

---

## 9. Quick Cheat Sheet

```python
# Bubble Sort
for i in range(n):
    for j in range(n - i - 1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

# Selection Sort
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if lst[j] < lst[min_idx]:
            min_idx = j
    lst[i], lst[min_idx] = lst[min_idx], lst[i]

# Merge Sort
def merge_sort(lst):
    if len(lst) <= 1: return lst
    mid = len(lst) // 2
    return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))

def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result
```

---

✅ **Status:** Day 20 Complete — Bubble, Selection, Merge Sort, Recursion, Two Pointers  

```

---

## 📄 الملف: `Week04\Notes\Day21.md`
- **الامتداد**: `.md`
- **المسار الكامل**: `D:\vs code\cybersecurity-roadmap\Phase-0\Month-1\Week04\Notes\Day21.md`

```markdown
# Day 21 - W06 (15/07) - Search Algorithms

> **Track:** Cybersecurity Python Fundamentals  
> **Topics:** Linear Search, Binary Search (Iterative & Recursive), Best Practices

---

## 1. Linear Search

### Idea
Check every element one by one until target is found or list ends.

```python
def linear_search(lst, target):
    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1
```

### Complexity
- **Best:** O(1) — target is first element
- **Worst:** O(n) — target is last or missing

### Pros & Cons
- ✅ Works on sorted and unsorted lists
- ✅ Very simple
- ❌ Slow for large datasets

---

## 2. Binary Search

### Idea
Only works on **sorted** lists. Remove half the search space every iteration.

```
[1, 3, 5, 7, 9, 11, 13]
         ^
        mid
```
- target < mid → search left
- target > mid → search right

### Why Must the List Be Sorted?
Binary Search decides "go left" or "go right" based on comparison. If unsorted, this decision is meaningless.

```
[9, 2, 15, 7, 1]   # unsorted — Binary Search fails
```

---

## 3. Iterative Binary Search

```python
def binary_search(lst, target):
    low, high = 0, len(lst) - 1

    while low <= high:          # while search space exists
        mid = (low + high) // 2

        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            low = mid + 1       # search right half
        else:
            high = mid - 1      # search left half

    return False                # search space disappeared
```

### Key Insight
> **Stop when the search space disappears (`low > high`), not when you decide a number of iterations.**

---

## 4. Recursive Binary Search

Same logic, different implementation.

```python
def binary_search_recursive(lst, target, low=0, high=None):
    if high is None:
        high = len(lst) - 1

    if low > high:              # base case: empty search space
        return False

    mid = (low + high) // 2

    if lst[mid] == target:
        return True
    elif lst[mid] < target:
        return binary_search_recursive(lst, target, mid + 1, high)
    else:
        return binary_search_recursive(lst, target, low, mid - 1)
```

---

## 5. Best Practices

### ✅ Pass indices, not slices
```python
# BAD: creates new list every call
binary_search(lst[:mid], target)

# GOOD: pass low/high indices
binary_search(lst, target, low, mid - 1)
```

### ✅ Use `is None` for defaults
```python
if high is None:      # correct
if high == None:      # avoid (works but not Pythonic)
```

### ✅ Flatten after return
```python
# BAD
if condition:
    return True
else:
    do_something()

# GOOD
if condition:
    return True

do_something()        # no else needed after return
```

### ✅ Don't use `while True`
```python
# BAD — hides the real stopping condition
while True:
    if low > high:
        break

# GOOD — condition is explicit
while low <= high:
    ...
```

---

## 6. Common Mistakes

| Mistake | Why It's Wrong |
|---------|---------------|
| `while True` | Hides real stopping condition |
| `for range(len(lst))` | Binary Search doesn't know iteration count |
| `log2()` for iterations | Algorithm decides when to stop, not you |
| Slicing `lst[:mid]` | O(n) memory per call — kills performance |
| Special conditions like `high == 0` | Trust the algorithm: `low > high` is enough |

---

## 7. Comparison

| Algorithm | Requires Sorted | Best | Worst | Use Case |
|-----------|----------------|------|-------|----------|
| Linear | No | O(1) | O(n) | Small/unsorted data |
| Binary | Yes | O(1) | O(log n) | Large sorted data |

---

## 8. Quick Cheat Sheet

```python
# Linear Search
for i, item in enumerate(lst):
    if item == target:
        return i
return -1

# Binary Search (Iterative)
low, high = 0, len(lst) - 1
while low <= high:
    mid = (low + high) // 2
    if lst[mid] == target: return True
    elif lst[mid] < target: low = mid + 1
    else: high = mid - 1
return False

# Binary Search (Recursive)
if low > high: return False
mid = (low + high) // 2
if lst[mid] == target: return True
elif lst[mid] < target:
    return binary_search(lst, target, mid + 1, high)
else:
    return binary_search(lst, target, low, mid - 1)
```

---

## 9. Key Takeaway

> **The algorithm stops because the search space disappeared (`low > high`), not because we decided on a number of iterations.**

---

✅ **Status:** Day 21 Complete — Linear Search, Binary Search (Iterative & Recursive)  

```

---


✅ **الإجمالي**: تم تجميع 44 ملف بنجاح (تم تخطي مجلدات وملفات Git).
