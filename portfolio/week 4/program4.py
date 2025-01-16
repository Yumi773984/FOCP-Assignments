'''
Write and test a function that takes a string parameter and returns it with the last 
character removed. (If the string contains one or fewer characters, return it unchanged.)
'''

# Function to remove the last character from a string
def remove_last_char(s):
    return s[:-1] if len(s) > 1 else s  

# Test the function
print("Testing the function...")

print(remove_last_char("Yuri"))       # Output: Yur
print(remove_last_char("Roka"))       # Output: Rok
print(remove_last_char("A"))          # Output: A
