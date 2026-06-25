import re

def check_password_strength(password):
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1

    # Check numbers
    if re.search(r"\d", password):
        score += 1

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength

# User Input
password = input("Enter a password: ")

strength = check_password_strength(password)

print("\nPassword Strength:", strength)
