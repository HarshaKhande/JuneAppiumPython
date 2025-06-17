import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

#https://monfared.medium.com/gestures-in-appium-part2-tap-double-tap-multi-finger-6d89451260cf#7c85

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
driver = webdriver.Remote('http://127.0.0.1:4723', options = capabilities_options)


element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Views')

# --- Get the center of the element ---
rect = element.rect
x = rect['x'] + rect['width'] // 2
y = rect['y'] + rect['height'] // 2

# --- Set up W3C Touch Actions ---
touch = PointerInput(kind="touch", name="finger")
actions = ActionBuilder(driver, mouse=touch)
actions.clear_actions()

# --- First tap ---
actions.pointer_action.move_to_location(x, y)
actions.pointer_action.pointer_down()
actions.pointer_action.pointer_up()

# --- Small pause between taps ---
#actions.pointer_action.pause(0.1)



# --- Second tap ---
actions.pointer_action.move_to_location(x, y)
actions.pointer_action.pointer_down()
actions.pointer_action.pointer_up()

# --- Execute the double tap ---
actions.perform()

appium_service.stop



