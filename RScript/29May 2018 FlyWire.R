install.packages('httr')
library(httr)
url<-"https://www.flywire.com/pay/2daylanguages"
html2 <- GET(url)
html2
content2 <- content(html2, as = "text") 
content2
library(XML)
parsedHTML <- htmlParse(content2, asText =TRUE)
parsedHTML
cbind(xpathSApply(parsedHTML, "//td [@class='centered pricing_setting_savings']", xmlGetAttr, 'data-country_from'),xpathSApply(parsedHTML, "//td [@class='centered pricing_setting_savings']", xmlGetAttr, 'data-school_spread_percentage'), xpathSApply(parsedHTML, "//td [@class='centered pricing_setting_savings']", xmlGetAttr, 'data-currency_from'), xpathSApply(parsedHTML, "//td [@class='centered pricing_setting_savings']", xmlGetAttr, 'data-currency_to'))
