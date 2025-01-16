"""
Question:
Write a program to add line numbers to a file's contents and print them.
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        try:
            with open(file_name, "r") as file:
                for index, line in enumerate(file, start=1):
                    print(index, line.strip())
        except FileNotFoundError:
            print("File not found.")
    else:
        print("Please provide a file name.")
