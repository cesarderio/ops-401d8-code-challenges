#!/usr/bin/env python3

# Script Name:                  
# Author:                       Raphael Chookagian
# Date of latest revision:      07/24/2023
# Purpose:                      Create a python script:

# In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:
# * Utilize the scapy library
# * Define host IP
# * Define port range or specific set of ports to scan
# * Test each port in the specified range using a for loop
#   * If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
#   * If flag 0x14 received, notify user the port is closed.
#   * If no flag is received, notify the user the port is filtered and silently dropped.

# ## Stretch Goals (Optional Objectives)
# * Utilize the random library
# * Randomize the TCP source port in hopes of obfuscating the source of the scan

# Import libraries
import sys
from scapy.all import sr1, IP, ICMP, TCP
import random

# Define our target host and TCP port range to scan
host = "scanme.nmap.org"
port_range = range(20, 25)
# port_range = 22
# scr_port = 22
# dst_port = 22

# Main
for dst_port in port_range:
    scr_port = random.randint(1024, 65535)  # Randomize the TCP source port
    response = sr1(IP(dst=host)/TCP(sport=scr_port, dport=dst_port, flags="S"), timeout=1, verbose=0)

    if response is None:
        print(f"{host}:{dst_port} has been filtered and dropped.")
    elif response.haslayer(TCP):
        tcp_layer = response.getlayer(TCP)
        # Port is open
        if tcp_layer.flags == 0x12:
            send_rst = sr1(IP(dst=host)/TCP(sport=scr_port, dport=dst_port, flags="R"), timeout=1, verbose=0)
            print(f"{host}:{dst_port} is currently open.")
            # Port is closed
        elif tcp_layer.flags == 0x14:
            print(f"{host}:{dst_port} is currently not open.")

# End

# p=sr1(IP(dst=host)/ICMP())
# if p:
#     p.show()

# # TCP packet

# response = sr1(IP(dst=host)/TCP(sport=scr_port, dport=dst_port, flags="S"), timeout=1, verbose=0)

# # print(response)

# if (response.haslayer(TCP)):
#     if (response.getlayer(TCP).flags == 0x12):
#         # send RST packet
#         send_rst = sr1(IP(dst=host)/TCP(sport=scr_port, dport=dst_port, flags="R"), timeout=1, verbose=0)
#         print(f"{host}:{dst_port} is open.")
# else:
#     print(f"{host}:{dst_port} is not open.")
