#!/usr/bin/python3







# Following in class demo, must create(compress) a zipfile first to use with this script.


# import libraries
from zipfile import ZipFile
from getpass import getpass



zip_file = input("Please provide the path to the zip file")
password = getpass("Please enter your password")



# Try open the zip file with provided password

with ZipFile(zip_file) as zf:
    zf.extractall(pwd=bytes(password, 'utf-8'))

# declare variables


# declare functions



# Create


# Main



