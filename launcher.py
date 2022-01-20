# -*- coding: utf-8 -*-

#### pastlauncher #####



# Import definitions
from scripts import definitions as defs

# Detect OS
import platform
global system; system = platform.system()

# Set app ID and title
import ctypes

if system == "Windows":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(defs.appid)

if system == "Windows":
    ctypes.windll.kernel32.SetConsoleTitleA(defs.title + " (Log)") # ANSI
    ctypes.windll.kernel32.SetConsoleTitleW(defs.title + " (Log)") # UNICODE

# Setup logging
import logging, os, sys
try: os.remove(defs.logfile)
except: pass
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
logfile_handler = logging.FileHandler(defs.logfile)
logfile_handler.setLevel(logging.DEBUG)
logger.addHandler(logfile_handler)
logger.addHandler(stdout_handler)
logger.debug("Logging enabled.")

logger.info("Loading " + defs.title + "...")
logger.info("Version: " + defs.verstr)
logger.info("OS: " + str(system).strip())

# Import module for command execution
import subprocess

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

def launchscript(file):
    if system == "Windows":
        file = file + ".bat"
        os.system(file)
    elif system == "Linux":
        file = file + ".sh"
        os.system("sh ./" + file)
    elif system == "Darwin":
        file = file + ".bash"
        os.system("./" + file)

logger.debug("Importing PyQt5...")

# Import PyQt
try:
    from PyQt5 import QtCore, QtGui, QtWidgets, uic
except ImportError:
    launchscript("install")
    logger.info("PyQt wasn't installed, please restart the launcher.")
    sys.exit()

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

logger.debug("Imported PyQt5.")

logger.info("Loading UI...")

global app; app = QApplication(sys.argv)
app.setStyle(defs.skin)

logger.debug("Loading fonts...")

try:
    fontDB = QFontDatabase()
    fontDB.addApplicationFont("fonts/Saira.ttf")
    fontDB.addApplicationFont("fonts/SairaItalic.ttf")
except:
    logger.debug("Couldn't find fonts!")



app.exec()
