from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# fixes the window flashing open then closing issue
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# bypass the connection is not private for unsafe site.
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

service = Service(executable_path=r'./chromedriver_win32/chromedriver')
chrome_browser = webdriver.Chrome(service=service, options=options)

chrome_browser.maximize_window()
chrome_browser.get(r'https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
show_message_btn = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
# print(show_message_btn.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element(By.ID, 'user-message')
user_button = chrome_browser.find_element(By.CSS_SELECTOR, '#get-input > .btn')
print(user_button.text)
user_message.clear()
user_message.send_keys('Testing 123')

time.sleep(2)
show_message_btn.click()
output_message = chrome_browser.find_element(By.ID, 'display')
assert 'Testing 123' in output_message.text
time.sleep(2)

chrome_browser.quit()