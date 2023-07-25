#!/usr/bin/env python3

# Script Name:                  Network Security Tool with Scapy Part 2 of 3
# Author:                       Raphael Chookagian
# Date of latest revision:      07/25/2023
# Purpose:                      Create a python script:
# * User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set

# * ICMP Ping Sweep tool
#   * Prompt user for network address including CIDR block, for example “10.10.0.0/24”
#     *Careful not to populate the host bits!*

#   * Create a list of all addresses in the given network

#   * Ping all addresses on the given network except for network address and broadcast address
#     * If no response, inform the user that the host is down or unresponsive.
#     * If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is
      # actively blocking ICMP traffic.
#     * Otherwise, inform the user that the host is responding.

#   * Count how many hosts are online and inform the user.




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
