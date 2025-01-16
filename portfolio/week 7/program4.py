def analyze_frequency(text):
    # Dictionary to store the frequency of each letter
    frequency_map = {chr(c): 0 for c in range(97, 123)}  # a-z initialized with 0

    # Iterate through the input text
    for character in text.lower():
        if character.isalpha():  # Only consider alphabetic characters
            frequency_map[character] += 1

    # Sort the frequencies in descending order and take the top 6
    most_frequent = sorted(frequency_map.items(), key=lambda pair: pair[1], reverse=True)[:6]

    # Output the top six letters and their counts
    print("Top six most frequent letters:")
    for char, freq in most_frequent:
        print(f"{char.upper()}: {freq}")

# Test the function
encrypted_message = input("Provide an encrypted string: ")
analyze
