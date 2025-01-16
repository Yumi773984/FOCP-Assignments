"""
Modify the "Times Table" program so that the user enters the number of the table they require. 
This number should be between 0 and 12 inclusive.
"""

# Prompt user for the table they want
while True:
    try:
        table_number = int(input("Enter the number of the times table (0-12): "))
        if 0 <= table_number <= 12:
            print(f"Times Table for {table_number}:")
            for n in range(13):
                print(f"{n} x {table_number} = {n * table_number}")
            break
        else:
            print("Error: Please enter a number between 0 and 12.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
