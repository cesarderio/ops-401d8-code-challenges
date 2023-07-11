#!/usr/bin/python3

# Script Name:
# Author:                       Raphael Chookagian
# Date of latest revision:      07/11/2023
# Purpose:                      Create a python script that:
# * Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# * Evaluate the response as either success or failure.
# * Assign success or failure to a status variable.
# * For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
# *Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8*

# Script Outline

# Import libraries
import datetime
import time
import subprocess

# Declare Variables

# Update and/or change IP address here
dest_ip = "8.8.8.8"

# Declare Functions

def send_ping():
    while True:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Execute the ping command
        ping_process = subprocess.Popen(['ping', '-c', '1', dest_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        _, stderr = ping_process.communicate()

        # Get the return code from the subprocess
        return_code = ping_process.returncode

        # Map the return code to a descriptive message
        if return_code == 0:
            res_mes = 'Success'
        elif return_code == 1:
            res_mes = 'Destination Unreachable'
        elif return_code == 2:
            res_mes = 'Packet Loss'
        else:
            res_mes = 'Unknown Error'

        # Print the response message
        print(f"[{timestamp}] Destination IP: {dest_ip} | Response: {res_mes}")

        # Wait for 2 seconds before sending the next ping
        time.sleep(2)

# Main

# Call send_ping function
send_ping()

# End
