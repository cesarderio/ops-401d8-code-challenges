# Ops Challenge: Automated Brute Force Wordlist Attack Tool Part 3 of 3

## Overview

A brute force attack is a type of computer hack that relies on guessing possible combinations of a targeted password until the correct password is discovered. Today you will finish developing a custom tool that performs brute force attacks.

## Resources

[Zipfile documentation](https://docs.python.org/3/library/zipfile.html#module-zipfile)

## Requirements

First, setup your target ZIP file.

* Create a .txt file containing a secret message.

* Follow the guide, How to Protect Zip file with Password, to archive the .txt file with password protection.

Next, add a new mode to your Python brute force tool that allows you to brute force attack a password-locked zip file.

* Use the ***zipfile*** library.
* Pass it the ***RockYou.txt*** list to test all words in the list against the password-locked zip file.
