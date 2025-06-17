import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

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
views = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views")
views.click()
WebView = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "WebView")
WebView.click()

contexts = driver.contexts

for context in contexts:
    print(context)


webview = driver.contexts[1]
driver.switch_to.context(webview)


header = driver.FindElement(By.CssSelector("body>h1"));
print(header.Text);

appium_service.stop



