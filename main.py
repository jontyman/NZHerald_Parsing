import requests
from bs4 import BeautifulSoup 


# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='header-main__slider')
#print(s)

#lines=s.find('ul')
#elements = lines.find_all('li')

elements=s.find('ul').find_all('li')

for stuff in elements:
    print(stuff.getText())


# Getting the title tag
#print(soup.title)

# Getting the name of the tag
#print(soup.title.name)

# Getting the name of parent tag
#print(soup.title.parent.name)

# use the child attribute to get 
# the name of the child tag
