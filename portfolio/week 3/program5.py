"""
Modify your program a final time so that it executes until the user successfully 
chooses a password. That is, if the password chosen fails any of the checks, the program 
should return to asking for the password the first time.
"""

BAD_PASSWORDS = ['password', '123456', 'qwerty', 'letmein', 'hello']

# Loop until a valid password is entered and confirmed
while True:
    temp_password = input("Create a secure password (8-12 characters, not too common): ")
    if len(temp_password) < 8 or len(temp_password) > 12:
        print("Error: Password must be between 8 and 12 characters.")
        continue
    if temp_password in BAD_PASSWORDS:
        print("Error: That password is too common. Try something more secure.")
        continue
    confirm_temp_password = input("Confirm your password: ")
    if temp_password == confirm_temp_password:
        print("Password successfully set!")
        break
    else:
        print("Error: Passwords did not match. Please try again.")
