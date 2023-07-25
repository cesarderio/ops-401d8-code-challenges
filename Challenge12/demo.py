#!/usr/bin/env python3

# Import variables

import ipaddress
from scapy.all import ICMP, IP, sr1, TCP






# Define variables
network = "10.0.2.0/24"
ip_list = ipaddress.IPv4Network(network)
host_count = 0
# for i in ip_list:
    # print(i)




# Define functions

def ping_sweep():
    
    # ask user for CIDR block
    # IP list
    global ip_list
    global host_count

    # send ICMP request for each host
    for host in ip_list:
        # adds exception for broadcast address and network address
        if (host in (ip_list.network_address, ip_list.broadcast_address)):
            # skip two addresses
            continue

            response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)

        elif ( int(response.getlayer(ICMP().type) == 3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10.13] ):
              print(f"Host {host} is blocking traffic")
        
        else:
            host_count = host_count + 1
            print(f"Host {host} is alive")




# Main
