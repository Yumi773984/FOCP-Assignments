'''
Modify the previous program so that it can process any number of values. The input 
terminates when the user just presses "Enter" at the prompt rather than entering a value.
'''

# Celsius to Fahrenheit conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32  

fahrenheit_temps = []

while True:
    temp_input = input("Enter a temperature in Celsius (e.g., 25C) or press Enter to finish: ")
    if not temp_input:
        break
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
else:
    print("No temperatures entered.")
