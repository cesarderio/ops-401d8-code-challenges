# Ops Challenge: Attack Tools Part 1 of 3

## Overview

Many pentesting tools involve the use of Python for its code base. Impacket, a collection of Python classes for working with network protocols, is a pentester favorite for manipulating network traffic to the target system.

Today you will use some of Impacket’s example scripts.

*Be warned this is a self-guided, “sandbox” style activity. You’ll be choosing what scripted attack tool to execute. Remember to keep your traffic local to your NAT network.*

## Resources

* [Impacket](https://github.com/SecureAuthCorp/impacket)

* [Capabilities of Impacket](https://www.secureauth.com/labs/open-source-tools/impacket)

## Requirements

### Staging

For this lab you will need a Kali VM, feel free to use one from a previous class if you already have one ready. Follow these commands to get Impacket on your Kali VM `-sudo apt-get update` `-sudo git clone <https://github.com/SecureAuthCorp/impacket.git> /opt/impacket` `-sudo python3 ./setup.py install`

## Part 1: Practice Impacket Example sniff.py

First, let’s practice using the sniff.py packet sniffing tool.

* Locate sniff.py in your Impacket folder (/opt/impacket/examples).

* Activate the sniffer on your local network adapter.

* Perform a ping to this computer from another VM. Capture a screenshot. How do you know it’s ping traffic?

* Perform an ARP from another computer on the same subnet. Capture a screenshot. How do you know it’s ARP traffic?

  * What is an ARP request?

  * Perform multiple ARP requests from the neighboring computer. Why does only the first ARP packet show up in your sniffer?

  * Clear the ARP cache on the neighboring computer, then resend an ARP to the entire subnet. Does it show up? Why?

* Open up a browser on this computer and access a website. Capture a screenshot of your packet. Can you tell what traffic it is? Why/why not?

<br>

## Part 2: Practice Impacket Example of Your Choice

Now it’s time to experiment on your own with another one of Impacket’s example scripts.

* Review

  * [Capabilities of Impacket](https://www.secureauth.com/labs/open-source-tools/impacket)

  * [Impacket Guide](https://www.hackingarticles.in/impacket-guide-smb-msrpc/)

* Utilize one of the example scripts.

* Document the scenario, process, and outcomes.

*Budget your time on this one. Try to keep things simple to start with!*

<br>

## Stretch Goals (Optional Objectives)

If you fancy a challenge, try using Impacket to exploit a Windows target system.

Try deploying Windows 7 to the same subnet and execute some of the attacks included in the Impacket repo.
