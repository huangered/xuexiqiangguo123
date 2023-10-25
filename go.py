from selenium import webdriver
from selenium.webdriver.common.by import By

import time


    # read file
    #f = open("all.txt", "rw")
def readDoc():
    option = webdriver.ChromeOptions()

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
        if len(doc1.text) > 6:
            links.append(doc1);
            print("Add title {0}\r\n".format(doc1.text))

    for i in range (0, 8):
        doc1 = links[i]
        doc1.click()


    time.sleep(3)

    windows = driver.window_handles

    print(windows)
    for i in range (1, 11):
        driver.switch_to.window(windows[i])
        time.sleep(5)
        voice = driver.find_element(By.CLASS_NAME, "voice-lang-switch")
        if voice != None:
            print("voice\r\n")
            voice.click()
        time.sleep(70)
        

        
    print("看视频")
    
    
    
if __name__ == "__main__":    
    readDoc()
    time.sleep(1000000)