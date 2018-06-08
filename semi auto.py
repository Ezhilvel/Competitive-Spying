"""
Created on Thu Jun  7 16:31:45 2018
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


#run from this 
driver = webdriver.Chrome("E:\WUBS\chromedriver.exe") 

#list institutes
urls = "https://www.flywire.com/pay/sunyjccresidence"
driver.get(urls)
#list countries
countries = [ "India", "China", "Australia","United States","United Kingdom", "Germany"]
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
    
money = driver.find_element_by_name("transfer[amount_to]")
money.clear()
money.send_keys("1000.00")

driver.get(urls)
#####iterate from here
#for num in range(0,6):
c = countries[5]

c

country = driver.find_element_by_id('transfer_country_from_id').send_keys(c)

money = driver.find_element_by_name("transfer[amount_to]")
money.clear()
money.send_keys("1000.00")
    
#if c == 'China':
elements = driver.find_elements_by_xpath("//td [@class='pricing_setting_savings']")

#else:       
elements = driver.find_elements_by_xpath("//td [@class='centered pricing_setting_savings']")

elements
            
for e in elements:
    attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', e)
    print(attrs['data-country_from'])     
            
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

res = vstack((school_ID, institute,From_Country,Deal_CCY, Settelemnt_CCY, Amount, Spread, Fee, Pay_Id, mode_id,payment_detail, Pay_Id_2)) 
my_df = pd.DataFrame(res)
my_df
my_df.to_csv('out2.csv', index=False, header=False)


#--------------------------------------------------------------- 



#---------------------------------------------------------------         
paymode = driver.find_elements_by_xpath("//td [@class='payment_details']")
x = 0
for p in paymode:
    x=x+1
    payment_detail.append(p.text)
    Pay_Id_2.append(x)


    
    
string = re.compile(r'transfer_pricing_setting_id$' )  
x =('transfer_amount_to'
'transfer_country_from_id'
's2id_autogen8'
's2id_autogen8_search'
'transfer_pricing_setting_id_29779'
'transfer_pricing_setting_id_29779'
'transfer_pricing_setting_id_225183'
'transfer_pricing_setting_id_225183'
'transfer_pricing_setting_id_28907') 

matches = [y for y in x if string.match(y)]
          
res = vstack((school_ID, institute,From_Country,Deal_CCY, Settelemnt_CCY, Amount, Spread, Fee, Pay_Id, mode_id)) 
my_df = pd.DataFrame(res)
my_df
my_df.to_csv('out.csv', index=False, header=False)

for y in x:
    'transfer_pricing_setting_id' in y

