from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import sys
import os


#Enter path to your browser's webdriver, check your browser's version number first
# If you are using windows the add r' at the begining of the path URL as shown below
PATH = r'C:\Users\hamza\Projects\python_projects\cv\fire_project\chromedriver.exe'
driver = webdriver.Chrome(PATH)

img_URL = input('Enter or paste the page URL to be scanned for images \n') 

try:
    if img_URL == '':
        driver.get('https://www.google.com/search?q=cat&sxsrf=ALeKk013s4Rg0Fmazjb899lP1bAXLHc8Lg:1600896156146&source=lnms&tbm=isch&sa=X&ved=2ahUKEwib-9X1moDsAhVMqxoKHY0HCJgQ_AUoAXoECB4QAw&biw=1278&bih=920')
    else:
        driver.get(img_URL)
except:
    print('URL Error')


i = int(input('Enter the number of leading pages to be scanned for images \n'))    
if i == None:
    print('Incorrect number entered')
try:
    while i<5:  
        #page scrol
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        
        try:
            #click on next page or show more results
            driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
        except Exception as e:
            pass
        time.sleep(5)
        i+=1
except:
    print('Incorrect number entered \n')

#parse page
soup = BeautifulSoup(driver.page_source, 'html.parser')


#close browser once search is completed
driver.close()


#urls are scrapped using img tags
img_tags = soup.find_all("img", class_="rg_i")

# count saves the number of images downoaded
count = 0
for i in img_tags:
    
    try:
		#passing image urls one by one and downloading
        urllib.request.urlretrieve(i['src'], str(count) +".jpg")
        count+=1
        print("Number of images downloaded = "+str(count),end='\r')
    except Exception as e:
        pass
