#!/usr/bin/env python3


# Import library
import logging

# Create my logger object
logger = logging.getLogger('my_logger')

# Create handlers (stream handler / file handler)
terminal_handler = logging.StreamHandler()
file_handler = logging.FileHandler('errors.log')


# Set our levels for the handlers
terminal_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

# Create formatter for log messages
terminal_format = logging.Formatter('%(name)s:%(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Pair up my new formatters with the handlers
terminal_handler.setFormatter(terminal_format)
file_handler.setFormatter(file_format)


# Add handlers to the logger
logger.addHandler(terminal_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning message')
logger.error('This is a error message')


# # Import libraries
# import logging, time, os
# import logging.handlers import RotatingFileHandler
# import logging.handlers import TimeRotatingFileHandler


# # Create logger object
# logger = logging.getLogger("my_logger")

# logging.basicConfig(filename="demo.log", format='%(asctime)s %(message)s', filemode='w')

# logger.setLevel(logging.INFO)

# # Create the handler
# # handler = RotatingFileHandler('my_logs.log', maxBytes = 20, backupCount = 3)

# handler = TimeRotatingFileHandler(filename="my_logs.log", interval = 20%m,  backupCount = 3)

# # Telling 
# logger.addHandler(handler)

# while True:
#     time.sleep(1)
#     logger.info("This is a test log message")
