# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:00:04 2018

@author: ezhilvel
"""


#importing libs
import selenium
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver 
from pprint import pprint
import numpy as np
import pandas as pd
import numpy
from numpy import vstack
from numpy import hstack
import re

###########################
#run from this 
driver = webdriver.Chrome("E:\WUBS\chromedriver.exe") 

#list institutes
urls = "https://student.globalpay.wu.com/#!/landing"
driver.get(urls)


payment_method = []
pt_amount = []
country = []
institute_name = []

countries = []

univ_countries = ['Australia','Canada','France','Japan','New Zealand','United Kingdom','United States']

elem_1= []
#country_loop
elem_1 = driver.find_elements_by_xpath("//input [@class='search']")
elem_1[0].clear()
elem_1[0].send_keys("Australia")
time.sleep(1)
elem_1[1].send_keys(Keys.DOWN)
elem_1[0].send_keys(Keys.ENTER)


elem_1[1].clear()  
elem_1[1].send_keys("Academies Australasia Polytechnic")
time.sleep(1)
elem_1[1].send_keys(Keys.DOWN)
elem_1[1].send_keys(Keys.ENTER)

time.sleep(1)
elem_2 = driver.find_element_by_xpath("//button [@class='btn fw btn-custom ng-scope']")
elem_2.click()

time.sleep(1)
elem_3 = driver.find_element_by_xpath("//input [@class='search']")
elem_3.clear()
elem_3.send_keys("Australia")
time.sleep(1)
elem_3.send_keys(Keys.DOWN)
elem_3.send_keys(Keys.ENTER)


elem_4 = driver.find_element_by_xpath("//input [@class='form-control']")
elem_4.clear()
elem_4.send_keys(10000)
time.sleep(1)

elem_5 = driver.find_element_by_xpath("//button [@class='btn fw btn-custom get-quote-btn ng-scope']")
elem_5.click()

########################
for e in elem_9:
    institute = (e.text)
        
elem_2 = driver.find_element_by_id("sender_country")
elem_2.send_keys(Keys.ENTER)
elem_1 = driver.find_elements_by_xpath("//li [@class='Autocomplete-option']")


elem_1 = driver.find_element_by_xpath("//input [@class='search']")

elem_1.send_keys("Australia")
for i in elem_1:
    countries.append(i.text)
 

    
    
for j in range(0,len(countries)) :
    elem_9 = driver.find_elements_by_class_name("Heading")
    while(elem_9 == []):
        driver.back()
        driver.forward()
        j = j+1
        elem_9 = driver.find_elements_by_class_name("Heading")
    c = countries[j]
    elem_9 = driver.find_elements_by_class_name("Heading")
    for e in elem_9:
        institute = (e.text)
    elem_5 = driver.find_element_by_id("sender_country")
    elem_5.send_keys(c)
    elem_5.send_keys(Keys.ENTER)
    elem_6  = driver.find_element_by_id("amount")
    elem_6.clear()
    elem_6.send_keys("10000.00")
    time.sleep(3)
    elem_7 = driver.find_element_by_class_name("Navigation-slider")
    elem_7.click()
    time.sleep(5)
    elem_7 = driver.find_elements_by_class_name("Offer-name")
    elem_8 = driver.find_elements_by_class_name("Offer-price")
    for e in elem_7:
        payment_method.append(e.text)
        country.append(c)  
    for e in elem_8:
        pt_amount.append(e.text) 
        institute_name.append(institute)
    time.sleep(3)
    driver.back()
    time.sleep(3)
    res__15 = vstack((payment_method,pt_amount, country, institute_name)) 






########    

my_df__15 = pd.DataFrame(res__15)
my_df__15
my_df__15.to_csv('file__15.csv', index=False, header=True)

