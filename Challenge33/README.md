# Ops Challenge: Signature-based Malware Detection Part 3 of 3

## Overview

Detection and remediation of malware is the core function of many security products, and an optional secondary feature on others like perimeter firewalls and proxy servers.

VirusTotal is a respected vendor-neutral database of malware signatures. Today you will finish development of your own basic antivirus tool in Python by incorporating VirusTotal.

## Resources

* [Getting Started with VirusTotal API](https://developers.virustotal.com/reference#file-scan)

* [VirusTotal API – Getting started with security automation](https://www.tines.io/blog/virustotal-api-security-automation)

* [Video - Python: VirusTotal Lookup Script](https://www.youtube.com/watch?v=D925hYZjKY0&t=359s&ab_channel=EduardMarian)

* [Virustotal Search GitHub Repo](https://github.com/eduardxyz/virustotal-search)

## Staging

* Copy and paste the demo script into a new Python file on your system.

* Download virustotal-search.py and place it in the same folder as the demo Python script.

* Sign up for an account at virustotal.com to get a free API key.

* To query the VirusTotal API, you’ll need to set your API key as an environment variable to avoid hard-coding it into your demo Python script, which is currently set to call “API_KEY_VIRUSTOTAL” in place of your literal API key. You can always hard-code it at first for testing, but don’t leave it that way!

* Set the variable hash to whatever MD5 hash you wish to VirusTotal to evaluate.

*Note that this is one of many ways to interact with the VirusTotal API. If you are an advanced coder, try further optimizing your API query process.*

## Requirements

Add to your malware detection script features to:

* Successfully connect to the VirusTotal API

* Automatically compare your target file’s md5 hash with the hash values of entries on VirusTotal API

* Print to the screen the number of positives detected and total files scanned

The script must successfully execute on both Ubuntu Linux 20.04 Focal Fossa and Windows 10.

  *The best way to start this lab is by confirming you can call virustotal-search.py from your demo.py script and effectively query the VirusTotal API. After that, it’s all about integrating these capabilities into your directory scanner to result in a fully-operational anti-malware tool.*
