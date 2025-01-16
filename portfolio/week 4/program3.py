'''
Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently.
'''

# Greetings program
name = input("Enter your name: ").capitalize()  # Convert to proper case
print("Hello, " + name + "!")
