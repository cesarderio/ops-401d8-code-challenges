#!/usr/bin/python3

# Script Name:                  Uptime Sensor pt.2
# Author:                       Raphael Chookagian
# Date of latest revision:      07/12/2023
# Purpose:                      Create a script that:
# * Ask the user for an email address and password to use for sending notifications.

# * Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).

# * Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.


# Import libraries
import os, time, datetime
import smtplib
from getpass import getpass

# Declare Variables





email = input("Enter your email: ")
password = getpass("Enter your password: ")
ip = input("Please provide an ip address: ")

up = "Host is active"
down = "Host is down"

# Declare Functions

# Create

# Main


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
  s.sendmail(raphaellab2323@gmail.com, email, message)
  # close the session
  s.quit()

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
  s.sendmail(raphaellab2323@gmail.com, email, message)
  # close the session
  s.quit()



# function handles ping
def check_ping(ip):

  global ping_result
  global last
  # sends single ping to target and puts the response in a variable
  response = os.system("ping -c 1" + ip)

  # check the response
  if response == 0:
    # send up alert
    send_upAlert()
    ping_status = "Host is active"
  else:
    # send down alert
    send_downAlert()
    ping_status = "Host is down"

  return ping_status







# End
