from selenium import webdriver
from pprint import pprint
import time

from main import get_schemes, ROOT_URL

# ROOT_URL = "https://gueedc.gujarat.gov.in/"
myoptions = webdriver.ChromeOptions()
service = webdriver.chrome.service.Service(
    "C:/Users/prodo/.wdm/drivers/chromedriver/win32/106.0.5249.61/chromedriver.exe")

schemes = get_schemes()

prefs = {
    "translate_whitelists": {"gu": "en"},
    "translate": {"enabled": "true"},
    "profile.managed_default_content_settings.images": 2,
    'profile.managed_default_content_settings.stylesheet': 2,
    'profile.managed_default_content_settings.css': 2
}

myoptions.add_experimental_option("prefs", prefs)
# initialise with custom service
driver = webdriver.Chrome(service=service, options=myoptions)
# driver = webdriver.Chrome("C:/Users/prodo/.wdm/drivers/chromedriver/win32/106.0.5249.61/chromedriver.exe",
#                           options=myoptions)

driver.get(list(schemes.values())[0])
time.sleep(50)
