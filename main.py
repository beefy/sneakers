from selenium import webdriver
import logging
from dotenv import load_dotenv
import os
# from selenium.webdriver.common.keys import Keys
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.NOTSET)

# get env variables
load_dotenv(".env.local")
driver_path = os.getenv("DRIVER")
if not driver_path:
    raise Exception("Chrome driver path not found. Please reference SETUP.md")

log.info("Using chrome driver %s", driver_path)

# initialize chrome web driver
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(driver_path, options=options)
log.info("Driver initialized")

# get list of 'new arrivals'
driver.get('https://www.footlocker.com/')
new_arrivals = driver.find_elements_by_xpath(
    '//div[@class="Band HeroBand Theme--light align-center"]/a')
links = [elem.get_attribute('href') for elem in new_arrivals]
log.info("\n".join(links))

# close out
log.info("Done: closing driver")
driver.close()
