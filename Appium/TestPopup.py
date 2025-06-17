import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()

acce = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Accessibility")

# Get coordinates
rect = ok_button.rect
x = rect['x'] + rect['width'] // 2
y = rect['y'] + rect['height'] // 2

# Perform tap using W3C
touch = PointerInput(kind="touch", name="finger")
actions = ActionBuilder(driver, mouse=touch)
actions.pointer_action.move_to_location(x, y)
actions.pointer_action.pointer_down()
actions.pointer_action.pointer_up()
actions.perform()



appium_service.stop



