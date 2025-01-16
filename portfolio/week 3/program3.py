"""
Modify your previous program so that the password must be between 8 and 12 characters (inclusive) long.
"""

# Ask the user to create a password within valid length constraints
while True:
    user_password = input("Enter a password (must be 8-12 characters long): ")
    if 8 <= len(user_password) <= 12:
        confirm_password = input("Please confirm your password: ")
        if user_password == confirm_password:
            print("Password successfully created!")
            break
        else:
            print("Passwords do not match. Try again.")
    else:
        print("Error: Password length must be between 8 and 12 characters.")
