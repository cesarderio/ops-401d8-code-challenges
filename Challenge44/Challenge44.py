#!/usr/bin/python3

# Script Name:                  Create a Port Scanner
# Author:                       Raphael Chookagian
# Date of latest revision:      09/06/2023
# Purpose:                      Create a python script: Complete the Demo.


import socket

# Create a socket object
sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout value
# timeout = # TODO: Set a timeout value here.
timeout = 1  # 1 second, you can adjust this as needed
sockmod.settimeout(timeout)

# Collect a host IP from the user
# hostip = # TODO: Collect a host IP from the user.
hostip = input("Enter the target IP address: ")

# Collect a port number from the user, then convert it to an integer data type
# portno = # TODO: Collect a port number from the user, then convert it to an integer data type.
portno = int(input("Enter the target port number: "))

# def portScanner(portno):
#     if sockmod.FUNCTION((hostip, portno)): # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
#         print("Port closed")
#     else:
#         print("Port open")

def portScanner(port):
    try:
        # Connect to the target IP and port
        sockmod.connect((hostip, port))
        print("Port open")
    except socket.error:
        print("Port closed")
    finally:
        sockmod.close()

portScanner(portno)
