#!/usr/bin/env python3

# Script Name:                  
# Author:                       Raphael Chookagian
# Date of latest revision:      07/18/2023
# Purpose:                      Create a python script that adds a feature capability

import os
import subprocess
import sys
import shutil
import tarfile
import ctypes
import ctypes.wintypes
from cryptography.fernet import Fernet


# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

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

def encrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=True):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path)

    print("Folder and its contents encrypted successfully.")

def decrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=True):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path)

    print("Folder and its contents decrypted successfully.")

def change_wallpaper(message):
    # Set the wallpaper
    SPI_SETDESKWALLPAPER = 0x0014
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, message, 0)

    print("Desktop wallpaper changed successfully.")

def show_popup_window(title, message):
    # Create a pop-up window
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, message, title, 0)

    print("Pop-up window displayed successfully.")

def main():
    while True:
        print("Select a mode:")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Encrypt a message")
        print("4. Decrypt a message")
        print("5. Compress a file")
        print("6. Decompress a file")
        print("7. Recursively encrypt a folder and its contents")
        print("8. Recursively decrypt a folder encrypted by this tool")
        print("9. Change desktop wallpaper with a message")
        print("10. Show a pop-up window with a message")
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
        
        elif mode == 7:
            folder_path = input("Enter the folder path to encrypt: ")
            if not os.path.isdir(folder_path):
                print("Error: Folder does not exist.")
                continue

            encrypt_folder(folder_path)
        
        elif mode == 8:
            folder_path = input("Enter the folder path to decrypt: ")
            if not os.path.isdir(folder_path):
                print("Error: Folder does not exist.")
                continue

            decrypt_folder(folder_path)
        
        elif mode == 9:
            message = input("Enter the message for the desktop wallpaper: ")
            change_wallpaper(message)
        
        elif mode == 10:
            title = input("Enter the title for the pop-up window: ")
            message = input("Enter the message for the pop-up window: ")
            show_popup_window(title, message)
        
        elif mode == 0:
            print("Exiting...")
            break

        else:
            print("Invalid mode.")

if __name__ == '__main__':
    main()
