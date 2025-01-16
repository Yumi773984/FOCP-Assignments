"""
Modify your program again so that the chosen password cannot be one of a list of 
common passwords, defined thus: BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
"""

# List of disallowed passwords
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# Loop to get a valid password
while True:
    chosen_password = input("Choose a strong password (8-12 characters, avoid common ones): ")
    if chosen_password in BAD_PASSWORDS:
        print("This password is too common. Choose a different one.")
    elif 8 <= len(chosen_password) <= 12:
        confirm_password = input("Re-enter your password to confirm: ")
        if chosen_password == confirm_password:
            print("Your password has been successfully set!")
            break
        else:
            print("Passwords do not match. Please try again.")
    else:
        print("Password must be between 8 and 12 characters.")
