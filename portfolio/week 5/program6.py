"""
Question:
Write a program to create a backup copy of a file.
"""

import shutil
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        backup_name = file_name + ".backup"
        try:
            shutil.copy(file_name, backup_name)
            print("Backup created:", backup_name)
        except FileNotFoundError:
            print("File not found.")
    else:
        print("Please provide a file name.")
