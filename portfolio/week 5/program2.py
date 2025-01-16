"""
Question:
Write a program to count how many arguments were given when running the script.
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("Number of arguments:", len(sys.argv) - 1)
    else:
        print("No arguments provided.")
