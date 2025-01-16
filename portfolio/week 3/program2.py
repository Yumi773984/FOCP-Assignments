"""
Write a program that simulates the way in which a user might choose a password. 
The program should prompt for a new password, and then prompt again. 
If the two passwords entered are the same, the program should say "Password Set" or similar. 
Otherwise, it should report an error.
"""

# Prompt user to create and confirm a password
new_password = input("Set a new password: ")
confirm_password = input("Confirm your password: ")

# Validate if the passwords match
if new_password == confirm_password:
    print("Password Set Successfully!")
else:
    print("Error: Passwords don't match. Please try again.")
