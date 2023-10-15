# Function to check the password strength
def check_password_strength(password):
    # Check the minimum length
    if len(password) < 8:
        return False

    # Initialize variables to check other criteria
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Define a set of special characters
    special_characters = "!@#$%^&*(),.?\":{}|<>"

    # Iterate through each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in special_characters:
            has_special = True

    # Check if all criteria are met
    return has_upper and has_lower and has_digit and has_special

# Function to get user input and provide feedback
def main():
    password = input("Enter a password: ")
    is_strong = check_password_strength(password)

    if is_strong:
        print("Password is strong. Good job!")
    else:
        print("Password is weak. Please make sure it meets the criteria.")

# Entry point of the script
if __name__ == "__main__":
    main()
