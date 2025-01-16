"""
Question:
Write a program to find the max, min, and mean of temperatures provided as arguments.
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        temps = [float(temp) for temp in sys.argv[1:]]
        print("Maximum:", max(temps))
        print("Minimum:", min(temps))
        print("Mean:", sum(temps) / len(temps))
    else:
        print("No temperatures provided.")
