from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "8",
    "deviceName": "Android Emulator",
    "app": "/Users/zzohamadro/PycharmProjects/AppiumClassTests/app_binaries/org.wikipedia.apk",
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

"""XPATH
"//android.widget.ImageView[@content-desc = 'Search Wikipedia']"
"""
driver.implicitly_wait(5)
driver.find_element(By.ID, 'org.wikipedia:id/search_container').click()

e = driver.find_element(By.ID, 'org.wikipedia:id/search_src_text')
e.clear()
e.send_keys('Python')

text = driver.find_element(By.ID, 'org.wikipedia:id/page_list_item_title').text

assert 'Python' in text, f"Expected Python to be in {text}"
