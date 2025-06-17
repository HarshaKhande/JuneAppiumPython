import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(


    deviceName='ca1f79ac',
    platformName='Android',
    appPackage = 'com.oneplus.calculator',
    appActivity = 'com.android.calculator2.Calculator',
    automationName = 'UIAutomator2'

)

appium_service = AppiumService()
appium_service.start()

print(appium_service.is_running)
print(appium_service.is_listening)


# bind these caps to uiautomator2 options

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options = capabilities_options)
time.sleep(2)
driver.find_element(AppiumBy.ID, "com.oneplus.calculator:id/digit_7").click()
time.sleep(2)
driver.find_element(AppiumBy.ID,"com.oneplus.calculator:id/op_add").click()
time.sleep(2)
driver.find_element(AppiumBy.ID, "com.oneplus.calculator:id/digit_3").click()
time.sleep(2)
appium_service.stop



