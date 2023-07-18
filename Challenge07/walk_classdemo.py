#!/usr/bin/env python3

# Script Name:                  
# Author:                       Raphael Chookagian
# Date of latest revision:      07/18/2023
# Purpose:                      Create a python script that utilizes the os.walk function

# Import libraries
import os

# Begin to recursively crawl through the directory tree
for root, dirs, files in os.walk('.', topdown=True):
    # For each hit, concatenate the current directory path to left of result
    for file in files:
        print(os.path.join(root, file))
    for dir in dirs:
        print(os.path.join(root, dir))


# Declare variables


# Declare functions


# Create


# Main


# End

