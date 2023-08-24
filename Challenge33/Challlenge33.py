#!/usr/bin/env python3

# Script Name:                  Signature-based Malware Detection Part 3 of 3
# Author:                       Raphael Chookagian
# Date of latest revision:      08/23/2023
# Purpose:                      Create a python script:



# Install required dependencies/libraies
# Import libraries
import os
import hashlib
from time import sleep, strftime
import platform
# pip3 install requests
import requests
import subprocess

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


# Functions for VirusTotal integration

def get_virustotal_apikey_from_config(config_file=".config"):
    """Extract the VirusTotal API key from the config file."""
    try:
        with open(config_file, 'r') as file:
            for line in file.readlines():
                if "API_KEY_VIRUSTOTAL" in line:
                    return line.split('=')[-1].strip()
    except FileNotFoundError:
        print("Error: .config file not found.")
        return None

def virustotal_search(md5_hash):
    """Search for the MD5 hash on VirusTotal."""
    apikey = get_virustotal_apikey_from_config()
    
    if not apikey:
        print("Error: VirusTotal API key not found.")
        return
    
    # This concatenates everything into a working shell statement 
    # that gets passed into virustotal-search.py
    # query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + md5_hash
    # os.system(query)
    query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + md5_hash
    result = subprocess.getoutput(query)  # Capturing the output
    return result



# Main
if my_os == "Linux":
    linux_search()
elif my_os == "Windows":
    windows_search()
else:
    print("Your operating system is not supported")

# End



