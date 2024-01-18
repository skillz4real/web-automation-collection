#from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
import time 
import random
from datetime import datetime

with open("http.txt","r") as f:
    proxies = f.readlines()

i = 0

while (True):
    sleept = random.randint(10,30)
    print(f"sleeping {sleept}s")
    time.sleep(sleept)
    #proxy = random.choice(proxies)
    proxy = "127.0.0.1:9050"

    print(f"using proxy:{proxy}")

    options = uc.ChromeOptions()
    options.add_argument(f"--proxy-server=socks5://{proxy}")
    print("openning browser")
    driver = uc.Chrome(options,headless=True,use_subprocess=False)
    #driver = uc.Chrome(options)

    #driver.get("https://ifconfig.me")
    try:
        driver.get("link.com")
        wait = WebDriverWait(driver, timeout=30, poll_frequency=1,ignored_exceptions = [ElementNotVisibleException, ElementNotSelectableException])

        btn = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/div[3]/div[1]/span")))

        btn.click()

        print("Successful vote")
        print("Logging success")
        with open("success.log", 'a') as l:
            l.write(f"At {datetime.now()}: successful vote with proxy: {proxy}\n")

    except:
        print("something went wrong casting the vote")
        i-= 1
        bad_proxy = proxies.pop(proxies.index((proxy)))

        print("logging bad proxy")
        with open("bad_proxy", "a") as b:
            b.write(bad_proxy)
        
        print("overwriting proxy file")
        with open("http.txt", "w") as h:
            h.writelines(proxies)

    time.sleep(10)

    driver.quit()
    
    i+=1

