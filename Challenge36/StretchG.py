#!/usr/bin/env python3

# Script Name:                  Web Application Fingerprinting
# Author:                       Raphael Chookagian
# Date of latest revision:      08/28/2023
# Purpose:                      Create a python script:
# In Python create a script that executes from a Linux box to perform the following:
# * Prompts the user to type a URL or IP address.
# * Prompts the user to type a port number.
# * Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.
# * Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.
# * Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.


# Import libraries
import os, time, sys, socket

# Netcat function
def netcat_scan(addr, port):
    try:
        # Create a socket and a new connection
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket1.settimeout(5)  # Set a timeout for the connection
        socket1.connect((addr, int(port)))

        # Receive the banner
        banner = socket1.recv(1024)
        print("[Netcat] Banner:", banner.decode().strip())

        # Completely close the connection
        socket1.close()
    except Exception as e:
        print("[Netcat] Error:", str(e))

# Telnet function
def telnet_scan(addr, port):
    command = f"telnet {addr} {port}"
    try:
        os.system(command)
    except Exception as e:
        print("[Telnet] Error:", str(e))

# Nmap function
def nmap_scan(addr):
    command = f"nmap -p- --open {addr}"
    try:
        os.system(command)
    except Exception as e:
        print("[Nmap] Error:", str(e))

# WhatWeb function
def whatweb_scan(addr):
    command = f"whatweb {addr}"
    try:
        os.system(command)
    except Exception as e:
        print("[WhatWeb] Error:", str(e))

# Curl function
def curl_scan(addr):
    command = f"curl -I {addr}"
    try:
        os.system(command)
    except Exception as e:
        print("[CURL] Error:", str(e))

# Main
while True:
    print("\nScanning Tool Menu")
    print("1. Netcat Scan")
    print("2. Telnet Scan")
    print("3. Nmap Scan")
    print("4. WhatWeb Scan")
    print("5. CURL Header Scan")
    print("6. Exit")
    
    choice = input("Enter choice number: ")

    if choice == "1":
        addr = input("Enter an IP address or URL for Netcat scan: ")
        port = input("Enter port number for Netcat scan: ")
        netcat_scan(addr, port)
    elif choice == "2":
        addr = input("Enter an IP address or URL for Telnet scan: ")
        port = input("Enter port number for Telnet scan: ")
        telnet_scan(addr, port)
    elif choice == "3":
        addr = input("Enter an IP address or URL for Nmap scan: ")
        nmap_scan(addr)
    elif choice == "4":
        addr = input("Enter a URL for WhatWeb scan: ")
        whatweb_scan(addr)
    elif choice == "5":
        addr = input("Enter a URL for CURL scan: ")
        curl_scan(addr)
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select a valid option.")
