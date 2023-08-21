# Ops Challenge: Signature-based Malware Detection Part 1 of 3

## Overview

Detection and remediation of malware is the core function of many security products, and an optional secondary feature on others like perimeter firewalls and proxy servers.

Today you will begin development of your own basic antivirus tool in Python.

## Resources

[How to Find Files and Folders in Linux Using the Command Line](https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/)

[How to Use Find from the Windows Command Prompt](https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/)

## Requirements

In Python, write a script that will:

* Prompt the user to type in a file name to search for.

* Prompt the user for a directory to search in.

* Search each file in the directory by name.
  *TIP: You may need to perform different commands depending on what OS you’re executing the script on.*

* For each positive detection, print to the screen the file name and location.

* At the end of the search process, print to the screen how many files were searched and how many hits were found.

The script must successfully execute on both Ubuntu Linux 20.04 Focal Fossa and Windows 10.

## Stretch Goals (Optional Objectives)

Pursue these optional objectives if you are an advanced user or have remaining time.

* Add logging capabilities to this script.
