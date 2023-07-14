#!/usr/bin/python3

#import libraries
import os, time, datetime
import smtplib
from getpass import getpass

# declare functions


email = input("Enter your email: ")
password = getpass("Enter your password: ")
ip = input("Please provide an ip address: ")

up = "Host is active"
down = "Host is down"


# Check that status changed
last = 0
ping_result = 0

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
  message = "Your server is back up"
  # send the email
  s.sendmail("cesar3432@gmail.com", email, message)
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
def check_ping():
    global last
    global ping_result
    now = datetime.datetime.now()
    # sends single ping to target and puts the response in a variable
    # response = os.system("ping -c 1 " + ip)

    # check the change of status
    # check the response
    if ((ping_result != last) and (ping_result == up)):
        # send up alert
        last = up
        send_upAlert()
        # ping_status = "Host is active"
    elif ((ping_result!= last) and (ping_result == down)):
        # send down alert
        last = down
        # call the function
        send_downAlert()
        # ping_status = "Host is down"
    response = os.system("ping -c 1 " + ip)

    if response == 0:
            ping_result = up
    else:
            ping_result = down
    print(str(now) + ": " + str(ping_result) + " to " + ip)

# Main

# Infinite loop
while True:
    check_ping()
    time.sleep(2)
