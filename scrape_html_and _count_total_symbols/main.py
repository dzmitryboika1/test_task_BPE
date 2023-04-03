import pandas as pd
import requests
import bs4

all_tags_list = []

pd.set_option('display.max_rows', None)

url = 'https://www.python.org/'
source = requests.get(url).text

soup = bs4.BeautifulSoup(source, 'lxml')

for child in soup.recursiveChildGenerator():
    if child.name:
        all_tags_list.append(child.name)

# total tags in source html
print(pd.Series(all_tags_list).value_counts())

# total symbols in source html
print(pd.Series(list(str(soup))).value_counts())
