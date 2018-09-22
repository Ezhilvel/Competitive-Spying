# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 11:00:25 2018

@author: admin2
"""

"""
Created on Mon Jun 25 12:00:04 2018
@author: admin2
"""


#importing libs
import selenium
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver 
from pprint import pprint
import numpy as np
import pandas as pd
import numpy
from numpy import vstack
from numpy import hstack
import re
import csv

c_ccy = pd.read_csv("E:\WUBS\c_ccy.csv", sep=',')

###########################
#run from this 
driver = webdriver.Chrome("E:\WUBS\chromedriver.exe") 

#list institutes
urls = "https://www.flywire.com/"
driver.get(urls)

##-----------------------------------------------------------------------------------------------------------------------------------
driver.switch_to.window(driver.window_handles[0])
action = ActionChains(driver)
link = driver.find_element_by_tag_name('a')
action.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

sleep(2)
##-----------------------------------------------------------------------------------------------------------------------------------

payment_method = []
pt_amount = []
country = []
institute_name = []
CCY_Full = []
fx_rate = []
To_Currency = []
pt_amount_final = []
EUR_Count= 0
USD_Count= 0

To_CCY = "CAD"
amount = 10000
amount_int = "10000"

Currency_List = ['FJD',	'MXN',	'STD',	'EUR',	'SCR',	'TVD',	'CDF',	'BBD',	'HNL',	'UGX',	'ZAR',	'STN',	'CUC',	'BSD',	'SDG',	'SDG',	'IQD',	'CUP',	'GMD',	'TWD',	'RSD',	'MYR',	'FKP',	'XOF',	'UYU',	'CVE',	'OMR',	'KES',	'SEK',	'BTN',	'GNF',	'MZN',	'MZN',	'SVC',	'ARS',	'QAR',	'IRR',	'EUR',	'XPD',	'THB',	'UZS',	'XPF',	'BDT',	'LYD',	'KWD',	'XPT',	'RUB',	'ISK',	'EUR',	'MKD',	'DZD',	'PAB',	'SGD',	'JEP',	'KGS',	'XAF',	'XAG',	'EUR',	'CHF',	'HRK',	'EUR',	'DJF',	'TZS',	'VND',	'XAU',	'AUD',	'KHR',	'IDR',	'KYD',	'BWP',	'SHP',	'EUR',	'TJS',	'RWF',	'DKK',	'BGN',	'MMK',	'NOK',	'SYP',	'XBT',	'LKR',	'CZK',	'EUR',	'EUR',	'XCD',	'HTG',	'BHD',	'EUR',	'EUR',	'KZT',	'SZL',	'YER',	'AFN',	'AWG',	'NPR',	'MNT',	'GBP',	'BYN',	'HUF',	'BYN',	'BIF',	'XDR',	'BZD',	'MOP',	'NAD',	'EUR',	'TMT',	'PEN',	'WST',	'TMT',	'EUR',	'EUR',	'GTQ',	'CLP',	'EUR',	'TND',	'SLL',	'DOP',	'KMF',	'GEL',	'MAD',	'AZN',	'TOP',	'AZN',	'PGK',	'CNH',	'UAH',	'ERN',	'MRO',	'CNY',	'MRU',	'BMD',	'PHP',	'PYG',	'JMD',	'EUR',	'COP',	'USD',	'GGP',	'ETB',	'VEF',	'SOS',	'VEF',	'VUV',	'LAK',	'BND',	'ZMW',	'LRD',	'ALL',	'GHS',	'EUR',	'ZMW',	'SPL',	'TRY',	'ILS',	'GHS',	'GYD',	'KPW',	'BOB',	'MDL',	'AMD',	'TRY',	'LBP',	'JOD',	'HKD',	'EUR',	'LSL',	'CAD',	'EUR',	'MUR',	'IMP',	'RON',	'GIP',	'RON',	'NGN',	'CRC',	'PKR',	'ANG',	'SRD',	'EUR',	'SAR',	'TTD',	'MVR',	'SRD',	'INR',	'KRW',	'JPY',	'AOA',	'PLN',	'SBD',	'EUR',	'MWK',	'MGA',	'EUR',	'EUR',	'MGA',	'BAM',	'EGP',	'NIO',	'NZD',	'BRL']

 
countries = ['Afghanistan',	'Albania',	'Algeria',	'Angola',	'Argentina',	'Australia',	'Austria',	'Azerbaijan',	'Bahamas',	'Bahrain',	'Bangladesh',	'Barbados',	'Belarus',	'Belgium',	'Bhutan',	'Bolivia',	'Bosnia and Herzegovina',	'Botswana',	'Brazil',	'Brunei Darussalam',	'Bulgaria',	'Burundi',	'Cambodia',	'Cameroon',	'Canada',	'Central African Republic',	'Chad',	'Chile',	'China',	'Colombia',	'Congo',	'Costa Rica',		'Croatia',	'Cyprus',	'Czech Republic',	'Denmark',	'Dominican Republic',	'Ecuador',	'Egypt',	'El Salvador',	'Estonia',	'Ethiopia',	'Fiji',	'Finland',	'France',	'Gabon',	'Gambia',	'Georgia',	'Germany',	'Ghana',	'Gibraltar',	'Greece',	'Grenada',	'Guatemala',	'Guinea',	'Guyana',	'Haiti',	'Honduras',	'Hong Kong',	'Hungary',	'Iceland',	'India',	'Indonesia',	'Iraq',	'Ireland',	'Israel',	'Italy',	'Jamaica',	'Japan',	'Jordan',	'Kazakhstan',	'Kenya',	'Korea, Republic of',	'Kuwait',	'Kyrgyzstan',	'Latvia',	'Lebanon',	'Lithuania',	'Madagascar',	'Malaysia',	'Maldives',	'Malta',	'Mauritius',	'Mexico',	'Moldova, Republic of',	'Monaco',	'Mongolia',	'Montenegro',	'Morocco',	'Mozambique',	'Myanmar',	'Namibia',	'Nepal',	'Netherlands',	'New Zealand',	'Nicaragua',	'Niger',	'Nigeria',	'Norway',	'Oman',	'Pakistan',	'Panama',	'Papua New Guinea',	'Paraguay',	'Peru',	'Philippines',	'Poland',	'Portugal',	'Puerto Rico',	'Qatar',	'Reunion',	'Romania',	'Russian Federation',	'Rwanda',	'Saint Vincent and the Grenadines',	'Saudi Arabia',	'Senegal',	'Serbia',	'Seychelles',	'Singapore',	'Slovakia',	'Slovenia',	'Somalia',	'South Africa',	'Spain',	'Sri Lanka',	'Suriname',	'Sweden',	'Switzerland',	'Syrian Arab Republic',	'Taiwan',	'Tajikistan',	'Tanzania, United Republic of',	'Thailand',	'Trinidad and Tobago',	'Tunisia',	'Turkey',	'Turkmenistan',	'Uganda',	'Ukraine',	'United Arab Emirates',	'United Kingdom',	'United States',	'Uruguay',	'Uzbekistan',	'Venezuela',	'Vietnam',	'Western Sahara',	'Yemen',	'Zambia',	'Zimbabwe']
                    
    
    
for j in range(0,len(countries)) :
    CCY_corrdidor = []
    fx_rate_corridor = []
    driver.switch_to.window(driver.window_handles[0])
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
    elem_6.send_keys(amount_int)
    time.sleep(3)
    elem_7 = driver.find_element_by_class_name("Navigation-slider")
    elem_7.click()
    time.sleep(3)
    ahref = driver.find_elements_by_tag_name("a")
    for a in ahref:
        guest = a.text
        if guest == 'continue as a guest':
            a.click()
    time.sleep(5)
    try:
        elem_9 = driver.find_element_by_class_name("PaymentOptions-showMore")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        elem_9.click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except:
        aa=5
    time.sleep(3)
    elem_7 = driver.find_elements_by_class_name("Offer-name")
    #while(elem_7[-1].text == ''):
        #elem_7 = driver.find_elements_by_class_name("Offer-name")  
    elem_8 = driver.find_elements_by_class_name("Offer-price")
    #while(elem_8[-1].text == ''):
        #elem_8 = driver.find_elements_by_class_name("Offer-name")
    elem_7 = driver.find_elements_by_class_name("Offer-name")
    time.sleep(1)
    elem_8 = driver.find_elements_by_class_name("Offer-price")
    for e in elem_7:
        payment_method.append(e.text)
        country.append(c)  
    for e,f in zip(elem_8,elem_7):
        pt_amount.append(e.text) 
        if e.text == '':
            pt_amount_1 = 0
        else:
            pt_amount_1 = int(''.join(ele for ele in e.text if ele.isdigit()))
            if e.text[:1] == '¥' or f.text[-3:] == 'CLP':
                pt_amount_2 = pt_amount_1
            #elif e.text[0:4] == 'ر.ع.' or e.text[0:3] == 'ب.د' or e.text[-2:] == 'dt' or f.text[-3:] == 'KWD':
            elif e.text[-4:] == '.000' or e.text[-2:] == 'dt':    
                pt_amount_2 = pt_amount_1/1000
            elif f.text[-3:] == 'MGA':
                pt_amount_2 = pt_amount_1/10
            else:
                pt_amount_2 = pt_amount_1/100
        institute_name.append("yyy")
        pt_amount_final.append(pt_amount_2)
        To_Currency.append(To_CCY)
    
    for a,b in zip(elem_7, elem_8):
        c1 = "NAC"
        if a.text == "":
            c1 = "DC"
        elif a.text[0:8] == "Domestic" and c == "India":
            c1 = "INR"
        elif c1 == "NAC" and a.text[-1:] == ")" and a.text[-4:-1] in Currency_List:
            c1 = a.text[-4:-1]
        elif c1 == "NAC" and a.text[-3:] in Currency_List: 
            c1 = a.text[-3:]
        elif c1 == "NAC" and b.text[-1:] == "€":
            c1 = "EUR"
        elif c1 == "NAC" and b.text[:1] == "£":
            c1 = "GBP"
        elif c1 == "NAC" and b.text[-1:] == "£":
            c1 = "GBP"
        elif c1 == "NAC" and b.text[:2] == "R$":
            c1 = "BRL"
        elif c1 == "NAC" and b.text[:2] == "l$":
            c1 = "LRD"
        elif c1 == "NAC" and b.text[:2] == "A$":
            c1 = "AUD"
        elif c1 == "NAC" and b.text[:1] == "$" and ('Canadian' in a.text or c == "Canada"):
            c1 = "CAD"
        elif c1 == "NAC" and b.text[:1] == "$" :
            c1 = "USD"
        elif c1 == "NAC" and a.text[-3:] not in Currency_List: 
            c2 = a.text[-3:]
            xyz = c_ccy.loc[c_ccy['c'] == c, 'CCY'].item() 
            c1 = xyz
        From_CCY = c1
        CCY_corrdidor.append(From_CCY)
        ccy_set = list(set(CCY_corrdidor))
    fx_rate_set = []
    for cs in ccy_set:
        driver.switch_to.window(driver.window_handles[1])
        if cs == To_CCY:
            fx_rate_set.append(amount_int)
        elif cs == 'EUR' and EUR_Count%5 == 0:
            time.sleep(3)
            xe = "https://www.xe.com/currencyconverter/convert/?Amount=" +  amount_int +"&From=" + To_CCY + "&To=" + cs
            driver.get(xe)
            time.sleep(3)
            elem_9 = driver.find_element_by_class_name("converterresult-toAmount")
            time.sleep(3)
            fx_rate_set.append(elem_9.text)
            last_EUR = elem_9.text            
            time.sleep(3)
            EUR_Count = EUR_Count + 1
        elif cs == 'EUR' and EUR_Count%5 != 0:
            fx_rate_set.append(last_EUR)
        elif cs == 'USD' and USD_Count%5 == 0:
            time.sleep(3)
            xe = "https://www.xe.com/currencyconverter/convert/?Amount=" +  amount_int +"&From=" + To_CCY + "&To=" + cs
            driver.get(xe)
            time.sleep(3)
            elem_9 = driver.find_element_by_class_name("converterresult-toAmount")
            time.sleep(3)
            fx_rate_set.append(elem_9.text)
            last_USD = elem_9.text            
            time.sleep(3)
            USD_Count = USD_Count + 1
        elif cs == 'USD' and USD_Count%5 != 0:
            fx_rate_set.append(last_USD)
        elif cs != To_CCY and cs != 'USD' and cs != 'EUR':
            time.sleep(3)
            xe = "https://www.xe.com/currencyconverter/convert/?Amount=" +  amount_int +"&From=" + To_CCY + "&To=" + cs
            driver.get(xe)
            time.sleep(3)
            elem_9 = driver.find_element_by_class_name("converterresult-toAmount")
            time.sleep(3)
            fx_rate_set.append(elem_9.text)
            time.sleep(3)
    for cc in CCY_corrdidor:
        ccy_index = ccy_set.index(cc)
        fx_rate_corridor.append(fx_rate_set[ccy_index])
        CCY_Full.append(cc)
        fx_rate.append(fx_rate_set[ccy_index])
    
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    driver.back()
    time.sleep(1)
    try:
        best_price  = driver.find_element_by_class_name("BestPriceGuaranteed")
        driver.back()
    except:
        aa=5
    time.sleep(3)

#loop over 

#calculating spread and fee    

fee = []
spread = []


for deal, settlemnt, amt, fx in zip(To_Currency,CCY_Full,pt_amount_final, fx_rate):
    fx_int = int(''.join(ele for ele in fx if ele.isdigit()))
    if deal == settlemnt:
        spread.append(0)
        fee.append((amt - fx_int))
    if deal != settlemnt:
        fx_int = fx_int/100
        spread.append((amt - fx_int)/fx_int)
        fee.append(0)   

res__21 = vstack((payment_method,pt_amount, country, institute_name, To_Currency, CCY_Full, pt_amount_final, fx_rate, spread, fee)) 
my_df__21 = pd.DataFrame(res__21)
my_df__22 = my_df__21.T
my_df__22.to_csv('file ggg 10000 full xe.csv', index=False, header=True)


#payment_method_pd = pd.DataFrame(payment_method)
#pt_amount_pd = pd.DataFrame(pt_amount)
#country_pd = pd.DataFrame(country)
#institute_name_pd = pd.DataFrame(institute_name)
#To_Currency_pd = pd.DataFrame(To_Currency)
#CCY_Full_pd = pd.DataFrame(CCY_Full)
#pt_amount_final_pd = pd.DataFrame(pt_amount_final)
#fx_rate_pd = pd.DataFrame(fx_rate)
#spread_pd = pd.DataFrame(spread)
#fee_pd = pd.DataFrame(fee)

#test3 = pd.concat([payment_method_pd,pt_amount_pd, country_pd, institute_name_pd, To_Currency_pd, CCY_Full_pd, pt_amount_final_pd, fx_rate_pd, spread_pd, fee_pd], axis=1)
#test3.to_csv('file_Syracuse 10000 full xe.csv', index=False, header=True)




#### In case of interuption
#pop_n = len(payment_method) - len(CCY_Full)
countries.index(country[-1])

pop_n = country.count(country[-1])
for i in range(0,(pop_n)) :
    payment_method.pop()
    pt_amount.pop()
    country.pop()
    institute_name.pop()