"""
Question:
Write a program to check for misspelled words in a file using a dictionary.
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        try:
            with open("/usr/share/dict/words", "r") as dict_file:
                dictionary = set(word.strip().lower() for word in dict_file)

            with open(file_name, "r") as file:
                for word in file.read().split():
                    word_clean = ''.join(filter(str.isalpha, word)).lower()
                    if word_clean and word_clean not in dictionary:
                        print("Misspelled:", word_clean)
        except FileNotFoundError:
            print("File not found.")
    else:
        print("Please provide a file name")
