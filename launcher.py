# -*- coding: utf-8 -*-

#### pastlauncher #####

# Setup logging
import logging, os, sys
try: os.remove("latest.log")
except: pass
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
file_handler = logging.FileHandler("latest.log")
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(stdout_handler)
logger.debug("Logging enabled.")

logger.info("Loading pastlauncher...")

# Detect OS
import platform
global system; system = platform.system()
logger.debug("OS detected: " + str(system))

import subprocess # Import module for command execution

# Create the devnull
global devnull; devnull = open(os.devnull, "w")
logger.debug("Devnull created.")

# Encoding tweaks for Windows
if system == "Windows":
    try:
        subprocess.check_call(["chcp", "65001"], shell=True, stdout=devnull)
    except:
        pass
    try:
        subprocess.check_call(["set", '"PYTHONIOENCODING=UTF-8"'], shell=True, stdout=devnull)
    except:
        pass

# Get time
from datetime import datetime
global time_now; time_now = datetime.now()
global time_hms; time_hms = time_now.strftime("%H:%M:%S")
global time_hm; time_hm = time_now.strftime("%H:%M")
logger.debug("Got time.")
