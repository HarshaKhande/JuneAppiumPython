import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(


    deviceName='emulator-5554',
    platformName='Android',
    browserName='Chrome',
    automationName = 'UIAutomator2'

)

# bind these caps to uiautomator2 options

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options = capabilities_options)
driver.get("http://google.com")
driver.find_element(AppiumBy.XPATH,"//*[@name='q']").send_keys("hello Appium")
print(driver.title)
time.sleep(2)
driver.quit()



