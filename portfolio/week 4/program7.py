'''
Write a program that reads 6 temperatures (in the same format as before), and displays 
the maximum, minimum, and mean of the values.
'''

# Celsius to Fahrenheit conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32  

# List for Fahrenheit temperatures
fahrenheit_temps = []

for i in range(6):
    temp_input = input(f"Enter temperature {i+1} in Celsius (e.g., 25C): ")
    if temp_input[-1].upper() == 'C':
        celsius = float(temp_input[:-1])
        fahrenheit_temps.append(celsius_to_fahrenheit(celsius))
    else:
        print("Invalid input.")

if fahrenheit_temps:
    print("\nResults:")
    print(f"Maximum: {max(fahrenheit_temps)}°F")
    print(f"Minimum: {min(fahrenheit_temps)}°F")
    print(f"Mean: {sum(fahrenheit_temps) / len(fahrenheit_temps)}°F")
