from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
try:
    driver.get('https://www.yahoo.co.jp')
    email_input = driver.find_element(By.NAME, 'email')
    password_input = driver.find_element(By.NAME, 'password')
    email_input.send_keys('test1@test.jp')
    password_input.send_keys('test1111')
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()
    time.sleep(5)
    download_link = driver.find_element(By.LINK_TEXT, 'ファイルをダウンロード') 
    download_link.click()
    time.sleep(10)
finally:
    driver.quit()
