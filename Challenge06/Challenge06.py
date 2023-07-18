#!/usr/bin/env python3

# Script Name:                  
# Author:                       Raphael Chookagian
# Date of latest revision:      07/17/2023
# Purpose:                      Create a python script that utilizes the cryptography library to: * see README.md



import os
import sys
import shutil
import tarfile
from cryptography.fernet import Fernet

# Declare Variables
# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Declare Functions

def encrypt_file(file_path):
    # Read the contents of the file
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Encrypt the file data
    encrypted_data = cipher_suite.encrypt(file_data)

    # Write the encrypted data back to the file
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

    print("File encrypted successfully.")

def decrypt_file(file_path):
    # Read the contents of the file
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Decrypt the file data
    decrypted_data = cipher_suite.decrypt(file_data)

    # Write the decrypted data back to the file
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

    print("File decrypted successfully.")

def encrypt_message(message):
    # Encode the message as bytes
    message_bytes = message.encode()

    # Encrypt the message
    encrypted_message = cipher_suite.encrypt(message_bytes)

    # Print the encrypted message
    print("Encrypted message:", encrypted_message.decode())

def decrypt_message(message):
    # Decrypt the message
    decrypted_message = cipher_suite.decrypt(message.encode())

    # Print the decrypted message
    print("Decrypted message:", decrypted_message.decode())

def compress_file(file_path):
    # Create a tar.gz archive
    archive_name = file_path + '.tar.gz'
    with tarfile.open(archive_name, 'w:gz') as tar:
        tar.add(file_path)

    print("File compressed to:", archive_name)

def decompress_file(archive_path):
    # Extract the contents of the tar.gz archive
    with tarfile.open(archive_path, 'r:gz') as tar:
        tar.extractall(path=os.path.dirname(archive_path))

    print("File decompressed successfully.")


# Create

def main():
    while True:
        print("Select a mode:")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Encrypt a message")
        print("4. Decrypt a message")
        print("5. Compress a file")
        print("6. Decompress a file")
        print("0. Exit")

        mode = int(input("Enter the mode number: "))

        if mode == 1 or mode == 2:
            file_path = input("Enter the filepath: ")
            if not os.path.isfile(file_path):
                print("Error: File does not exist.")
                continue
            
            if mode == 1:
                encrypt_file(file_path)
            else:
                decrypt_file(file_path)
        
        elif mode == 3 or mode == 4:
            message = input("Enter the message: ")

            if mode == 3:
                encrypt_message(message)
            else:
                decrypt_message(message)
        
        elif mode == 5:
            file_path = input("Enter the filepath to compress: ")
            if not os.path.isfile(file_path):
                print("Error: File does not exist.")
                continue
            
            compress_file(file_path)
        
        elif mode == 6:
            archive_path = input("Enter the filepath to decompress: ")
            if not os.path.isfile(archive_path):
                print("Error: Archive file does not exist.")
                continue

            decompress_file(archive_path)

        elif mode == 0:
            print("Exiting...")
            break

        else:
            print("Please enter a valid mode number.")


# Main

if __name__ == '__main__':
    main()

# End
