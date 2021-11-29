# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 20:15:01 2021

@author: saulb
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import time
import sys
import os
import shutil
import numpy as np
import pandas as pd

#from webdriver_manager.chrome import ChromeDriverManager
#path = "/content/gdrive/MyDrive/Tecnologías de información emergentes/Proyecto/dataset/"
songs = pd.read_csv("songs(1).csv")
songs["index"] = np.array(range(len(songs)))
songs["file"] = ""

webpage = r"https://onlinevideoconverter.pro/en15/youtube-converter-mp3/" # edit me

path = "./dataset/"
pathD = "C:/Users/saulb/Downloads/" 

def search(index):
    searchterm = songs["link"][index]
    
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('.\chromedriver_win32\chromedriver.exe',options=options)
    
    songname = str(index)+".mp3"
    driver.get(webpage)
    
    sbox = driver.find_element(By.ID, "texturl")
    sbox.send_keys(searchterm)
    sbox.send_keys(Keys.RETURN)
    time.sleep(1)
    submit = driver.find_element(By.ID, "convert1")
    submit.send_keys(Keys.ENTER)
    
    #print(sbox.get_attribute("value"))
    
    
    download = None
    while(not download):
      time.sleep(0.25)   
      #driver.refresh()
      prog = driver.find_element(By.CLASS_NAME, "loader-progress")
      if(prog):
        prog_text = prog.text
        if(prog_text):
          done = int(int(prog_text.replace('%', ''))/2)
        else:
          done = 0
        sys.stdout.write("\r[%s%s] %s " % ('=' * done, ' ' * (50-done), songname) )    
        sys.stdout.flush()
      try:
        elements = set(driver.find_elements(By.CLASS_NAME, "start-button"))
        elements = elements.intersection(set(driver.find_elements(By.CLASS_NAME, "disabled")))
        download = None if (not elements) else elements.pop()
      except:
        download = None
    
    download.click()
    #href = download.get_attribute("href")
    #print(download)
    #print(href)
    
    driver.execute_script("window.open()")
    # switch to new tab
    driver.switch_to.window(driver.window_handles[-1])
    # navigate to chrome downloads
    driver.get('chrome://downloads')
    handle = driver.current_window_handle
    title = driver.title
    # define the endTime
    endTime = time.time()+120
    name = ""
    while True:
       try:
            driver.switch_to.window(handle)
            name = driver.execute_script("return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text")
            break
       except:
            pass
       time.sleep(1)
       if time.time() > endTime:
           break
    print(name)
    #driver.get("https://www.youtube.com")
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        driver.close()
    if(name):    
        os.rename(pathD+name, pathD+songname)
        shutil.move(pathD+songname, path+songname)
        songs["file"][index]  = songname
    if(index%20==0):
        songs.to_csv("songs(2).csv")
   
for index in range(36, len(songs)):
    try:
        search(index)
    except:
        pass
        
        
    
songs.to_csv("songs(2).csv")
    
