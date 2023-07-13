#!/usr/bin/python3

# Script Name:                  Uptime Sensor pt.2
# Author:                       Raphael Chookagian
# Date of latest revision:      07/12/2023
# Purpose:                      Create a script that:
# * Ask the user for an email address and password to use for sending notifications.

# * Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).

# * Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.


# Import libraries
import os
import time
import datetime
import smtplib
from getpass import getpass

# Declare Variables
email = input("Enter your email: ")
password = getpass("Enter your password: ")
ip = input("Please provide an ip address: ")

up = "Host is active"
down = "Host is down"

# Check that status changed
last = 0
ping_result = 0

# Declare Functions

# Funtion that handles when the host goes from down to up
def send_upAlert():
  # gets timestamp
  now = datetime.datetime.now()
  # start smtp session
  s = smtplib.SMTP('smtp.gmail.com', 587)
  # start TLS
  s.starttls()
  # authentication
  s.login(email, password)
  # content of email
  message = "Server is up and running"
  # send the email
  s.sendmail("raphaellab2323@gmail.com", email, message)
  # close the session
  s.quit()

# Function that handles when the host goes from up to down
def send_downAlert():
  # gets timestamp
  now = datetime.datetime.now()
  # start smtp session
  s = smtplib.SMTP('smtp.gmail.com', 587)
  # start TLS
  s.starttls()
  # authentication
  s.login(email, password)
  # content of email
  message = "Server connection is down"
  # send the email
  s.sendmail("raphaellab2323@gmail.com", email, message)
  # close the session
  s.quit()



# function handles ping
def check_ping(ip):
    global last
    global ping_result
    # sends single ping to target and puts the response in a variable
    response = os.system("ping -c 1 " + ip)

    # check the change of status
    # check the response
    if ((ping_result != last) and (response == 0)):
        # send up alert
        send_upAlert()
        ping_status = "Host is active"
    else:
        # send down alert
        send_downAlert()
        ping_status = "Host is down"
    return ping_status

# Main
while True:
    response = os.system("ping -c 1 " + ip)

    # Extract the exit code from the response
    ping_result = response >> 8
    ping_status = check_ping(ip)
    print(ping_status)
    # Wait for 10 seconds before checking again
    time.sleep(10)
