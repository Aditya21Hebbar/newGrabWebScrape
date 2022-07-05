import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC



url = 'https://food.grab.com/sg/en/restaurants'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}



def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headers')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  driver.maximize_window()
  return driver 



def get_locs(driver):
  driver.get(url)
  while True:
    try:
      loadMoreButton = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[5]/div[4]/div/div/div[4]/div/button")
      time.sleep(2)
      loadMoreButton.click()
      time.sleep(5)
    except Exception as e:
      print (e)
      break
      print ("Complete")
      time.sleep(10)
      driver.quit()

if __name__ == "__main__":
  driver = get_driver()
  driver.get(url)
  WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[5]/div[4]/div/div/div[4]/div/button")))
  while True:
    try:
        loadMoreButton = driver.find_element_by_xpath("//button[contains(@aria-label,'Load more')]")
        time.sleep(2)
        loadMoreButton.click()
        time.sleep(5)
    except Exception as e:
        print(e)
        break
print("Complete")
time.sleep(10)
