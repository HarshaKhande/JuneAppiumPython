import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy


@pytest.mark.usefixtures("log_on_failure")
def test_dologin(appium_driver):
    driver = appium_driver
    acce = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views")
    acce.click()