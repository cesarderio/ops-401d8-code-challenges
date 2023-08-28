#!/usr/bin/env python3

# Script Name:                  
# Author:                       Raphael Chookagian
# Date of latest revision:      08/28/2023
# Purpose:                      Create a python script:

# Import libraries
import os, time, sys, socket

# Declare variable
addr = input("Enter an IP address: ")
port = input("Enter port number: ")
# Declare functions

# Netcat function
def netcat_scan(addr, port):
    # os.system("nc " + addre + " " + port)
    # Create a socket and a new connection
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket1.connect((addr, int(port)))

    # Send the netcat command
    command = "nc " + addr + " " + port
    socket1.sendall(command.encode())
    socket1.shutdown(socket.SHUT_WR)

    # Handle the output
    output = socket1.recv(1024)
    clean_output = output.decode()
    print (clean_output)

    # Completely close the connection
    socket1.close()


# telnet function
def telnet_scan():


# nmap function
def nmap_scan():



# Main

print("Scanning Tool Menu")

# Build a menu giving the user the three options

netcat_scan(addr, port)
