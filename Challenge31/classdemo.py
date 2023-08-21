#!/usr/bin/env python3

# Import libraries
import os
from time import sleep
import platform


# Declare variables
my_os = platform.system()

print(my_os)

# Declare functions
def linux_search():

# Create

# Main
if my_os == "Linux":
    linux_search()
elif my_os == "Windows":
    windows_search()
else:
    print("Your operating system is not supported")

# End



