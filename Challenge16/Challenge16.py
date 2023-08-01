#!/usr/bin/env python3

# Script Name:                  Automated Brute Force Wordlist Attack Tool Part 1 of 3
# Author:                       Raphael Chookagian
# Date of latest revision:      07/31/2023
# Purpose:                      Create a python script:
# In Python, create a script that prompts the user to select one of the following modes:

# ### **Mode 1: Offensive; Dictionary Iterator**
# * Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
# * Add a delay between words.
# * Print to the screen the value of the variable.

# ### **Mode 2: Defensive; Password Recognized**
# * Accepts a user input string.
# * Accepts a user input word list file path.
# * Search the word list for the user input string.
# * Print to the screen whether the string appeared in the word list.

# import libraries
import time

# Declare functions

# Create

def Off(file_path, delay=1):
    with open(file_path, 'r') as file:
        for line in file:
            # remove newline characters
            word = line.strip()
            print(word)
            # delay 
            time.sleep(delay)

def Def(file_path, target_word):
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()  # remove newline characters
            if word == target_word:
                print(f"'{target_word}' match found in list.")
                return
    print(f"'{target_word}' no match found in list.")

def main():
    while True:
        print("1: Offensive")
        print("2: Defensive")
        print("0: Exit")
        mode = int(input("Select task (0 to exit): "))
        
        if mode == 1:
            file_path = input("Enter file path(wordlist): ")
            Off(file_path)
        elif mode == 2:
            file_path = input("Enter (wordlist) file path: ")
            target_word = input("Enter target word: ")
            Def(file_path, target_word)
        elif mode == 0:
            break
        else:
            print("Invalid, please select available mode")


# Main

if __name__ == "__main__":
    main()

# End
















# def wordsList(file_path, delay=1):
#     with open(file_path, 'r') as file:
#         for line in file:
#             word = line.strip()  # remove newline characters
#             print(word)
#             time.sleep(delay)  # delay in seconds

# def target(file_path, target_word):
#     with open(file_path, 'r') as file:
#         for line in file:
#             word = line.strip()  # remove newline characters
#             if word == target_word:
#                 print(f"'{target_word}' match found in list.")
#                 return
#     print(f"'{target_word}' not found in word list.")

# def main():
#     mode = int(input("Enter 1 for Offensive mode or 2 for Defensive mode: "))
#     if mode == 1:
#         file_path = input("Enter the word list file path for Offensive mode: ")
#         wordsList(file_path)
#     elif mode == 2:
#         file_path = input("Enter the word list file path for Defensive mode: ")
#         target_word = input("Enter the word to search for: ")
#         target(file_path, target_word)
#     else:
#         print("Invalid mode selected. Please enter 1 or 2.")

# if __name__ == "__main__":
#     main()
