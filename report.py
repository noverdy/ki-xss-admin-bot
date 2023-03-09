from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from urllib.parse import urlparse

import os

load_dotenv()


def login(webdriver, url):
    try:
        uri = urlparse(url)
        webdriver.get(f'{uri.scheme}://{uri.netloc}/login')

        webdriver.find_element('id', 'nim').send_keys(
            os.environ['ADMIN_USERNAME'])
        webdriver.find_element('id', 'password').send_keys(
            os.environ['ADMIN_PASSWORD'])

        webdriver.find_element('id', 'submit').click()
    except Exception:
        return False
    else:
        return True


def open_post(webdriver, url):
    try:
        webdriver.get(url)
        time.sleep(10)
    except Exception:
        return False
    return True


def report_post(url) -> bool:
    if url == '':
        return False

    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options)

    status = login(webdriver=driver, url=url)
    if not status:
        return status

    status = open_post(webdriver=driver, url=url)
    driver.close()

    return status
