from selenium import webdriver
import logging
from dotenv import load_dotenv
import os
# from selenium.webdriver.common.keys import Keys
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.NOTSET)

load_dotenv(".env.local")
driver_path = os.getenv("DRIVER")
if not driver_path:
    raise Exception("Chrome driver path not found. Please reference SETUP.md")

log.info("Using chrome driver %s", driver_path)

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
driver = webdriver.Chrome(driver_path)  #, options=options)
log.info("Driver initialized")

# driver.get('https://www.google.com/')
# new_arrivals = driver.find_elements_by_xpath(
#     '//div[@class="Band HeroBand Theme--light align-center"]/a/@href')
# log.info(new_arrivals)

log.info("Done: closing driver")
driver.close()
