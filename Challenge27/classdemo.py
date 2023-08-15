#!/usr/bin/env python3

# Import libraries
import logging, time, os
import logging.handlers import RotatingFileHandler
import logging.handlers import TimeRotatingFileHandler


# Create logger object
logger = logging.getLogger("my_logger")

logging.basicConfig(filename="demo.log", format='%(asctime)s %(message)s', filemode='w')

logger.setLevel(logging.INFO)

# Create the handler
# handler = RotatingFileHandler('my_logs.log', maxBytes = 20, backupCount = 3)

handler = TimeRotatingFileHandler(filename="my_logs.log", interval = 20%m,  backupCount = 3)

# Telling 
logger.addHandler(handler)

while True:
    time.sleep(1)
    logger.info("This is a test log message")
