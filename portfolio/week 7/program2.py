def letters_present_in_any(word_a, word_b):
    return sorted(set(word_a) | set(word_b))  # Combine letters from both words

def letters_present_in_both(word_a, word_b):
    return sorted(set(word_a) & set(word_b))  # Find common letters

def letters_in_one_not_both(word_a, word_b):
    return sorted(set(word_a) ^ set(word_b))  # Symmetric difference of letters

# Test the functions
first_word = input("Enter the first string: ")
second_word = input("Enter the second string: ")

print("Letters present in at least one:", letters_present_in_any(first_word, second_word))
print("Letters present in both:", letters_present_in_both(first_word, second_word))
print("Letters in either but not both:", letters_in_one_not_both(first_word, second_word))
