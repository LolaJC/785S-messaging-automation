""" Messaging automation with an AirCard 785S using selenium """
import logging
import os
import configparser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def send_message(number, message):
    """
    Sends a message to a given phone number.

    Args:
        number (int): phone number
        message (str): message to send
    Returns:
        result (str): a result message indicating if the 
                      message was properly sent
    """
    # Set logging level to info
    logging.basicConfig(level=logging.INFO)

    # Use config parser to get passwords from config.ini
    CONFIG = configparser.RawConfigParser()

    # Get current working directory
    CWD = os.getcwd()
    logging.info(f"CWD: {CWD}")

    # Set paths
    PATH_CHROMEDRIVER = "/usr/local/bin/chromedriver"
    CONFIG_FILE_PATH = (os.path.join(CWD, 'config.ini'))

    # Get credentials for AirCard Manager
    # Try environment variables
    try:  
        URL = os.environ["AIRCARD_URL"]
        PASSWORD = os.environ["AIRCARD_PASSWORD"]
    except KeyError: 
        logging.info(f"Environment variables are not set")
        # Get credentials from config file
        CONFIG.read(CONFIG_FILE_PATH)
        URL = CONFIG.get('AirCard', 'URL')
        PASSWORD = CONFIG.get('AirCard', 'PASSWORD')
    logging.info(f"URL: {URL}")
    logging.info(f"PASSWORD: {PASSWORD}")

    # Set options for Chrome
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-gpu")

    browser = webdriver.Chrome(
        executable_path=PATH_CHROMEDRIVER, options=opts)

    # Open AirCard's login page
    browser.get(f"http://{URL}/index.html")
    logging.info("Page is open")

    # Login
    browser.find_element_by_id('session_password').send_keys(PASSWORD)
    browser.find_element_by_id('button_login').click()
    logging.info("Connected")

    # Open the messaging page
    browser.get(f"http://{URL}/index.html#sms_compose")

    # Send the message
    browser.find_element_by_id('sms_sendMsg_receiver').send_keys(f"{number}")
    browser.find_element_by_id('sms_sendMsg_text').send_keys(f"{message}")
    form = browser.find_element_by_id('form_mo_sms')
    form.submit()
    logging.info("Sending message")

    # Return a message indicating if the message was sent
    sleep(3)
    try:
        browser.find_element_by_xpath(("//div[@class='active' and "
                                       "@id='dialog_SmsSentOut']"))
        result = "Message was sent"
    except NoSuchElementException:
        result = "There was an error while sending the message"
    logging.warning(f"{result}")

    # Close
    browser.close()

    return f"{result}"
