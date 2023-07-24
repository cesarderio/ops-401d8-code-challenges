#!/usr/bin/env python3

# Import libraries
import sys
from scapy.all import sr1, IP, ICMP, TCP


# Define our target host and TCP  port to scan
host = "scanme.namp.org"
port_range = 22
scr_port = 22
dst_port = 22

p=sr1(IP(dst=host)/ICMP())
if p:
    p.show()

# TCP packet

response = sr1(IP(dst=host)/TCP(sport=scr_port, dport=dst_port, flags="S"), timeout=1, verbose=0)

# print(response)

if (response.haslayer(TCP)):
    if (response.getlayer(TCP).flags == 0x12):
        # send RST packet
        send_rst = sr1(IP(dst=host)/TCP(sport=scr_port, dport=dst_port, flags="R"), timeout=1, verbose=0)
        print(f"{host}:{dst_port} is open.")
else:
    print(f"{host}:{dst_port} is not open.")
 