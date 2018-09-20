# -*- coding: utf-8 -*-
"""
Created on Thu Jun  11  2018
@author: ezhilvel
"""

#importing libs
import selenium
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium import webdriver 
from pprint import pprint
import numpy as np
import pandas as pd
import numpy
from numpy import vstack
from numpy import hstack
import re



urls = ['a','b','c','d','e']
countries = ['India','China','US','UK','Australia']


#init row_number
n=-1
#init variables
institute =  []
school_ID = []
Amount =[]
From_Country = []
Spread = []
Fee = []
Pay_Id = []
Deal_CCY =[]
Settelemnt_CCY = []
mode_id = []

payment_detail = []
Pay_Id_2 = []



for url in urls:
    for country in countries:
        if country == 'China':
            driver = webdriver.Chrome("E:\WUBS\chromedriver.exe") 
            driver.get(urls)
            money = driver.find_element_by_name("transfer[amount_to]")
            money.clear()
            money.send_keys("1000.00")
            country = driver.find_element_by_id('transfer_country_from_id').send_keys(c)
            elements = driver.find_elements_by_xpath("//td [@class='pricing_setting_savings']")
            element = driver.find_element_by_xpath("//td [@class='pricing_setting_savings']")
            attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', e)
            while(attrs['data-country_from'] != country):
                driver.quit()
                driver = webdriver.Chrome("E:\WUBS\chromedriver.exe") 
                driver.get(urls)
                money = driver.find_element_by_name("transfer[amount_to]")
                money.clear()
                money.send_keys("1000.00")
                country = driver.find_element_by_id('transfer_country_from_id').send_keys(c)
                elements = driver.find_elements_by_xpath("//td [@class='pricing_setting_savings']")
                element = driver.find_element_by_xpath("//td [@class='pricing_setting_savings']")
                attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', e)
                
            m=0
            for e in elements:
                attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', e)
                n = n+1
                m = m+1
                print(m)
                institute.append(urls)
                From_Country.append(attrs['data-country_from']) 
                Spread.append(attrs['data-school_spread_percentage'])
                school_ID.append(attrs['data-school_id'])
                Amount.append(attrs['data-amount_to'])
                Fee.append(attrs['data-pt_fees'])
                Pay_Id.append(m)
                Deal_CCY.append(attrs['data-currency_from'])
                Settelemnt_CCY.append(attrs['data-currency_to'])
                mode_id.append(attrs['data-pricing_setting_id'])
        
            paymode = driver.find_elements_by_xpath("//td [@class='payment_details']")
            x = 0
            for p in paymode:
                x=x+1
                print(x)
                payment_detail.append(p.text)
                Pay_Id_2.append(x)
        else:
            driver = webdriver.Chrome("E:\WUBS\chromedriver.exe") 
            driver.get(urls)
            money = driver.find_element_by_name("transfer[amount_to]")
            money.clear()
            money.send_keys("1000.00")
            country = driver.find_element_by_id('transfer_country_from_id').send_keys(c)
            elements = driver.find_elements_by_xpath("//td [@class='centered pricing_setting_savings']")
            element = driver.find_element_by_xpath("//td [@class='centered pricing_setting_savings']")
            attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', e)
            while(attrs['data-country_from'] != country):
                driver.quit()
                driver = webdriver.Chrome("E:\WUBS\chromedriver.exe") 
                driver.get(urls)
                money = driver.find_element_by_name("transfer[amount_to]")
                money.clear()
                money.send_keys("1000.00")
                country = driver.find_element_by_id('transfer_country_from_id').send_keys(c)
                elements = driver.find_elements_by_xpath("//td [@class='pricing_setting_savings']")
                element = driver.find_element_by_xpath("//td [@class='pricing_setting_savings']")
                attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', e)
                
            m=0
            for e in elements:
                attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', e)
                n = n+1
                m = m+1
                print(m)
                institute.append(urls)
                From_Country.append(attrs['data-country_from']) 
                Spread.append(attrs['data-school_spread_percentage'])
                school_ID.append(attrs['data-school_id'])
                Amount.append(attrs['data-amount_to'])
                Fee.append(attrs['data-pt_fees'])
                Pay_Id.append(m)
                Deal_CCY.append(attrs['data-currency_from'])
                Settelemnt_CCY.append(attrs['data-currency_to'])
                mode_id.append(attrs['data-pricing_setting_id'])
        
            paymode = driver.find_elements_by_xpath("//td [@class='payment_details']")
            x = 0
            for p in paymode:
                x=x+1
                print(x)
                payment_detail.append(p.text)
                Pay_Id_2.append(x)

    driver.quit()



res = vstack((school_ID, institute,From_Country,Deal_CCY, Settelemnt_CCY, Amount, Spread, Fee, Pay_Id, mode_id,payment_detail, Pay_Id_2)) 
my_df = pd.DataFrame(res)
my_df
my_df.to_csv('out2.csv', index=False, header=False)
