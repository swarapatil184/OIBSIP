"""
Random Password Generator - Command Line Version (Beginner)
Python Programming Project 3
"""

import random
import string


# ─── Character Sets ────────────────────────────────────────────────────────────
LETTERS   = string.ascii_letters          # a-z A-Z
NUMBERS   = string.digits                 # 0-9
SYMBOLS   = "!@#$%^&*()-_=+[]{}|;:,.<>?" # special characters


def generate_password(length: int, use_letters: bool,
                      use_numbers: bool, use_symbols: bool,
                      exclude_chars: str = "") -> str:
    """
    Generate a random password based on user preferences.
    """
    # Build the character pool
    pool = ""
    if use_letters:
        pool += LETTERS
    if use_numbers:
        pool += NUMBERS
    if use_symbols:
        pool += SYMBOLS

    # Remove any excluded characters
    for ch in exclude_chars:
        pool = pool.replace(ch, "")

    if not pool:
        raise ValueError("No characters available! Please select at least one character type.")

    # Make sure password has at least one char from each selected type
    password_chars = []
    if use_letters and any(c in pool for c in LETTERS):
        password_chars.append(random.choice([c for c in LETTERS if c in pool]))
    if use_numbers and any(c in pool for c in NUMBERS):
        password_chars.append(random.choice([c for c in NUMBERS if c in pool]))
    if use_symbols and any(c in pool for c in SYMBOLS):
        password_chars.append(random.choice([c for c in SYMBOLS if c in pool]))

    # Fill remaining length from pool
    remaining = length - len(password_chars)
    password_chars += random.choices(pool, k=remaining)

    # Shuffle so guaranteed chars aren't always at the start
    random.shuffle(password_chars)

    return "".join(password_chars)


def check_strength(password: str) -> str:
    """Rate the strength of a password."""
    score = 0
    if len(password) >= 8:  score += 1
    if len(password) >= 12: score += 1
    if any(c in LETTERS.lower() for c in password): score += 1
    if any(c in LETTERS.upper() for c in password): score += 1
    if any(c in NUMBERS for c in password):         score += 1
    if any(c in SYMBOLS for c in password):         score += 1

    if score <= 2:   return "Weak   ⚠"
    elif score <= 4: return "Medium ✔"
    else:            return "Strong ✅"


def get_yes_no(prompt: str) -> bool:
    """Ask a yes/no question and return True/False."""
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ('y', 'yes'):
            return True
        elif answer in ('n', 'no'):
            return False
        else:
            print("  ✗ Please enter y or n.")


def get_int(prompt: str, min_val: int, max_val: int) -> int:
    """Get an integer within a range."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"  ✗ Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("  ✗ Invalid input. Please enter a whole number.")


# ─── Main Program ──────────────────────────────────────────────────────────────
def main():
    print("=" * 50)
    print("      RANDOM PASSWORD GENERATOR")
    print("=" * 50)

    while True:
        print("\n--- Password Settings ---")

        # Step 1: Length
        length = get_int("  Enter password length [6-64]: ", 6, 64)

        # Step 2: Character types
        use_letters = get_yes_no("  Include letters (a-z, A-Z)?")
        use_numbers = get_yes_no("  Include numbers (0-9)?")
        use_symbols = get_yes_no("  Include symbols (!@#$ ...)?")

        if not (use_letters or use_numbers or use_symbols):
            print("\n  ✗ You must select at least one character type!")
            continue

        # Step 3: Exclude characters
        exclude = input("  Exclude specific characters (leave blank to skip): ").strip()

        # Step 4: How many passwords
        count = get_int("  How many passwords to generate? [1-10]: ", 1, 10)

        # ── Generate ──────────────────────────────────────────────────────────
        print(f"\n{'─'*50}")
        print(f"  Generated Password(s):")
        print(f"{'─'*50}")

        generated = []
        for i in range(1, count + 1):
            try:
                pwd = generate_password(length, use_letters,
                                        use_numbers, use_symbols, exclude)
                strength = check_strength(pwd)
                print(f"  [{i}]  {pwd}   |  Strength: {strength}")
                generated.append(pwd)
            except ValueError as e:
                print(f"  ✗ Error: {e}")
                break

        print(f"{'─'*50}")

        # Step 5: Copy to clipboard (no external libraries needed)
        if generated:
            try:
                import subprocess, sys
                choice_str = input(
                    f"\n  Enter password number to copy [1-{len(generated)}] or press Enter to skip: "
                ).strip()
                if choice_str.isdigit():
                    idx = int(choice_str) - 1
                    if 0 <= idx < len(generated):
                        selected = generated[idx]
                        # Try pyperclip if available, otherwise show manual copy message
                        try:
                            import pyperclip
                            pyperclip.copy(selected)
                            print(f"  ✔ Password copied to clipboard!")
                        except ImportError:
                            print(f"\n  Selected password:  {selected}")
                            print("  (Select the text above and copy manually)")
            except Exception:
                pass

        # Step 6: Go again?
        again = get_yes_no("\n  Generate more passwords?")
        if not again:
            print("\n  Stay safe and use strong passwords! Goodbye.\n")
            break


if __name__ == "__main__":
    main()
