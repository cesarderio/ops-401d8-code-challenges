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
  s.sendmail(cesar3432@gmail.com, email, message)

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
    ping_status = "Host is active"
  else:
    ping_status = "Host is down"

  return ping_status

