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

sender_countries = ['Afghanistan',	'Algeria',	'American Samoa',	'Andorra',	'Angola',	'Anguilla',	'Antarctica',	'Antigua and Barbuda',	'Argentina',	'Armenia',	'Aruba',	'Australia',	'Austria',	'Azerbaijan',	'Bahamas',	'Bahrain',	'Bangladesh',	'Barbados',	'Belarus',	'Belgium',	'Belize',	'Benin',	'Bermuda',	'Bhutan',	'Bolivia',	'Bosnia and Herzegovina',	'Botswana',	'Brazil',	'British India Ocean Territory',	'Brunei Darussalam',	'Bulgaria',	'Burkina Faso',	'Burundi',	'Cambodia',	'Cameroon',	'Canada',	'Cape Verde',	'Cayman Islands',	'Central African Republic',	'Chad',	'Chile',	'China',	'Cocos (Keeling) Islands',	'Colombia',	'Comoros',	'Congo',	'Congo, The Democratic Republic of the',	'Cook Islands',	'Costa Rica',		'Croatia',	'Cyprus',	'Czech Republic',	'Denmark',	'Djibouti',	'Dominica',	'Dominican Republic',	'East Timor',	'Ecuador',	'Egypt',	'El Salvador',	'Equatorial Guinea',	'Eritrea',	'Estonia',	'Ethiopia',	'Falkland Islands (Malvinas)',	'Faroe Islands',	'Fiji',	'Finland',	'France',	'French Guiana',	'French Polynesia',	'French Southern Territories',	'Gabon',	'Gambia',	'Georgia',	'Germany',	'Ghana',	'Gibraltar',	'Greece',	'Greenland',	'Grenada',	'Guadeloupe',	'Guam',	'Guatemala',	'Guernsey, C.I.',	'Guinea',	'Guinea-Bissau',	'Guyana',	'Haiti',	'Heard and McDonald Islands',	'Holy See (Vatican City State)',	'Honduras',	'Hong Kong',	'Hungary',	'Iceland',	'India',	'Indonesia',	'Iraq',	'Ireland',	'Isle of Man',	'Israel',	'Italy',	'Jamaica',	'Japan',	'Jersey, C.I.',	'Jordan',	'Kazakhstan',	'Kenya',	'Kiribati',	'Korea, Republic of',	'Kuwait',	'Kyrgyzstan',		'Latvia',	'Lebanon',	'Lesotho',	'Liberia',	'Libyan Arab Jamahiriya',	'Liechtenstein',	'Lithuania',	'Luxembourg',	'Macau',	'Macedonia, The Former Yugoslav Republic of',	'Madagascar',	'Malawi',	'Malaysia',	'Maldives',	'Mali',	'Malta',	'Marshall Islands',	'Martinique',	'Mauritania',	'Mauritius',	'Mayotte',	'Mexico',	'Micronesia, Federated States of',	'Moldova, Republic of',	'Monaco',	'Mongolia',	'Montenegro',	'Montserrat',	'Morocco',	'Mozambique',	'Myanmar',	'Namibia',	'Nauru',	'Nepal',	'Netherlands',	'Netherlands Antilles',	'New Caledonia',	'New Zealand',	'Nicaragua',	'Niger',	'Nigeria',	'Niue',	'Norfolk Island',	'Northern Mariana Islands',	'Norway',	'Oman',	'Pakistan',	'Palau',	'Palestinian Autonomous Area',	'Panama',	'Papua New Guinea',	'Paraguay',	'Peru',	'Philippines',	'Pitcairn',	'Poland',	'Portugal',	'Puerto Rico',	'Qatar',	'Reunion',	'Romania',	'Russian Federation',	'Rwanda',	'Saint Kitts and Nevis',	'Saint Lucia',	'Saint Vincent and the Grenadines',	'Samoa']

                    
                    
                    
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


time.sleep(1)
elem_3 = driver.find_element_by_xpath("//input [@class='search']")
elem_3.clear()
elem_3.send_keys(sender_countries[0])
time.sleep(1)
elem_3.send_keys(Keys.ENTER)


elem_4 = driver.find_element_by_xpath("//input [@class='form-control']")
elem_4.clear()
elem_4.send_keys(10000)
time.sleep(1)

elem_5 = driver.find_element_by_xpath("//button [@class='btn fw btn-custom get-quote-btn ng-scope']")
elem_5.click()


########################

elem_pt_amount = driver.find_elements_by_class_name("amt")
for amt in range(0,len(elem_pt_amount)):
    if amt%2 == 0:
        pt_amount.append(elem_pt_amount[amt].text)
    
elem_pay_mode = driver.find_elements_by_xpath("//div [@class ='box-logo']")
for mode in elem_pay_mode:
    payment_method.append(mode.text)
    country.append(sender_countries[0])

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



#####
#pt_amount and from_ccy

elem_pt_amount = driver.find_elements_by_xpath("//div [@class ='amt sml ng-bidding']")
for amt in elem_pt_amount:
    pt_amount.append(amt)
    
elem_from_ccy = driver.find_elements_by_xpath("//span [@class ='ng-scope ng-bidding']")
for fccy in elem_from_ccy:
    from_ccy.append(fccy)

#institute_name.append(institute)

#country.append(c)

