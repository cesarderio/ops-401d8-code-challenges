# Ops Challenge: Web Application Fingerprinting

## Overview

Banner grabbing, also known as “service fingerprinting,” is a way to check if your target computer supports specific services. This is useful when gathering intelligence on a target such as a web server.

  When a computer network service is activated by another program on a computer, it transmits a message. This message is traditionally known as a “banner.” By deliberately exploiting this behavior, a person can solicit service requests from specific port numbers to glean information about whether the target computer is hosting a service on the port. This is “banner grabbing.”

Today you will develop a Python script that utilizes multiple banner grabbing approaches against a single target.

## Resources

[Multiple Ways to Banner Grabbing](https://www.hackingarticles.in/multiple-ways-to-banner-grabbing/)

## Requirements

For this lab you’ll need to develop and test your Python script from a Linux VM with the tools Nmap, Netcat, and Telnet installed. Generally speaking, Kali Linux is the recommendation for this challenge.

In Python create a script that executes from a Linux box to perform the following:

* Prompts the user to type a URL or IP address.

* Prompts the user to type a port number.

* Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.

* Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.

* Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.

*NOTE: Be sure to only target approved URLs like scanme.nmap.org or web servers you own.*

## Stretch Goals (Optional Objectives)

Use additional banner grabbing techniques, such as WhatWeb and CURL, to gather as much information as possible about a target web server.
