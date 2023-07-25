# Ops Challenge: Network Security Tool with Scapy Part 2 of 3

## Overview

Tools like Nmap are quite useful on their own, but what about customizing its capabilities? Because we know a little Python, we can explore creating our own network scanning tool with the Python library Scapy. Today you’ll continue development of your own network scanning tool.

## Resources

[Generating a Range of IP Addresses from a CIDR Address in Python](http://infinityquest.com/python-tutorials/generating-a-range-of-ip-addresses-from-a-cidr-address-in-python/)

## Requirements

Add the following features to your Network Security Tool:

* User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set

* ICMP Ping Sweep tool
  * Prompt user for network address including CIDR block, for example “10.10.0.0/24”
    *Careful not to populate the host bits!*

  * Create a list of all addresses in the given network

  * Ping all addresses on the given network except for network address and broadcast address
    * If no response, inform the user that the host is down or unresponsive.
    * If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
    * Otherwise, inform the user that the host is responding.

  * Count how many hosts are online and inform the user.
