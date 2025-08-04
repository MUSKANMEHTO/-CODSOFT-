"""
password_generator.py

A professional command-line password generator that allows users
to specify password length and complexity. It generates secure,
random passwords using standard Python libraries.

Author: Muskan (You 💫)
"""

import random
import string


def get_password_preferences() -> dict:
    """
    Prompt the user for password preferences including length and character types.

    Returns:
        dict: A dictionary with user preferences.
    """
    print("🔐 [ Password Generator Setup ]")
    while True:
        try:
            length = int(input("Enter desired password length (min 4): "))
            if length < 4:
                print("⚠️ Please enter a value 4 or above.")
                continue
            break
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

    print("\nInclude character types:")
    use_uppercase = input("Include uppercase letters? (Y/N): ").strip().lower() == "y"
    use_lowercase = input("Include lowercase letters? (Y/N): ").strip().lower() == "y"
    use_digits = input("Include digits? (Y/N): ").strip().lower() == "y"
    use_symbols = input("Include special characters? (Y/N): ").strip().lower() == "y"

    if not (use_uppercase or use_lowercase or use_digits or use_symbols):
        print("❌ At least one character type must be selected.")
        return get_password_preferences()

    return {
        "length": length,
        "uppercase": use_uppercase,
        "lowercase": use_lowercase,
        "digits": use_digits,
        "symbols": use_symbols
    }


def generate_password(prefs: dict) -> str:
    """
    Generate a password based on the provided preferences.

    Args:
        prefs (dict): Dictionary containing password length and character type booleans.

    Returns:
        str: The generated password.
    """
    character_pool = ""

    if prefs["uppercase"]:
        character_pool += string.ascii_uppercase
    if prefs["lowercase"]:
        character_pool += string.ascii_lowercase
    if prefs["digits"]:
        character_pool += string.digits
    if prefs["symbols"]:
        character_pool += string.punctuation

    if not character_pool:
        return "❌ Error: No character types selected."

    password = ''.join(random.choices(character_pool, k=prefs["length"]))
    return password


def main():
    """
    Main function to run the password generator application.
    """
    print("\n🧠 [ Strong Password Generator ]\n")
    preferences = get_password_preferences()
    password = generate_password(preferences)

    print("\n🔒 Your Secure Password:")
    print(f"[ {password} ]\n")


if __name__ == "__main__":
    main()
