1# This file contains the Command Line Interface (CLI) for
# Common utilities for the program

import os
import logging

# Ensure logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging settings
log_filename = "logs/0.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)
