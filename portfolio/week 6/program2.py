def calculate_factors(num):
    # Input validation for positive numbers
    if num <= 0:
        return "Only positive integers are allowed."
    
    # Generate a list of all factors
    divisors = []
    for candidate in range(1, num + 1):
        if num % candidate == 0:
            divisors.append(candidate)
    return divisors

# Example usage
test_value = 15
print(f"The divisors of {test_value} are: {calculate_factors(test_value)}")
