def is_number_prime(value):
    # Check if the number is less than 2
    if value <= 1:
        return False  # Values 1 and below are not prime
    
    # Check divisibility for numbers up to the square root
    for potential_factor in range(2, int(value**0.5) + 1):
        if value % potential_factor == 0:
            return False  # Found a divisor, not prime
    return True

# Example usage
try:
    user_input = int(input("Provide a number to test for primality: "))
    if is_number_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is not a prime number.")
except ValueError:
    print("Error: Please input a valid integer.")
