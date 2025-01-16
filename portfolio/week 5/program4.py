"""
Question:
Write a program to check if a website is working by providing a URL as an argument.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Website is working:", url)
            else:
                print("Website returned error code:", response.status_code)
        except Exception as e:
            print("Error connecting to website:", e)
    else:
        print("Please provide a URL.")
