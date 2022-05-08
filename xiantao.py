import requests
from lxml import html
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time 

LOGIN_URL = "https://www.xiantao.love/login"
URL = "https://www.xiantao.love/writings"

username = input("Input your username: ")
password = input("Input your password: ")
key = input("Input the key: ")
def main():    
    #browser = webdriver.Chrome(ChromeDriverManager().install())
    driver_path = r'C:\Users\DELL\.wdm\drivers\chromedriver\win32\100.0.4896.60\chromedriver.exe'
    s = Service(driver_path)
    browser = webdriver.Chrome(service=s)
    browser.get(URL) 
    search_place = browser.find_element(By.NAME, 'username') 
    search_place.send_keys(username) 
    search_place = browser.find_element(By.NAME, 'password') 
    search_place.send_keys(password) 
    confirm = browser.find_element(By.CLASS_NAME, 'login-btn')
    confirm.click()
    time.sleep(5)
    search_place = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'writing-inp')))
    search_place.clear()
    search_place.send_keys(key) 
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-btn'))).click()
    time.sleep(3)
    for example in browser.find_elements(By.XPATH, '//div[@class="tool-title-text cur-pointer text-justify-t-e"]'):
        print(example.text)
    #<div data-v-c785b294="" class="tool-title-text cur-pointer text-justify-t-e">Fresh/frozen <span class="highlight">tumor</span> specimen procurement is not part of the routine clinical and diagnostic practice in most institutions and for some <span class="highlight">tumor</span> types (e.g. small <span class="highlight">tumors</span> or <span class="highlight">tumors</span> where near complete sampling is required for histopathology) fresh/frozen samples cannot be obtained.</div>

if __name__ == '__main__':
    main()
