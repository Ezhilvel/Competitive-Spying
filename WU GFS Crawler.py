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
us_univ = ['American Language Academy',	'Barnard College',	'Calvin Christian School',	'Indiana University',	'Purdue University',	'UC Irvine',	'University Of Connecticut',	'University of Washington']

sender_countries = ['Afghanistan',	'Albania',	'Algeria',	'Angola',	'Argentina',	'Australia',	'Austria',	'Azerbaijan',	'Bahamas',	'Bahrain',	'Bangladesh',	'Barbados',	'Belarus',	'Belgium',	'Bhutan',	'Bolivia',	'Bosnia and Herzegovina',	'Botswana',	'Brazil',	'Brunei Darussalam',	'Bulgaria',	'Burundi',	'Cambodia',	'Cameroon',	'Canada',	'Central African Republic',	'Chad',	'Chile',	'China',	'Colombia',	'Congo',	'Costa Rica',		'Croatia',	'Cyprus',	'Czech Republic',	'Denmark',	'Dominican Republic',	'Ecuador',	'Egypt',	'El Salvador',	'Estonia',	'Ethiopia',	'Fiji',	'Finland',	'France',	'Gabon',	'Gambia',	'Georgia',	'Germany',	'Ghana',	'Gibraltar',	'Greece',	'Grenada',	'Guatemala',	'Guinea',	'Guyana',	'Haiti',	'Honduras',	'Hong Kong',	'Hungary',	'Iceland',	'India',	'Indonesia',	'Iraq',	'Ireland',	'Israel',	'Italy',	'Jamaica',	'Japan',	'Jordan',	'Kazakhstan',	'Kenya',	'Korea, Republic of',	'Kuwait',	'Kyrgyzstan',	'Latvia',	'Lebanon',	'Lithuania',	'Madagascar',	'Malaysia',	'Maldives',	'Malta',	'Mauritius',	'Mexico',	'Moldova, Republic of',	'Monaco',	'Mongolia',	'Montenegro',	'Morocco',	'Mozambique',	'Myanmar',	'Namibia',	'Nepal',	'Netherlands',	'New Zealand',	'Nicaragua',	'Niger',	'Nigeria',	'Norway',	'Oman',	'Pakistan',	'Panama',	'Papua New Guinea',	'Paraguay',	'Peru',	'Philippines',	'Poland',	'Portugal',	'Puerto Rico',	'Qatar',	'Reunion',	'Romania',	'Russian Federation',	'Rwanda',	'Saint Vincent and the Grenadines',	'Saudi Arabia',	'Senegal',	'Serbia',	'Seychelles',	'Singapore',	'Slovakia',	'Slovenia',	'Somalia',	'South Africa',	'Spain',	'Sri Lanka',	'Suriname',	'Sweden',	'Switzerland',	'Syrian Arab Republic',	'Taiwan',	'Tajikistan',	'Tanzania, United Republic of',	'Thailand',	'Trinidad and Tobago',	'Tunisia',	'Turkey',	'Turkmenistan',	'Uganda',	'Ukraine',	'United Arab Emirates',	'United Kingdom',	'United States',	'Uruguay',	'Uzbekistan',	'Venezuela',	'Vietnam',	'Western Sahara',	'Yemen',	'Zambia',	'Zimbabwe']
                    
                    
elem_1= []
#country_loop
elem_1 = driver.find_elements_by_xpath("//input [@class='search']")
elem_1[0].clear()
elem_1[0].send_keys("United States")
time.sleep(1)
elem_1[0].send_keys(Keys.ENTER)

elem_1[1].clear()  
elem_1[1].send_keys(us_univ[0])
time.sleep(2)
elem_1[1].send_keys(Keys.ENTER)

time.sleep(1)
elem_2 = driver.find_element_by_xpath("//button [@class='btn fw btn-custom ng-scope']")
elem_2.click()

for j in range(106,len(sender_countries)):
    time.sleep(1)
    elem_3 = driver.find_element_by_xpath("//input [@class='search']")
    elem_3.clear()
    elem_3.send_keys(sender_countries[j])
    time.sleep(1)
    elem_3.send_keys(Keys.ENTER)
    
    
    elem_4 = driver.find_element_by_xpath("//input [@class='form-control']")
    elem_4.clear()
    elem_4.send_keys(10000)
    time.sleep(1)
    
    elem_5 = driver.find_element_by_xpath("//button [@class='btn fw btn-custom get-quote-btn ng-scope']")
    elem_5.click()
       
    ########################    
    time.sleep(15)
    elem_pt_amount = driver.find_elements_by_class_name("amt")
    for amt in range(0,len(elem_pt_amount)):
        if amt%2 == 0:
            pt_amount.append(elem_pt_amount[amt].text)
            institute_name.append("Missouri Western State University")
        
    elem_pay_mode = driver.find_elements_by_xpath("//div [@class ='box-logo']")
    for mode in elem_pay_mode:
        payment_method.append(mode.text)
        country.append(sender_countries[j])
    ########################
    driver.back()
    time.sleep(3)
    kes__5 = vstack((payment_method,pt_amount, country, institute_name)) 
########################


########    

my_df_wu__5 = pd.DataFrame(kes__5)
my_df_wu__5
my_df_wu__5.to_csv('wu_file__5.csv', index=False, header=True)

