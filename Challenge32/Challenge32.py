#!/usr/bin/env python3

# Script Name:                  
# Author:                       Raphael Chookagian
# Date of latest revision:      08/22/2023
# Purpose:                      Create a python script:
# * Alter your search code to recursively scan each file and folder in the user input directory path and print it to the screen.

# * For each file scanned within the scope of your search directory:

#   * Generate the file’s MD5 hash using Hashlib.

#   * Assign the MD5 hash to a variable.

#   * Print the variable to the screen along with a timestamp, file name, file size, and complete (not symbolic) file path.


# Import libraries
import os
from time import sleep
import platform

# Declare variables
my_os = platform.system()

print(my_os)

def search_files(filename, search_directory):
    hits = []
    files_searched = 0
    
    for dirpath, dirnames, filenames in os.walk(search_directory):
        for file in filenames:
            files_searched += 1
            if file == filename:
                hits.append(os.path.join(dirpath, file))

    return hits, files_searched

def linux_search():
    filename = input("Please enter the file name to search for: ")
    search_directory = input("Please enter the directory to search in: ")

    if not os.path.exists(search_directory):
        print(f"Error: The directory '{search_directory}' does not exist.")
        return

    hits, files_searched = search_files(filename, search_directory)

    # Print results
    for hit in hits:
        print(f"Found: {hit}")

    print(f"\nTotal files searched: {files_searched}")
    print(f"Total hits found: {len(hits)}")

def windows_search():
    linux_search()

# Main
if my_os == "Linux":
    linux_search()
elif my_os == "Windows":
    windows_search()
else:
    print("Your operating system is not supported")


# End



