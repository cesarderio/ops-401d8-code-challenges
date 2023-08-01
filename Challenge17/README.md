# Ops Challenge: Automated Brute Force Wordlist Attack Tool Part 2 of 3

## Overview

A brute force attack is a type of computer hack that relies on guessing possible combinations of a targeted password until the correct password is discovered. Today you will continue to develop a custom tool that performs brute force attacks.

## Resources

* [How to Make an SSH Brute-Forcer in Python](https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/)

* [How to Execute Shell Commands in a Remote Machine using Python - Paramiko](https://www.geeksforgeeks.org/how-to-execute-shell-commands-in-a-remote-machine-using-python-paramiko/)

## Requirements

Add to your Python brute force tool the capability to:

* Authenticate to an SSH server by its IP address.
  * Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.

*Note: Stay out of trouble! Restrict this kind of traffic to your local network VMs.*

## Stretch Goals (Optional Objectives)

Add to your Python brute force tool the capability to:

* Dump the user credential hashes of the victim system and print them to the screen.
