import time

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = dict(

    deviceName='ca1f79ac',
    platformName='Android',
    appPackage='com.google.android.dialer',
    appActivity='com.android.dialer.main.impl.MainActivity',
    automationName='UIAutomator2'

)

appium_service = AppiumService()
appium_service.start()

print(appium_service.is_running)
print(appium_service.is_listening)


# bind these caps to uiautomator2 options

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723',options=capabilities_options)
driver.implicitly_wait(10)


element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Ajji"))'
    ))
)

element.click()

driver.quit()