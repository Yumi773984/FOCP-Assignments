"""
Modify your greeting program so that if the user does not enter a name (i.e., they just press Enter), 
the program responds "Hello, Stranger!". Otherwise, it should print a greeting with their name as before.
"""

# Ask the user for their name
user_input_name = input("Please type your name: ")

# Check if the user entered a name or left it blank
if user_input_name.strip() == "":
    print("Hello, Stranger!")
else:
    print(f"Hi there, {user_input_name}!")
