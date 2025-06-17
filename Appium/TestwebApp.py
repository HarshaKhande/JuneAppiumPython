import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(


    deviceName='ca1f79ac',
    platformName='Android',
    browserName='Chrome',
    automationName = 'UIAutomator2'

)

appium_service = AppiumService()
appium_service.start()

print(appium_service.is_running)
print(appium_service.is_listening)


# bind these caps to uiautomator2 options

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options = capabilities_options)
driver.get("http://google.com")
driver.find_element(AppiumBy.XPATH,"//*[@name='q']").send_keys("hello Appium")
print(driver.title)
time.sleep(2)
driver.quit()

appium_service.stop



