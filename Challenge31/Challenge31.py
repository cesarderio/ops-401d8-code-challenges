#!/usr/bin/env python3

# Script Name:                  Signature-based Malware Detection Part 1 of 3
# Author:                       Raphael Chookagian
# Date of latest revision:      08/21/2023
# Purpose:                      Create a python script:
# In your Python tool:

# * Prompt the user to type in a file name to search for.
# * Prompt the user for a directory to search in.
# * Search each file in the directory by name.
#   *TIP: You may need to perform different commands depending on what OS you’re executing the script on.*
# * For each positive detection, print to the screen the file name and location.
# * At the end of the search process, print to the screen how many files were searched and how many hits were found.
# The script must successfully execute on both Ubuntu Linux 20.04 Focal Fossa and Windows 10.
# ## Stretch Goals (Optional Objectives)
# Pursue these optional objectives if you are an advanced user or have remaining time.
# * Add logging capabilities to this script.

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



