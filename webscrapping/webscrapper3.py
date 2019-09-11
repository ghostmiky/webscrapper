# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:49:03 2019

@author: Malinda
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests


page = requests.get('https://en.wikipedia.org/wiki/Sri_Lanka')
soup = BeautifulSoup(page.content,'html.parser')

#print(soup.prettify())
ps1 = soup.find_all('p')[2].get_text()
ps2 = soup.find_all('p')[3].get_text()
print(ps1+ps2)