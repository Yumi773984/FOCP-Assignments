def encrypt_text(input_message):
    # Remove spaces and reverse the string
    no_space_message = input_message.replace(" ", "")
    reversed_message = no_space_message[::-1]
    return reversed_message

# Example usage
plain_text = input("Enter the text to encrypt: ")
encrypted_result = encrypt_text(plain_text)
print(f"The encrypted version of your message is: {encrypted_result}")
