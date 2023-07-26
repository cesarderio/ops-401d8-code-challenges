# Ops Challenge: Network Security Tool with Scapy Part 3 of 3

## Overview

Tools like Nmap are quite useful on their own, but what about customizing its capabilities? Because we know a little Python, we can explore creating our own network scanning tool with the Python library Scapy. Today you’ll finish development of your own network scanning tool.

By the end of this challenge, you’ll have your very own network scanning and enumeration tool. Use this knowledge of Python’s libraries to create custom network tools throughout your new career!

## Resources

## Objectives

The final iteration of your network scanning tool will perform the following:

* Ping an IP address determined by the user.

* If the host exists, scan its ports and determine if any are open.

## Tasks

Here’s a general outline of how to achieve the desired outcome.

* In Python, combine the two modes (port and ping) of your network scanner script.

* Eliminate the choice of mode selection.

* Continue to prompt the user for an IP address to target.

* Move port scan to its own function.

* Call the port scan function if the host is responsive to ICMP echo requests.

* Print the output to the screen.

## Stretch Goals (Optional Objectives)

* Instead of targeting a single IP address, allow the user to specify a range of IPs and have the tool scan each one in succession.
