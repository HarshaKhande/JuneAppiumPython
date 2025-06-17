import time

import self
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction


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


# bind these caps to uiautomator2 options

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723',options=capabilities_options)
views = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
exp = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Expandable Lists').click()
custom = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '1. Custom Adapter').click()
element = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="People Names"]')

#https://monfared.medium.com/gestures-in-appium-part3-press-and-hold-long-press-21a0d2727c91

# Create an instance from ActionChains class
actions = ActionChains(driver)

# Create a "touch" type of pointer input. By default it is "mouse"
touch_input = PointerInput(interaction.POINTER_TOUCH, 'touch')

# Override pointer action as 'touch'
actions.w3c_actions = ActionBuilder(driver, mouse=touch_input)

# Press and Hold using W3C actions on first contact
actions.w3c_actions.pointer_action.click_and_hold(element)
actions.perform()

time.sleep(3)



driver.quit()