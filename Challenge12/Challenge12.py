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
import random
import socket
import concurrent.futures
from scapy.all import sr, sr1, IP, ICMP, TCP, UDP, ARP
from netaddr import IPNetwork, AddrFormatError

# Define our target host and TCP port range to scan
# host = "scanme.nmap.org"
# port_range = range(20, 25)
# port_range = 22
# scr_port = 22
# dst_port = 22

# Define functions
# Create

def dns_resolution():
    host = input("Enter the host: ")
    try:
        print(f"IP address of {host}: {socket.gethostbyname(host)}")
    except socket.gaierror:
        print(f"Could not resolve {host}")

def arp_ping():
    ip = input("Enter the IP address: ")
    response = sr1(ARP(pdst=ip), timeout=1, verbose=0)
    if response is None:
        print(f"{ip} is down or unresponsive.")
    else:
        print(f"{ip} is up.")

def traceroute():
    host = input("Enter the host: ")
    for i in range(1, 28):
        pkt = IP(dst=host, ttl=i) / UDP(dport=33434)
        reply = sr1(pkt, timeout=1, verbose=0)
        if reply is None:
            break
        elif reply.type == 3:
            print(f"Reached {host} in {i} hops")
            break
        else:
            print(f"{i}: {reply.src}")

def udp_port_scan():
    host = input("Enter the host: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    port_range = range(start_port, end_port + 1)
    for dst_port in port_range:
        response = sr1(IP(dst=host)/UDP(dport=dst_port), timeout=1, verbose=0)
        if response is None:
            print(f"{host}:{dst_port} is open or filtered.")
        elif response.haslayer(ICMP):
            if response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
                print(f"{host}:{dst_port} is filtered.")
            else:
                print(f"{host}:{dst_port} is closed.")

def user_menu():
    print("Please select an option:")
    print("1. TCP Port Scan")
    print("2. ICMP Ping Sweep")
    print("3. DNS Resolution")
    print("4. ARP Ping")
    print("5. Traceroute")
    print("6. UDP Port Scan")
    choice = input("Enter your choice: ")
    if choice == '1':
        host = input("Enter the host to scan: ")
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))
        port_range = range(start_port, end_port + 1)
        tcp_port_scan(host, port_range)
    elif choice == '2':
        network = input("Enter the network (in CIDR notation): ")
        icmp_ping_sweep(network)
    elif choice == '3':
        dns_resolution()
    elif choice == '4':
        arp_ping()
    elif choice == '5':
        traceroute()
    elif choice == '6':
        udp_port_scan()
    else:
        print("Invalid choice.")


# Main

user_menu()

# End
