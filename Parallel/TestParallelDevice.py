import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy





def test_dologin(appium_driver):
    driver = appium_driver
    driver.get("http://google.com")
    driver.find_element(AppiumBy.XPATH, "//*[@name='q']").send_keys("hello Appium")
    print(driver.title)
    time.sleep(2)
    driver.quit()