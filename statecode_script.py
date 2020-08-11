from requests import get
url = 'https://abbreviations.yourdictionary.com/articles/state-abbrev.html'
response = get(url)

from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text,'html.parser')

li = [tag.text for tag in html_soup.find_all('li')]

li = li[24:24+50] 

statecode={}
for item in li:
    state,code = item.split(' - ')
    statecode[code] = state

import pickle
with open('statecode.pickle','wb') as handle:
    pickle.dump(statecode,handle)

with open('statecode.pickle','rb') as handle:
    b = pickle.load(handle)
