# Ops Challenge: Network Security Tool with Scapy Part 1 of 3

## Overview

Tools like Nmap are quite useful on their own, but what about customizing its capabilities? Because we know a little Python, we can explore creating our own network scanning tool with the Python library Scapy. Today you’ll begin development of your own network scanning tool.

## Resources

[Scapy Official Documentation](https://scapy.readthedocs.io/en/latest/index.html)

* [About Scapy](https://scapy.readthedocs.io/en/latest/introduction.html#)

* [Build your own tools](https://scapy.readthedocs.io/en/latest/extending.html)

## Requirements

In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:

* Utilize the scapy library

* Define host IP

* Define port range or specific set of ports to scan

* Test each port in the specified range using a for loop

  * If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
  * If flag 0x14 received, notify user the port is closed.
  * If no flag is received, notify the user the port is filtered and silently dropped.

## Stretch Goals (Optional Objectives)

* Utilize the random library

* Randomize the TCP source port in hopes of obfuscating the source of the scan
