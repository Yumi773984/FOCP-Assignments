import sys
import os
from statistics import mean
from tabulate import tabulate

def read_file(file_path):
    """Reads and parses the input file containing lap times."""
    # Check if the file exists
    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        sys.exit(1)

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract the race location from the first line (e.g., Monaco Grand Prix)
    race_location = lines[0].strip()
    lap_times = []

    # Process each line after the first one (which is race location)
    for line in lines[1:]:
        driver_code = line[:3]  # Driver code is the first 3 characters
        try:
            lap_time = float(line[3:].strip())  # The rest of the line is the lap time
            lap_times.append((driver_code, lap_time))
        except ValueError:
            # Handle invalid lap time entries (skip the line if not a valid float)
            print(f"Warning: Skipping invalid line: {line.strip()}")

    return race_location, lap_times

def calculate_fastest_time(lap_times):
    """Finds the driver with the fastest lap time."""
    # Use the min function to find the driver with the smallest lap time
    return min(lap_times, key=lambda x: x[1])

def calculate_driver_statistics(lap_times):
    """Calculates fastest and average times for each driver."""
    driver_data = {}

    # Organize lap times by driver code (group all lap times by driver)
    for driver_code, lap_time in lap_times:
        if driver_code not in driver_data:
            driver_data[driver_code] = []
        driver_data[driver_code].append(lap_time)

    # Calculate the fastest and average times for each driver
    driver_stats = {}
    for driver_code, times in driver_data.items():
        driver_stats[driver_code] = {
            "fastest": min(times),  # Fastest lap time for the driver
            "average": mean(times)  # Average lap time for the driver
        }

    return driver_stats

def calculate_overall_average(lap_times):
    """Calculates the overall average lap time for all drivers."""
    # Extract all lap times and compute their mean (overall average)
    times = [time for _, time in lap_times]
    return mean(times)

def display_results(race_location, fastest_driver, driver_stats, overall_average):
    """Displays the race results including driver statistics."""
    # Display basic race info: location, fastest driver, and overall average lap time
    print(f"Race Location: {race_location}\n")
    print(f"Fastest Driver: {fastest_driver[0]} with a time of {fastest_driver[1]:.3f} seconds\n")
    print(f"Overall Average Lap Time: {overall_average:.3f} seconds\n")

    # Display individual driver statistics: fastest and average times
    print("Driver Statistics:")
    table_data = []
    for driver, stats in driver_stats.items():
        table_data.append([driver, f"{stats['fastest']:.3f}", f"{stats['average']:.3f}"])

    # Print the table using tabulate for easy readability
    print(tabulate(table_data, headers=["Driver", "Fastest Time", "Average Time"], tablefmt="grid"))

    # Display fastest times in descending order (sorted by fastest lap time)
    print("\nFastest Times in Descending Order:")
    sorted_times = sorted([(driver, stats['fastest']) for driver, stats in driver_stats.items()], key=lambda x: x[1], reverse=True)
    sorted_table = [[driver, f"{time:.3f}"] for driver, time in sorted_times]
    print(tabulate(sorted_table, headers=["Driver", "Fastest Time"], tablefmt="grid"))

def main():
    """Main function to execute the program."""
    # Check if the correct number of arguments is provided (timings file and drivers file)
    if len(sys.argv) != 3:
        print("Usage: python timings_board.py <timings_file> <drivers_file>")
        sys.exit(1)

    timings_file = sys.argv[1]  # Path to the timings data file
    drivers_file = sys.argv[2]  # Path to the drivers data file

    # Read the input files and parse data
    race_location, lap_times = read_file(timings_file)

    # Exit if no valid lap times are found
    if not lap_times:
        print("Error: No valid lap time data found.")
        sys.exit(1)

    # Compute statistics and results
    fastest_driver = calculate_fastest_time(lap_times)  # Fastest driver based on lap time
    driver_stats = calculate_driver_statistics(lap_times)  # Stats for each driver
    overall_average = calculate_overall_average(lap_times)  # Overall average lap time

    # Sort driver statistics by fastest lap time for display
    sorted_driver_stats = dict(sorted(driver_stats.items(), key=lambda x: x[1]['fastest']))

    # Display all results
    display_results(race_location, fastest_driver, sorted_driver_stats, overall_average)

if __name__ == "__main__":
    main()
