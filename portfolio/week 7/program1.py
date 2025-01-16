def extract_unique_letters(text):
    # Use a set to gather unique characters
    unique_letters = set(text)
    
    # Return the sorted unique characters as a list
    return sorted(unique_letters)

# Test the function
string_input = input("Provide a string: ")
unique_result = extract_unique_letters(string_input)
print("The sorted unique letters are:", unique_result)
