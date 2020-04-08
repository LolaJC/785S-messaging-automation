""" Messaging automation with an AirCard 785S using selenium """
import logging
import os
import configparser
from selenium import webdriver

# Set logging level to info
logging.basicConfig(level=logging.INFO)

# Use config parser to get passwords from config.ini
CONFIG = configparser.RawConfigParser()

# Get current working directory
CWD = os.getcwd()
logging.info(f"CWD: {CWD}")

# Set paths
PATH_CHROMEDRIVER = '/usr/bin/chromedriver'
CONFIG_FILE_PATH = (os.path.join(CWD, 'config.ini'))

# Get credentials for Aircard Manager
# Try environment variables
try:  
    URL = os.environ["AIRCARD_URL"]
    PASSWORD = os.environ["AIRCARD_PASSWORD"]
except KeyError: 
    logging.info(f"Environment variables are not set")
    # Get credentials from config file
    CONFIG.read(CONFIG_FILE_PATH)
    URL = CONFIG.get('Aircard', 'URL')
    PASSWORD = CONFIG.get('Aircard', 'PASSWORD')
logging.info(f"URL: {URL}")
logging.info(f"PASSWORD: {PASSWORD}")