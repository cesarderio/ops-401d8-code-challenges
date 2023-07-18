#!/usr/bin/env python3



# Script Name:                  
# Author:                       Raphael Chookagian
# Date of latest revision:      07/17/2023
# Purpose:                      Create a python script that utilizes the cryptography library to: * see README.md






# Import libraries
from cryptography.fernet import Fernet



# Declare variables
y_n = "y"

# Declare functions

# Function to generate a key
def write_key():
    key = Fernet.generate_key()
    with open("key.txt", "wb") as f:
        f.write(key)


# Function to load a key
def load_key():
    with open("key.txt", "rb") as f:
        key = f.read()
    return key

# Function to encrypt a string/message
def encrypt_message():
    user_message = input("Enter a message: ")
    encrypt_message = user_message.encode()
    f = Fernet(key)

    # encrypt message
    encrypted = f.encrypt(encrypt_message)
    print("Your message has been encrypted")
    print(encrypted)

# Function to decrypt a string/message
def decrypt_message():
    user_message = input("Enter a message: ")
    decrypted_message = str.encode(user_message)

    f = Fernet(key)
    decrypted = f.decrypt(decrypted_message)
    print("Your message has been decrypted")
    print(decrypted)

# Function to encrypt a file
def encrypt_file():
    f = Fernet(key)
    filename = input("Enter a file name: ")
    with open(filename, "rb") as f:
        # read file data
        data = f.read()

    # encrypt the data
    encrypted_file = f.encrypt(data)

    # write encrypted data to file
    with open(filename + ".enc", "wb") as f:
            f.write(encrypted_file)
            print("Your file has been encrypted")

# Function to decrypt a file
def decrypt_file():
    f = Fernet(key)
    filename = input("Enter a full filepath: ")
    with open(filename, "rb") as f:
            # read file data
            data = f.read()
    decrypted_data = f.decrypt(data)

    with open(filename, "wb") as f:
         file.write(decrypted_data)
         print("Your file has been decrypted")
         print(decrypted_data)

# Function to encrypt a directory

# Function to decrypt a directory

# Function to handle the menu for the user
def menu():
     mode = input("What would you like to do? ")
     


# Create


# Main



# End

