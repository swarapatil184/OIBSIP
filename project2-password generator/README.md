# 🔐 Random Password Generator (CLI)

A beginner-friendly yet powerful **command-line password generator** written in Python.
This tool allows users to create secure, customizable passwords with options for length, character types, exclusions, and strength checking.

---

##  Features

* Generate strong random passwords
* Custom password length (6–64 characters)
* Choose character types:

  * Letters (a-z, A-Z)
  * Numbers (0-9)
  * Symbols (!@#$%^&*...)
* Exclude specific characters (e.g., `l`, `1`, `O`, `0`)
* Generate multiple passwords at once (up to 10)
* Built-in password strength checker
* Optional clipboard copy support
* Input validation for better user experience

---

##  Requirements

* Python 3.x

(Optional)

* `pyperclip` (for clipboard functionality)

Install optional dependency:

```bash
pip install pyperclip
```

---

##  How to Run

1. Clone or download this repository
2. Navigate to the project folder
3. Run the script:

```bash
python password_generator.py
```

---

##  Example Usage

```
==================================================
      RANDOM PASSWORD GENERATOR
==================================================

--- Password Settings ---
  Enter password length [6-64]: 12
  Include letters (a-z, A-Z)? (y/n): y
  Include numbers (0-9)? (y/n): y
  Include symbols (!@#$ ...)? (y/n): y
  Exclude specific characters: l1O0
  How many passwords to generate? [1-10]: 3

--------------------------------------------------
  Generated Password(s):
--------------------------------------------------
  [1]  A$9f!2Xk@Qw3   |  Strength: Strong ✅
  [2]  mP#8Zx!4Tq2@   |  Strength: Strong ✅
  [3]  B7@kL!9vX#2p   |  Strength: Strong ✅
--------------------------------------------------
```

---

##  Password Strength Criteria

The password strength is evaluated based on:

* Length (≥8 and ≥12 characters)
* Use of lowercase letters
* Use of uppercase letters
* Use of numbers
* Use of symbols

| Score | Strength |
| ----- | -------- |
| 0–2   | Weak ⚠   |
| 3–4   | Medium ✔ |
| 5–6   | Strong ✅ |

---

##  Security Note

This project uses Python's built-in `random` module.
For production-level security, it is recommended to switch to the `secrets` module for cryptographically secure random generation.


##  Project Structure

```
password_generator.py   # Main script
README.md               # Project documentation
-

Future Improvements

* Use `secrets` module for stronger security
* Add GUI version (Tkinter / PyQt)
* Export passwords to file
* Add password history
* Improve strength checker (entropy-based)


Built as part of a Python learning journey to practice:

* Functions
* Input validation
* Loops and conditionals
* String manipulation




