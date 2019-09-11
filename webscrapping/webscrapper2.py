# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 18:21:43 2019

@author: Malinda


"""

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
#url = 'https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq'
response = requests.get(url)


soup = BeautifulSoup(response.text,"html.parser")
alinks = soup.find_all('a')
#print(alinks)


one_a_tag = soup.find_all('a')[36]
link = one_a_tag['href']
print(link)


for i in range(36,len(soup.find_all('a'))+1):
        one_a_tag = soup.find_all('a')[i]
        download_url= 'http://web.mta.info/developers/'+ link
        urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
        time.sleep()