import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
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

# waits up to 10 seconds for elements to appear
driver.implicitly_wait(10)
acce = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Accessibility")


# explicit wait
element = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((AppiumBy.ID, "Accessibility"))
)


acce.click()

appium_service.stop



