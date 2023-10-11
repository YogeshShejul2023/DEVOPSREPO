def check_password_strength(password):
    # Check minimum length
    if len(password) < 8:
        return False

    # Check for uppercase and lowercase letters
    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        return False

    # Check for at least one digit (0-9)
    if not any(c.isdigit() for c in password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#\$%]', password):
        return False

    return True

# Get user input for a password
user_password = input("Enter a password: ")

# Check password strength
if check_password_strength(user_password):
    print("Password is strong and meets the criteria.")
else:
    print("Password is weak. Please choose a stronger password.")
