import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options



@pytest.fixture(params = ["device1", "device2"],scope= "function")
def appium_driver(request):

    if request.param == "device1":
        desired_caps = dict(

        deviceName='ca1f79ac',
        platformName='Android',
        app="C://Users//Harsha Patil//Documents//Appium//ApiDemos-debug.apk",
        automationName='UIAutomator2'
        )
        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4723', options = capabilities_options)

    if request.param == "device2":
        desired_caps = dict(
        deviceName='emulator-5544',
        platformName='Android',
        udid="emulator-5544",
        app="C://Users//Harsha Patil//Documents//Appium//ApiDemos-debug.apk",
        automationName='UIAutomator2',

        )
        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4724', options=capabilities_options)


    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request,appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)







