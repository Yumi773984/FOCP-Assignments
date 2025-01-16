def country_capital_manager():
    # A dictionary to store countries and capitals
    country_capital_map = {}

    while True:
        # Ask the user for a country or 'stop' to end
        nation = input("Enter a country name (or type 'stop' to end): ").strip()

        if nation.lower() == 'stop':
            print("Program ended.")
            break

        # Normalize input for case-insensitive matching
        nation = nation.lower()

        # Check if the country is already known
        if nation in country_capital_map:
            print(f"The capital of {nation.title()} is {country_capital_map[nation]}.")
        else:
            # Prompt for the capital if the country is not found
            capital_name = input(f"Enter the capital city of {nation.title()}: ").strip()
            country_capital_map[nation] = capital_name
            print(f"Added: {nation.title()} - {capital_name}")

# Run the manager
country_capital_manager()
