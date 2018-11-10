# Competitive-Spying

The crawler scrapes the quotes from the Payment website and cleans the variables to find the accurate payment amount and the currency. 

Using this the real-time exchange rate sourced through XE API, the spread is calculated (https://github.com/Ezhilvel/Competitive-Spying/blob/master/newpage_xe.py)

> Languages used: **R, Python**
> Packages Used: **Pandas, Numpy, Selenium Webdriver**
> <Scrapy and Beautiful Soup are good web scraping packages available for python, but selenium lets you perform actions> 
> Refer: (https://selenium-python.readthedocs.io/getting-started.html)

For exchange rates, either XE API can be used to extract the exchange rates in bulk or the real-time exchange rate can be extracted from the XE website, which has a fairly simple URL structure. (https://github.com/Ezhilvel/Competitive-Spying/blob/master/XE%20API/xe%20api%20request.docx)
