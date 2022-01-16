# -*- coding: utf-8 -*-

#### pastlauncher #####

import logging
logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
fh = logging.FileHandler("latest.log")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.debug("Logging enabled.")

logger.info("Loading pastlauncher...")

# Detect OS
import platform
global system; system = platform.system()
logger.debug("OS detected:", system)

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
