#!/usr/bin/env python3

# Script Name:                  Network Security Tool with Scapy Part 2 of 3
# Author:                       Raphael Chookagian
# Date of latest revision:      07/25/2023
# Purpose:                      Create a python script:
# * Ping an IP address determined by the user.
# * If the host exists, scan its ports and determine if any are open.
# ## Tasks
# Here’s a general outline of how to achieve the desired outcome.
# * In Python, combine the two modes (port and ping) of your network scanner script.
# * Eliminate the choice of mode selection.
# * Continue to prompt the user for an IP address to target.
# * Move port scan to its own function.
# * Call the port scan function if the host is responsive to ICMP echo requests.
# * Print the output to the screen.
# ## Stretch Goals (Optional Objectives)
# * Instead of targeting a single IP address, allow the user to specify a range of IPs and have the tool scan each one in succession.


# Import libraries
import random
import socket
# pip install scapy
from scapy.all import sr, sr1, IP, ICMP, TCP, UDP, ARP
# pip install netaddr
from netaddr import IPNetwork, AddrFormatError

def dns_resolution(host):
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Could not resolve {host}")
        return None

def arp_ping(ip):
    response = sr1(ARP(pdst=ip), timeout=1, verbose=0)
    return response is not None

def tcp_port_scan(host, start_port, end_port):
    port_range = range(start_port, end_port + 1)
    for dst_port in port_range:
        src_port = random.randint(1025,65534)
        response = sr(IP(dst=host) / TCP(sport=src_port, dport=dst_port, flags='S'), timeout=2, verbose=0)
        if response is not None:
            for s,r in response:
                if r.haslayer(TCP) and r.getlayer(TCP).flags == 0x12:
                    print(f"{host}:{dst_port} is open.")

def scan_network():
    network = input("Enter the network (in CIDR notation): ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    # Iterate over all IP addresses in the network
    for ip in IPNetwork(network):
        ip = str(ip)
        
        # Check if host is responsive
        if arp_ping(ip):
            # Perform TCP port scan if host is responsive
            tcp_port_scan(ip, start_port, end_port)
        else:
            print(f"{ip} is down or unresponsive.")

# Main
scan_network()


# End
