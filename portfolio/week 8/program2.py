"""
Question:
Write a program to compare the contents of two files and say if they are the same.
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        try:
            with open(file1, "r") as f1, open(file2, "r") as f2:
                if f1.read() == f2.read():
                    print("Files are the same.")
                else:
                    print("Files are different.")
        except FileNotFoundError as e:
            print("Error:", e)
    else:
        print("Please provide two file names.")
