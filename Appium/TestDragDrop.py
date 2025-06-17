import time

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.action_chains import ActionChains


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

views = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
exp = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Drag and Drop').click()


source = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="io.appium.android.apis:id/drag_dot_1"]')
target = driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="io.appium.android.apis:id/drag_dot_3"]')

# --- Get center coordinates of elements ---
src_rect = source.rect
tgt_rect = target.rect

start_x = src_rect['x'] + src_rect['width'] // 2
start_y = src_rect['y'] + src_rect['height'] // 2

end_x = tgt_rect['x'] + tgt_rect['width'] // 2
end_y = tgt_rect['y'] + tgt_rect['height'] // 2

# --- Set up W3C touch input ---
touch = PointerInput(kind="touch", name="finger")
actions = ActionBuilder(driver, mouse=touch)
actions.clear_actions()
time.sleep(2)


# --- Perform drag-and-drop ---
actions.pointer_action.move_to_location(start_x, start_y)
actions.pointer_action.pointer_down()
actions.pointer_action.pause(0.5)  # Optional: Hold before dragging
time.sleep(2)
actions.pointer_action.move_to_location(end_x, end_y)
actions.pointer_action.pointer_up()

# --- Execute the action ---
actions.perform()


driver.quit()