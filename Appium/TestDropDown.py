import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
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

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Spinner"))'
    ))
)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Spinner").click()
driver.find_element(AppiumBy.XPATH, '//android.widget.Spinner[@resource-id="io.appium.android.apis:id/spinner1"]').click()

time.sleep(2)
driver.find_element(AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="yellow"]').click()
time.sleep(2)



appium_service.stop



