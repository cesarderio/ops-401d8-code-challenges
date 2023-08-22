#!/usr/bin/env python3

# Script Name:                  Signature-based Malware Detection Part 2 of 3
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
import hashlib
from time import sleep, strftime
import platform

# Declare variables
my_os = platform.system()

print(my_os)

# Declare functions

def generate_md5(file_path):
    """Generate MD5 hash for a file"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def search_files(search_directory):
    for dirpath, dirnames, filenames in os.walk(search_directory):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            file_size = os.path.getsize(file_path)
            md5_hash = generate_md5(file_path)
            timestamp = strftime('%Y-%m-%d %H:%M:%S')
            
            print(f"Timestamp: {timestamp}")
            print(f"File Name: {file}")
            print(f"File Size: {file_size} bytes")
            print(f"Complete File Path: {os.path.abspath(file_path)}")
            print(f"MD5 Hash: {md5_hash}")
            print("-" * 50)

def linux_search():
    search_directory = input("Please enter the directory to search in: ")

    if not os.path.exists(search_directory):
        print(f"Error: The directory '{search_directory}' does not exist.")
        return

    # Perform the search
    search_files(search_directory)

def windows_search():
    # This function is currently identical to the Linux version
    # It's separated for potential future OS-specific modifications
    linux_search()

# Main
if my_os == "Linux":
    linux_search()
elif my_os == "Windows":
    windows_search()
else:
    print("Your operating system is not supported")

# End



