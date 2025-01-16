'''
Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the function 
with a short program.
'''

# Function to count uppercase and lowercase letters
def count_case(s):
    uppers = sum(1 for letter in s if letter.isupper())
    lowers = sum(1 for letter in s if letter.islower())
    return uppers, lowers  

# Test the function
print("Testing the function...")

# Testing with a sample sentence
test_string = "Hi! I am Yuri Roka" 
up, low = count_case(test_string)  

print("String:", test_string)
print("Number of uppercase letters:", up)
print("Number of lowercase letters:", low)
