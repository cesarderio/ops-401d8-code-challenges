# Ops Challenge: Signature-based Malware Detection Part 2 of 3

## Overview

Detection and remediation of malware is the core function of many security products, and an optional secondary feature on others like perimeter firewalls and proxy servers.

By generating a hash value derived from a target file, we can uniquely identify that file either now or later on. This facilitates the security process known as hash validation. Today you will continue development of your own basic antivirus tool in Python.

*“MD5 Message Digest Algorithm, or MD5, is a cryptographic hashing function. It is a part of the Message Digest Algorithm family which was created to verify the integrity of any message or file that is hashed. MD5 is still used in a few cases; however, MD5 is insecure and should not be used in any application.”* [-Section](https://www.section.io/engineering-education/what-is-md5/)

## Resources

[Hashlib Official Documentation](https://docs.python.org/3/library/hashlib.html)

[Python Program to Find Hash of File](https://www.programiz.com/python-programming/examples/hash-file)

## Requirements

Continue developing your Python malware detection tool.

* Alter your search code to recursively scan each file and folder in the user input directory path and print it to the screen.

* For each file scanned within the scope of your search directory:

  * Generate the file’s MD5 hash using Hashlib.

  * Assign the MD5 hash to a variable.

  * Print the variable to the screen along with a timestamp, file name, file size, and complete (not symbolic) file path.

*TIP: You may need to bring in additional Python modules to complete today’s objective.*

The script should be tested to execute successfully in Python3.

## Stretch Goals (Optional Objectives)

Pursue these optional objectives if you are an advanced user or have remaining time.

* Include logging capabilities in your script. All data output to the screen should also append to a log file.

* Instead of assigning the MD5 hash to a variable, pass all data into a 2D array.

  * Treat each row of the array as a single entry in a database, including timestamp, file path, and MD5 hash value.

  * Each new file scanned should row append into the array.
