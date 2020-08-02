""" Module to check a website's status code """
import logging
import os
import configparser
import urllib.request

def check_status_code():
    """
    Checks the website's status code.

    Returns:
        status (str): the websites's status code
    """
    # Set logging level to info
    logging.basicConfig(level=logging.INFO)

    # Use config parser to get passwords from config.ini
    CONFIG = configparser.RawConfigParser()

    # Get current working directory
    CWD = os.getcwd()
    logging.info(f"CWD: {CWD}")

    # Set path
    CONFIG_FILE_PATH = (os.path.join(CWD, 'config.ini'))

    # Get credentials for AirCard Manager
    # Try environment variables
    try:  
        URL = os.environ["AIRCARD_URL"]
    except KeyError: 
        logging.info(f"Environment variables are not set")
        # Get credentials from config file
        try:
            CONFIG.read(CONFIG_FILE_PATH)
            URL = CONFIG.get('AirCard', 'URL')
        except:
            logging.error("config.ini does not exist")
    logging.info(f"URL: {URL}")

    # Return status code
    return f"{urllib.request.urlopen(f'{URL}/index.html').getcode()}"