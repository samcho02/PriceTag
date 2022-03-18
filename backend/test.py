from bs4 import BeautifulSoup as BS
from numpy import column_stack
import requests
import lxml

my = "0613008735418"
url = "https://www.upcitemdb.com/upc/" + my
result = requests.get(url)

doc = BS(result.text, "lxml")

data = []

table = doc.find("table", attrs={'class': 'list' ,'style':'width:100%;'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    colums = row.findAll('td')
    colums = [ele.text.strip() for ele in colums]
    data.append([ele for ele in colums if ele])
    
print(data[0][2])