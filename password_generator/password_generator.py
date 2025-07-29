import random
import string


def generate_password(length=12):
    # length (int): Length of the password (default 12).

    if length < 4:
        raise ValueError(
            "Password length should be at least 4 to include all character types.")

    # Define character sets
    uppercase_letters = string.ascii_uppercase  # A-Z
    lowercase_letters = string.ascii_lowercase  # a-z
    digits = string.digits                      # 0-9
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/"  # Common special chars

    # Ensure password has at least one char from each category
    password_chars = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with a mix of all characters
    all_chars = uppercase_letters + lowercase_letters + digits + special_chars
    password_chars += random.choices(all_chars, k=length - 4)
    # Add remaining random characters to meet the desired password length.
    # We already included 1 uppercase, 1 lowercase, 1 digit, and 1 special character (total 4),
    # so we need (length - 4) more characters to complete the password.

    # Shuffle the characters to avoid predictable patterns
    random.shuffle(password_chars)

    # Join list to make a string
    password = "".join(password_chars)
    return password


if __name__ == "__main__":
    length = int(input("Enter desired password length (minimum 4): "))
    try:
        strong_password = generate_password(length)
        print("Generated password:", strong_password)
    except ValueError as e:
        print("Error:", e)
    # as e means store the error message inside the variable 'e'
    # Then you can print the error message using print("Error:", e)
