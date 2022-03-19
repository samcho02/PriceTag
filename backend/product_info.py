from bs4 import BeautifulSoup as BS
import requests
import lxml

## URL Request
my = "810497025840"
url = "https://www.upcitemdb.com/upc/" + my
result = requests.get(url)
doc = BS(result.text, "lxml")

## Lists
data = []
dict = {"Store": [], "Product": [], "Price": []}


table = doc.find("table", attrs={'class': 'list' ,'style':'width:100%;'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')

# finds the colum td
for row in rows:
    colums = row.findAll('td')
    colums = [ele.text.strip() for ele in colums]
    data.append([ele for ele in colums if ele])
    
# Adds Store, Product, Price data to dictionary
for list in data:

    dict["Store"].append(list[0])
    dict["Product"].append(list[1])
    dict["Price"].append(list[2])
    
print(dict)