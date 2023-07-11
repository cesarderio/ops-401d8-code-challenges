#!/usr/bin/python3

# Script Name:                  
# Author:                       Raphael Chookagian
# Date of latest revision:      07/11/2023
# Purpose:                      Create a python script that:


# Script Outline
# Import libraries
# Build a function that handles my ping command


# import datetime library
import datetime
import os
import time


# Print current date and time
now = datetime.datetime.now()
# print("Current date and time: ")
# print(str(now))


# ping = os.system("ping 8.8.8.8")
# time.sleep(2)

# print(ping)

while True:
  ping = os.system("ping -c 1 8.8.8.8")
  time.sleep(2)
  print(str(now) + " " + str(ping) + " to 8.8.8.8")

# Declare Variables

# Declare Functions

# Create

# Main

# End
