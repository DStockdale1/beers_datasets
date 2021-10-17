'''
Attempting to make a webscraper for colleting info from untappd

Part 1
  Collect all breweries within Australia with a lower bound of beers (e.g. 50)
  this mean l should have the more stable ones rather than random brewers that only
  make a few beers and are likely out of business

  Will need to this with Selenium as the page loads dynamically

  Put the above into a excel file or data frame

Part 2 -option a
  Input a given search term into the search bar "url"
  Again will need Selenium to load all pages

  Question is do I wat to scrape all of the beers as a ton of them won't be Australian
  and won't be relevant for what l want to do?

  Regardless of the above l'll collect them all and then cross reference them

Part 2 -option b
  From the previous URL list of brewers, open url and add /beer and directly scrape from that
  Will also need a selenium script as page is again dynamic

'''
import re
import xlsxwriter
import os
import requests
import pandas as pd
import math
import webbrowser
import PIL

import time
from time import gmtime
from time import strftime

from bs4 import BeautifulSoup, SoupStrainer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import pyautogui as pyg

# Becuase Selenium has captcha and l can't get through it l need to try something else
# Waht I'm going to try to do is open up a webpage and just scroll through it
# l'll haveto login automatically and do the captcha manually

import requests
import bs4
from bs4 import BeautifulSoup, SoupStrainer


#below works
url = 'https://untappd.com/login?go_to=https%3A%2F%2Funtappd.com%2Fsearch%3Fq%3DAustralia%26type%3Dbrewery'
#driver = webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:/Users/Declan/Downloads/chromedriver_win32_new/chromedriver.exe"))

#webbrowser.get('chrome').open(url)

# clicking on show more buttons
#time.sleep(5.0)
#selenium
driver = webdriver.Chrome("C:/Users/Declan/Downloads/chromedriver_win32_new/chromedriver.exe")


driver.get(url)

time.sleep(1.0)

pyg.moveTo(981, 29) # max brwser
pyg.click()

pyg.write('modgg20000')
time.sleep(0.5)
pyg.press('tab')
pyg.write('nut$$lapthem00n')

pyg.moveTo(468, 483)
pyg.click()

time.sleep(60) # time to do captcha



for i in range(0,round(100/25)): #4867

    pix_test = PIL.ImageGrab.grab(bbox=None).load()[429, 393]
    pyg.press('end')
    pyg.moveTo(426, 374)
    pyg.click()

    pix_test = PIL.ImageGrab.grab(bbox=None).load()[429, 456]

    while int(pix_test[0]) == 245:
        pyg.press('end')

        pix_show_button = PIL.ImageGrab.grab(bbox=None).load()[511,382]
        pix_end_test =  PIL.ImageGrab.grab(bbox=None).load()[376, 396]
        if int(pix_show_button[0]) == 255:
            pyg.moveTo(522, 391)
            pyg.click()

        if int(pix_end_test[0]) == 233:
            #print('finished')
            break


#driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")
source = driver.page_source
soup = BeautifulSoup(source, "html.parser")
print(str(soup).encode('ascii','ignore'))

# above does everything l want

# code below will be impore from new script
