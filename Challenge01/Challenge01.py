#!/usr/bin/python3

# Script Name:
# Author:                       Raphael Chookagian
# Date of latest revision:      07/11/2023
# Purpose:                      Create a python script that:


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
            response_message = 'Success'
        elif return_code == 1:
            response_message = 'Destination Unreachable'
        elif return_code == 2:
            response_message = 'Packet Loss'
        else:
            response_message = 'Unknown Error'

        # Print the response message
        print(f"[{timestamp}] Destination IP: {dest_ip} | Response: {response_message}")

        # Wait for 2 seconds before sending the next ping
        time.sleep(2)

# Main

# Call send_ping function
send_ping()

# End
