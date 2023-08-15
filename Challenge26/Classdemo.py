#!/usr/bin/env python3

# Script Name:                  Event Loggin
# Author:                       Raphael Chookagian
# Date of latest revision:      08/14/2023
# Purpose:                      Create a python script:




# Import libraries
import logging
import os


# Basic config of our logger
logging.basicConfig(filename="demo.log", format='%(asctime)s %(message)s', filemode='w')


# Creating log objects
log = logging.getLogger("my_logger")


log.setLevel(logging.WARNING)


# Generate a set of test log messages
log.debug("Starting debug messages")
log.info("Information messages")
log.warning("Warning messages")
log.error("Error messages")
log.critical("Critical messages")
