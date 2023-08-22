#!/usr/bin/env python3





# Import libraries
import os
from time import sleep
import platform

import hashlib

# Declare variables


# Declare functions
def hash_file(filename):
    """This function returns the SHA-1 hash of a file passed into it"""

    # Create a hash object
    h = hashlib.sha1()

    # Open a file for reading in binary format
    with open(filename, 'rb') as file:
        
        # loop until the end of the file
        data = 0
        while data != b'':
            # read a chunk of bytes at a time
            data = file.read(1024)
            print(data)
            h.update(data)

    # Return the hex representation of the hash object
    return h.hexdigest()

message = hash_file("./test2.txt")
print(message)

# Main


# End



