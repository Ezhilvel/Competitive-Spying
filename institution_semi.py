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


#run from this 
driver = webdriver.Chrome("E:\WUBS\chromedriver.exe") 

#list institutes
urls = "https://www.flywire.com/pay/2daylanguages"
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

money = driver.find_element_by_name("transfer[amount_to]")
money.clear()
money.send_keys("1000.00")

for num in range(0,6):

    c = countries[num]

    money = driver.find_element_by_name("transfer[amount_to]")
    money.clear()
    money.send_keys("1000.00")

    country = driver.find_element_by_id('transfer_country_from_id').send_keys(c)
    
    if c == 'China':
        elements = driver.find_elements_by_xpath("//td [@class='pricing_setting_savings']")
    else:       
        elements = driver.find_elements_by_xpath("//td [@class='centered pricing_setting_savings']")

    elements
            
    #for e in elements:
        #attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', e)
        #print(attrs['data-country_from'])    
            
    m=0
    for e in elements:
        attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', e)
        n = n+1
        m = m+1
        print(m)
        institute.append(url)
        From_Country.append(attrs['data-country_from']) 
        Spread.append(attrs['data-school_spread_percentage'])
        school_ID.append(attrs['data-school_id'])
        Amount.append(attrs['data-amount_to'])
        Fee.append(attrs['data-pt_fees'])
        Pay_Id.append(m)
        Deal_CCY.append(attrs['data-currency_from'])
        Settelemnt_CCY.append(attrs['data-currency_to'])
            
            
            
res = vstack((school_ID, institute,From_Country,Deal_CCY, Settelemnt_CCY, Amount, Spread, Fee, Pay_Id)) 
my_df = pd.DataFrame(res)
my_df
my_df.to_csv('out.csv', index=False, header=False)



#------------------------------------------------------#------------------------------------------------------   
#------------------------------------------------------#------------------------------------------------------         
for url in urls:
    driver.get(url)
    time.sleep(5)
    money = driver.find_element_by_name("transfer[amount_to]")
    money.clear()
    money.send_keys("1000.00")
    for c in countries:
        country = driver.find_element_by_id('transfer_country_from_id').send_keys(c)
        time.sleep(5) 
        
        if c != 'China':
            elements = driver.find_elements_by_xpath("//td [@class='centered pricing_setting_savings']")
            element = driver.find_element_by_xpath("//td [@class='centered pricing_setting_savings']")
            attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
        
        else:
            elements = driver.find_elements_by_xpath("//td [@class='pricing_setting_savings']")
            element = driver.find_element_by_xpath("//td [@class='centered pricing_setting_savings']")
            attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
        
        
        
        while (attr['data-country_from'] != c): 
            driver.get(url)
            country = driver.find_element_by_id('transfer_country_from_id').send_keys(c)
            money = driver.find_element_by_name("transfer[amount_to]")
            money.clear()
            money.send_keys("1000.00")
            if c != 'China':
                elements = driver.find_elements_by_xpath("//td [@class='centered pricing_setting_savings']")
                element = driver.find_element_by_xpath("//td [@class='centered pricing_setting_savings']")
                attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
            else:
                elements = driver.find_elements_by_xpath("//td [@class='pricing_setting_savings']")
                element = driver.find_element_by_xpath("//td [@class='centered pricing_setting_savings']")
                attr = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
        
        time.sleep(5) 
        m=0
        for e in elements:
            attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', e)
            n = n+1
            m = m+1
            print(m)
            institute.append(url)
            From_Country.append(attrs['data-country_from']) 
            Spread.append(attrs['data-school_spread_percentage'])
            school_ID.append(attrs['data-school_id'])
            Amount.append(attrs['data-amount_to'])
            Fee.append(attrs['data-pt_fees'])
            Pay_Id.append(m)
            Deal_CCY.append(attrs['data-currency_from'])
            Settelemnt_CCY.append(attrs['data-currency_to'])
           

                
res = vstack((institute,From_Country,Spread)) 
my_df = pd.DataFrame(res)
my_df
my_df.to_csv('out.csv', index=False, header=False)


                
#c
#pprint(n)
#pprint(attrs)
#data[2][:]
        #turnover_value = driver.find_elements_by_xpath("//span [@class='pt_amount']")
        #turnover=[]
        #for i in turnover_value:
        #turnover.append(i.text)
        #payment_methods = driver.find_elements_by_xpath("//td [@class='payment_details']")
        #pay_method=[]
        #for pay in payment_methods:
            #data_table[][4].append(pay.text)   
  
 res = vstack((institute,From_Country,Spread)) 
 my_df = pd.DataFrame(res)
 my_df.to_csv('out.csv', index=False, header=False)