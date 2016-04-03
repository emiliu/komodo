import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.inc.com/jeff-haden/100-best-motivational-quotes-to-inspire-anyone.html'
response = requests.get(url)
html = response.content
#print html

soup = BeautifulSoup(html)
table = soup.find('div', attrs={'class': 'article-body inc_editable'})
#print table.prettify
#table = soup.find('li', attrs={'style': 'font-style:inherit'})
#print table#.prettify


list_of_rows = []
for row in table.findAll('li')[1:]:
    list_of_cells = []
    for cell in row.findAll('span'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./quotes.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)