import time

import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


@pytest.mark.usefixtures("log_on_failure")
def test_1():
    desired_caps = dict(

    deviceName='ca1f79ac',
    platformName='Android',
    app = "C://Users//Harsha Patil//Documents//Appium//ApiDemos-debug.apk",
    automationName = 'UIAutomator2'

    )

    appium_service = AppiumService()
    appium_service.start()

    print(appium_service.is_running)
    print(appium_service.is_listening)
    global driver

    # bind these caps to uiautomator2 options

    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options = capabilities_options)
    acce = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Accessibily")
    acce.click()



    appium_service.stop



