from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.support.ui import Select

def get_driver():
    # initialize options
    options = webdriver.ChromeOptions()
    # pass in headless argument to options
    options.add_argument('--headless')
    # initialize driver
    driver = webdriver.Remote(
                command_executor='http://172.20.0.2:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
    return driver


