#!/usr/bin/env python3

# Script Name:                  Event Logging Tool Part 3 of 3
# Author:                       Raphael Chookagian
# Date of latest revision:      08/16/2023
# Purpose:                      Create a python script:
# In your Python tool:
# * Use StreamHandler and FileHandler in your Python script.
#   * FileHandler should write to a local file.
#   * StreamHandler should output to the terminal.
# ## Stretch Goals (Optional Objectives)
# Have your script also email you the event details.
# * Your handler must distinguish by event type. For example, in [DEMO.md](https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/class-28/challenges/DEMO.html) the handler only emails `ERROR` and not `WARNING` types.
# * See if you can include all features this week in one script, e.g. log rotation with FileHandler.


# Import libraries 
import logging
from logging.handlers import RotatingFileHandler
import sys
import random
import socket
import concurrent.futures
from scapy.all import sr, sr1, IP, ICMP, TCP, UDP, ARP
from netaddr import IPNetwork, AddrFormatError

# Create a logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Create a FileHandler and set level to debug
file_handler = RotatingFileHandler('network_tool.log', maxBytes=5*1024*1024, backupCount=3) 
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Create a StreamHandler and set level to debug
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


# Declare functions
# Create

def dns_resolution():
    host = input("Enter the host: ")
    try:
        print(f"IP address of {host}: {socket.gethostbyname(host)}")
        logging.info(f"Resolved IP address of {host}")
    except socket.gaierror:
        print(f"Could not resolve {host}")
        logging.error(f"Failed to resolve IP address of {host}", exc_info=True)

def arp_ping():
    ip = input("Enter the IP address: ")
    try:
        response = sr1(ARP(pdst=ip), timeout=1, verbose=0)
        if response is None:
            print(f"{ip} is down or unresponsive.")
            logging.warning(f"{ip} is unresponsive.")
        else:
            print(f"{ip} is up.")
            logging.info(f"{ip} is up.")
    except Exception as e:
        logging.error(f"Error during ARP ping to {ip}", exc_info=True)

def traceroute():
    host = input("Enter the host: ")
    try:
        for i in range(1, 28):
            pkt = IP(dst=host, ttl=i) / UDP(dport=33434)
            reply = sr1(pkt, timeout=1, verbose=0)
            if reply is None:
                break
            elif reply.type == 3:
                print(f"Reached {host} in {i} hops")
                logging.info(f"Reached {host} in {i} hops")
                break
            else:
                print(f"{i}: {reply.src}")
                logging.info(f"Traceroute hop {i}: {reply.src}")
    except Exception as e:
        logging.error(f"Error during traceroute to {host}", exc_info=True)

def udp_port_scan():
    host = input("Enter the host: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    port_range = range(start_port, end_port + 1)
    try:
        for dst_port in port_range:
            response = sr1(IP(dst=host)/UDP(dport=dst_port), timeout=1, verbose=0)
            if response is None:
                print(f"{host}:{dst_port} is open or filtered.")
                logging.info(f"{host}:{dst_port} is open or filtered.")
            elif response.haslayer(ICMP):
                if response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
                    print(f"{host}:{dst_port} is filtered.")
                    logging.warning(f"{host}:{dst_port} is filtered.")
                else:
                    print(f"{host}:{dst_port} is closed.")
                    logging.info(f"{host}:{dst_port} is closed.")
    except Exception as e:
        logging.error(f"Error during UDP port scan on {host}", exc_info=True)

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
        # Error for testing
        logging.error("This is a fake error for TCP Port Scan.")
        print("TCP Port Scan function is not defined yet.")
    elif choice == '2':
        # Error for testing
        logging.error("This is a fake error for ICMP Ping Sweep.")
        print("ICMP Ping Sweep function is not defined yet.")
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
        logging.warning("Invalid menu choice selected.")

# Main
user_menu()
