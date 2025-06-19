import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

#https://monfared.medium.com/gestures-in-appium-part2-tap-double-tap-multi-finger-6d89451260cf#7c85

desired_caps = dict(


    deviceName='emulator-5554',
    platformName='Android',
    app = "/home/runner/work/JuneAppiumPython/JuneAppiumPython/Appium/ApiDemos-debug.apk",
    automationName = 'UIAutomator2'

)
# bind these caps to uiautomator2 options

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options = capabilities_options)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Controls').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Light Theme').click()

# click on check box button
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Checkbox 1').click()

# click on radio button
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='RadioButton 1').click()
time.sleep(3)






