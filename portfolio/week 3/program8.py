"""
Modify the "Times Table" again so that the user still enters the number of the table, 
but if this number is negative, the table is printed backwards. 
So entering "-7" would produce the Seven Times Table starting at "12 times" down to "0 times".
"""

# Get user input for the times table
user_number = int(input("Enter a number for the times table (negative for reverse): "))

if user_number >= 0:  # Normal order
    print(f"{user_number} Times Table:")
    for i in range(13):
        print(f"{i} x {user_number} = {i * user_number}")
else:  # Reverse order
    print(f"{-user_number} Times Table (Reverse):")
    for i in range(12, -1, -1):
        print(f"{i} x {-user_number} = {i * -user_number}")
