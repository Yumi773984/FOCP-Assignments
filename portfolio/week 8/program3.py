"""
Question:
Write a program to find lines in a file that contain a given word or pattern.
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        pattern = sys.argv[1]
        file_name = sys.argv[2]
        try:
            with open(file_name, "r") as file:
                for line in file:
                    if pattern in line:
                        print(line.strip())
        except FileNotFoundError:
            print("File not found.")
    else:
        print("Please provide a pattern and a file name.")
