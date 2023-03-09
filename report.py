from dotenv import load_dotenv
from selenium import webdriver
import time
from urllib.parse import urlparse

import os

load_dotenv()


def login(webdriver, url):
    uri = urlparse(url)
    webdriver.get(f'{uri.scheme}://{uri.netloc}/login')

    webdriver.find_element('id', 'nim').send_keys(
        os.environ['ADMIN_USERNAME'])
    webdriver.find_element('id', 'password').send_keys(
        os.environ['ADMIN_PASSWORD'])

    webdriver.find_element('id', 'submit').click()


def open_post(webdriver, url):
    try:
        webdriver.get(url)
    except Exception:
        return False
    return True


def report_post(url) -> bool:
    if url == '':
        return False

    driver = webdriver.Chrome()

    login(webdriver=driver, url=url)

    status = open_post(webdriver=driver, url=url)
    time.sleep(10)
    driver.close()

    return status
