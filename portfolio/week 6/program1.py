def number_to_binary(value):
    # Ensure the input is a positive integer
    if value <= 0:
        return "Input should be a positive integer."
    
    # Create the binary format by dividing repeatedly
    binary_result = ""
    while value > 0:
        binary_result = str(value % 2) + binary_result
        value //= 2  # Perform integer division
    
    return binary_result

# Example usage
input_number = 20
print(f"Binary form of {input_number} is: {number_to_binary(input_number)}")
