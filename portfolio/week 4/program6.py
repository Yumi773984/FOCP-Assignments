'''
Write and test a function that converts a temperature measured in degrees centigrade 
into the equivalent in Fahrenheit, and another that does the reverse conversion. Test 
both functions.
'''

# Celsius to Fahrenheit conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32  

# Fahrenheit to Celsius conversion
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9  

# Choose conversion
print("Choose the conversion:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter 1 or 2: ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F.")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C.")
else:
    print("Invalid choice.")
