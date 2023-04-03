from collections import Counter

import requests
import bs4

all_tags_list = []


url = 'https://www.python.org/'
source = requests.get(url).text

soup = bs4.BeautifulSoup(source, 'lxml')

for child in soup.recursiveChildGenerator():
    if child.name:
        all_tags_list.append(child.name)

# total tags in source html
print(Counter(all_tags_list))

# # total symbols in source html
print(Counter((str(soup))))
