from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

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
driver = webdriver.Remote('http://127.0.0.1:4723',options = capabilities_options)


# Get window size for scrolling
size = driver.get_window_size()
start_x = size['width'] // 2
start_y = int(size['height'] * 0.8)
end_y = int(size['height'] * 0.2)

# Define touch input
finger = PointerInput("touch", "finger1")
actions = ActionBuilder(driver, mouse=finger)

# Perform scroll/swipe gesture
actions.pointer_action.move_to_location(start_x, start_y)
actions.pointer_action.pointer_down()
actions.pointer_action.move_to_location(start_x, end_y)
actions.pointer_action.release()
actions.perform()

appium_service.stop