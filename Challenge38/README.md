# Ops Challenge: XSS Vulnerability Detection with Python

## Overview

Now that you’ve studied and practiced XSS, it’s time to explore Python’s capabilities in helping us automate the detection of vulnerabilities like XSS.

Today you will learn how a Python script can be written to evaluate a target for XSS vulnerabilities.

  Due to its extensive libraries and modules, the possibilities for creating useful security tools in Python are seemingly boundless! Check out Wapiti, a full web application security scanner coded in Python and installable using pip.

## Objectives

* Programmatically detect the presence (or lack) of a XSS vulnerability in a given target URL using a Python script

## Resources

[How to Build a XSS Vulnerability Scanner in Python](https://www.thepythoncode.com/article/make-a-xss-vulnerability-scanner-in-python)

## Staging

For this Ops Challenge, you’ll need to use VS Code to SSH into Web Security Dojo and prepare a few things. Here are the steps to take:

* Set Web Security Dojo to Bridged mode in VirtualBox.

* Identify its IP address in terminal.

* Verify SSH is running with `sudo systemctl status sshd` (the credentials to this VM are dojo/dojo)

* SSH into Web Security Dojo from VS Code using `ssh dojo@ip` where “ip” is its IP address

* In VS Code, install the Python extension via the extensions marketplace.

* Run `sudo apt update`

* Try `sudo apt install python3` to verify Python 3 is installed as an APT package on Web Security Dojo.

* Try `pip3 --version` to verify Pip3 is installed.

* Run `pip3 install bs4` to install Beautiful Soup, which is used by the demo code

* In VS Code, open the desktop of Web Security Dojo and access today’s folder on the desktop.

* Create a new challenge.py file and paste the demo code into it.

Now you’re all set to execute today’s Ops Challenge.

## Requirements

Copy the DEMO.md file from class repo > class-38 > challenges and complete the TODOs.

* Fully annotate any missing comments and populate any missing variables/code

* Test the script in Web Security Dojo to confirm the output is correct

  * This target URL should yield a positive vulnerability detection: https://xss-game.appspot.com/level1/frame

  * This target URL should yield a negative vulnerability detection: http://dvwa.local/login.php


## Stretch Goals (Optional Objectives)

Write a separate Python script that detects for SQL vulnerability in the target web app.

* Reference How to Build a SQL Injection Scanner in Python

* Test the script in Web Security Dojo to confirm the output is correct
