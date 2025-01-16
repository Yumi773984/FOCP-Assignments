"""
Question:
Write a program to count lines, words, and characters in a file.
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        try:
            with open(file_name, "r") as file:
                content = file.read()
                print("Lines:", content.count("\n"))
                print("Words:", len(content.split()))
                print("Characters:", len(content))
        except FileNotFoundError:
            print("File not found.")
    else:
        print("Please provide a file name.")
