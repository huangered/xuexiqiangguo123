from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
import platform
import requests
import json

def readFile():
    with open('doc.txt', 'r', encoding='utf-8') as file:
        lines = []
        for line in file:
            line = line.strip()
            lines.append(line)
        return lines

def appendFile(lines):
    with open('doc.txt', 'a', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            file.write("\r\n")

def readDoc():
    titles = readFile()
    option = webdriver.ChromeOptions()
    if platform.system() == "Windows":
        option.add_argument('--user-data-dir=C:\\Users\\pethua01\\AppData\\Local\\Google\\Chrome\\User Data')
        option.add_argument('--profile-directory=Default')
    if platform.system() == "Darwin":
        option.add_argument('--user-data-dir=C:\\Users\\pethua01\\AppData\\Local\\Google\\Chrome\\User Data')
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument('--disable-gpu')
    #option.add_argument("--headless")

    driver = webdriver.Chrome(options=option)

    driver.get("https://www.xuexi.cn")

    driver.maximize_window()

    print("Maximize window")

    time.sleep(5)

    print("读文章")

    # 每天中午操作。
    docs = driver.find_elements(By.CLASS_NAME, "text-link-item-title")

    print(docs)

    links = []

    for doc in docs:
        doc1 = doc.find_element(By.CLASS_NAME, "text-wrap").find_element(By.CLASS_NAME, "text")
        if len(doc1.text) > 6 and doc1.text not in titles:
            links.append(doc1)
            titles.append(doc1.text)
            print("Add title {0}\r\n".format(doc1.text))

    for i in range (0, 8):
        doc1 = links[i]
        doc1.click()
    appendFile(titles[0:8])

    time.sleep(3)

    windows = driver.window_handles

    print(windows)
    for i in range (1, 9):
        driver.switch_to.window(windows[i])
        time.sleep(5)
        try:
            voice = driver.find_element(By.CLASS_NAME, "voice-lang-switch")
            if voice != None:
                print("voice\r\n")
                voice.click()
            time.sleep(70)
        except NoSuchElementException:
            print("Do nothing")
        
def readByApi():
    urls = []
    titles = readFile()
    new_titles = []
    r = requests.get('https://www.xuexi.cn/lgdata/1crqb964p71.json')
    print(r.status_code)
    for item in r.json():
        print("{} {} {}".format(item['title'], item['publishTime'], item['url']))
        if item['title'] not in titles:
            new_titles.append(item['title'])
            urls.append(item['url'])
    appendFile(new_titles)
    # open chrome
    option = webdriver.ChromeOptions()
    if platform.system() == "Windows":
        option.add_argument('--user-data-dir=C:\\Users\\pethua01\\AppData\\Local\\Google\\Chrome\\User Data')
    if platform.system() == "Darwin":
        option.add_argument('--user-data-dir=C:\\Users\\pethua01\\AppData\\Local\\Google\\Chrome\\User Data')
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument('--disable-gpu')
    #option.add_argument("--headless")

    driver = webdriver.Chrome(options=option)

    driver.get("https://www.xuexi.cn")

    driver.maximize_window()

    print("检查是否登录。。。。。。")

    time.sleep(5)

    for url in urls:
        driver.get(url)
        time.sleep(5)
        try:
            voice = driver.find_element(By.CLASS_NAME, "voice-lang-switch")
            if voice != None:
                print("voice\r\n")
                voice.click()
            time.sleep(70)
        except NoSuchElementException:
            print("Do nothing")

if __name__ == "__main__":
    readByApi()
#    readDoc()
#    time.sleep(1000000)