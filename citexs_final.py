import requests
from lxml import html
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.mouse import Button, Controller
import time

base_url = 'https://www.citexs.com/AIHelp?keyWord='
key_word = 'cancer'
#key_word = input("Input the keyword: ")
url = base_url + key_word
mouse = Controller()


def main():
    f = open('output.txt', 'w')

    driver_path = r'C:\Users\DELL\.wdm\drivers\chromedriver\win32\100.0.4896.60\chromedriver.exe'
    s = Service(driver_path)
    browser = webdriver.Chrome(service=s)
    browser.get(url)
    browser.maximize_window()
    time.sleep(10)
    browser.get(url)
    time.sleep(2)
    output(browser, f)

    for i in range(1, 20):
        page = browser.find_element(By.CLASS_NAME, 'btn-next')
        browser.execute_script("arguments[0].click();", page)
        time.sleep(5)
        output(browser, f)
    f.close()


def output(browser, f):
    examples = browser.find_elements(By.CLASS_NAME, 'summary_text')
    count = 1
    for example in examples:
        English = example.find_element(By.CLASS_NAME, 'summary')
        print(English.text)
        f.write(English.text + '\n')
        Chinese = example.find_element(By.CLASS_NAME, 'mt-10')
        print(Chinese.text)
        f.write(Chinese.text + '\n')
        xpath = "//div" + "[" + str(count) + "]" + "/div[2]/button[4]/span"
        journal = example.find_element(By.XPATH, xpath)
        print(journal.text)
        f.write(journal.text + '\n')
        full_text = example.find_element(By.LINK_TEXT, '查看全文')
        print(full_text.get_attribute("href"))
        f.write(full_text.get_attribute("href") + '\n')
        xpath = "//div" + "[" + str(count) + "]" + "/div[2]/button[3]/span"
        context_click = example.find_element(
            By.XPATH, xpath)
        browser.execute_script("arguments[0].click();", context_click)
        time.sleep(2)
        context = browser.find_element(By.CLASS_NAME, 'el-dialog__body')
        realtext = context.text
        print(realtext)
        try:
            f.write(realtext + '\n')
        except Exception:
            pass
        f.write("\n")

        mouse.position = (142, 494)
        mouse.press(Button.left)
        mouse.release(Button.left)
        count += 1
        time.sleep(5)


if __name__ == '__main__':
    main()
