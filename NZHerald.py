import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://www.nzherald.co.nz/')
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup)

menuBar = soup.find('ul', class_="swiper-wrapper mx-0 h-full items-center").find_all('li')

newsItems = soup.find_all('h3', class_='story-card__heading')

latestNewsHeadings= soup.find_all("div", class_=re.compile(r"^\s*$"))

print(latestNewsHeadings)
#print(newsItems)
allNewsItems=[]

for items in newsItems:
    newsTitle = items.getText()
    #allNewsItems.append(newsTitle)
    #print(newsTitle)

for latestNews in latestNewsHeadings:
    newsTitle=latestNews.getText()
    allNewsItems.append(newsTitle)   

for menuItems in menuBar:
    heading = menuItems.find('span').getText()
    #print(heading)

print(allNewsItems)
