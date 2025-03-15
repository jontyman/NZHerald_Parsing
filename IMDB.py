import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nzherald.co.nz/')
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup)

menuBar = soup.find('ul', class_="swiper-wrapper mx-0 h-full items-center").find_all('li')

newsItems = soup.find_all('h3', class_='story-card__heading')
print(newsItems)
#print(movieEntries)

#find_all('span').getText()
for menuItems in menuBar:
    heading = menuItems.find('span').getText()
    #print(heading)
#.find_all('div',class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-3713cfda-2 fSzZES cli-title with-margin')
#ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-3713cfda-2 fSzZES cli-title with-margin