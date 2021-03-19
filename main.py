from selenium import webdriver
import logging
from dotenv import load_dotenv
import os
from typing import List
import pandas as pd

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

def get_xpath(driver, xpath: str, attr: str = None) -> List[str]:
    elements = driver.find_elements_by_xpath(xpath)
    if attr:
        return [elem.get_attribute(attr) for elem in elements]
    
    return [elem.text for elem in elements]

# get list of 'new arrivals'
driver.get('https://www.footlocker.com/release-dates')
links = get_xpath(driver, '//a[@class="c-release-product-link"]', 'href')
shoe_names = get_xpath(driver, '//a[@class="c-release-product-link"]/p[@class="c-prd-name"]')
df = pd.DataFrame({'links': links, 'shoe_names': shoe_names})
log.info(df)

# # get countdown for this shoe
# for link in links[-2:]:
#     driver.get(link)
#     sold_out = get_xpath(driver, '/div[@class="targetProductDetails-hero]/div/h5')
#     countdown = get_xpath(driver, '//p[@class="CountDownTimer"]')
#     log.info(link)
#     log.info(countdown)
#     log.info(sold_out)

# close out
log.info("Done: closing driver")
driver.close()
