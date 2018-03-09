import bs4 as bs
import urllib.request
import sqlite3

sauce = urllib.request.urlopen('http://store.steampowered.com/search/?specials=1').read()
soup = bs.BeautifulSoup(sauce,'lxml')

spans = soup.find_all('span', {'class' : 'title'})
#for title in spans:
#    print(title.text)

items = {}




divs = soup.find_all('div', {'class' : 'col search_price discounted responsive_secondrow'})

prices = iter(divs)

for n, title in enumerate(spans):
    items[title.text] = next(prices).text.strip()


print(items)
#for x, price in enumerate(divs):
#    items[title.text] = items[price.text]

#for a in divs:
#    print(a.text)
