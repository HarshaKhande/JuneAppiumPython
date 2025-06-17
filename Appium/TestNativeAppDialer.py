import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(


    deviceName='ca1f79ac',
    platformName='Android',
    appPackage = 'com.google.android.dialer',
    appActivity = 'com.android.dialer.main.impl.MainActivity',
    automationName = 'UIAutomator2'

)

appium_service = AppiumService()
appium_service.start()

print(appium_service.is_running)
print(appium_service.is_listening)


# bind these caps to uiautomator2 options

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options = capabilities_options)

driver.find_element(AppiumBy.ID, "com.google.android.dialer:id/one").click()
driver.find_element(AppiumBy.ID,"com.google.android.dialer:id/two").click()
driver.find_element(AppiumBy.ID, "com.google.android.dialer:id/three").click()



appium_service.stop



