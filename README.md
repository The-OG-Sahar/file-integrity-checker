

# Simple File Integrity Checker

## Description

This is a beginner-friendly cybersecurity project that checks if files have been modified.
It calculates a SHA-256 hash for each file and compares it with previous hashes to detect changes automatically.
This project demonstrates a real cybersecurity concept in a simple and easy-to-understand way.

---

## Scripts / Files

* **`check_file.py`** → Optional: prints the SHA-256 hash of a file.
* **`check_integrity.py`** → Main program: detects file modifications automatically.
* **`hashes.txt`** → Stores SHA-256 hashes for future comparisons (created automatically).
* **`check_log.txt`** → Logs all file checks with timestamps.

---

## Features

* Check a single file or all `.py` files in the folder.
* Detects file modifications reliably using SHA-256.
* Logs every check for tracking purposes.
* Friendly menu and clear messages for easy use.
* Fully beginner-friendly and expandable.

---

## How to Run

### Open Command Prompt

* Press `Windows + R`, type `cmd`, and press Enter.
* Or search for **Command Prompt** in the Start menu.

### Navigate to your project folder

Type the command below and press Enter:

```text
cd C:\Users\Dell\Desktop\cybersecrity-project
```

### Run the program

Type the command below and press Enter:

```bash
python check_integrity.py
```

### Follow the menu

Example:

* `1` → Check a single file
* `2` → Check all `.py` files in folder
* `3` → Exit

If you select `1`, enter the file name when prompted.

---

## Example Output

```text
=== Simple File Integrity Checker ===

Menu:
1. Check a single file
2. Check all .py files in folder
3. Exit
Enter choice (1/2/3): 1
Enter file name: check_file.py
⚠️ 'check_file.py' has been MODIFIED!
```

Legend:

* ✅ unchanged → File is safe
* ⚠️ modified → File has been changed
* ℹ️ first check → Hash saved for the first time

---

## Requirements

* Python 3.x installed on your computer

---
 