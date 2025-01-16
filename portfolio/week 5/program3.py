"""
Question:
Write a program to find the shortest argument given when running the script.
If no arguments are provided, show a message.
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        shortest_arg = min(sys.argv[1:], key=len)
        print("Shortest argument is:", shortest_arg)
    else:
        print("No arguments were given.")
