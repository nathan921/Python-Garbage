__author__ = 'e228596'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys




driver = webdriver.Firefox()
driver.get("http://www.google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("honeywell")
elem.send_keys(Keys.RETURN)



