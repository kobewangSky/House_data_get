import requests
from bs4 import BeautifulSoup

html = 'https://www.realestate.com.au/sold/property-unit+apartment-with-2-bedrooms-in-melbourne,+vic+3000/list-1?numParkingSpaces=1&numBaths=2&activeSort=price-desc&source=refinement'

res = requests.get(html)

soup = BeautifulSoup(res.text, 'lxml')

for item in soup.select('.residential-card--compressed-view'):
    print item.select('.property-price')