install.packages('httr')
library(httr)
url<-"https://www.flywire.com"
html2 <- GET(url)
html2
content2 <- content(html2, as = "text") 
content2
library(XML)
parsedHTML <- htmlParse(content2, asText =TRUE)
parsedHTML
x<- xpathSApply(parsedHTML, "//td [@class='payment_details']", xmlValue)
x
