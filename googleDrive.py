import requests
from bs4 import BeautifulSoup
from math import inf

r = requests.get('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub')

# F
#r = requests.get('https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub')
soup = BeautifulSoup(r.content, 'html.parser')

tableRows = soup.find('table').find_all('tr')

#Initialize arrays to store 
xCo=[]
unicodeCharacter=[]
yCo=[]

maxXCo=0
maxYCo=0

for row in enumerate(tableRows[1:]):
    elements=row[1].find_all('p')
    tempXCo = int(elements[0].getText())
    if(tempXCo>maxXCo):
        maxXCo=tempXCo

    xCo.append(tempXCo)
    unicodeCharacter.append(elements[1].getText())
    tempYCo = int(elements[2].getText())
    if(tempYCo>maxYCo):
        maxYCo=tempYCo
    yCo.append(tempYCo)

graphCol=maxXCo+1
graphRow=maxYCo+1

graph=[[' ' for _ in range(graphCol)] for _ in range(graphRow)]

numCol = len(graph[0])

numRow = len(graph)


lengthXCo = len(xCo)

for x in range(lengthXCo):
    graph[maxYCo-yCo[x]][xCo[x]] = unicodeCharacter[x]

for row in graph:
    print(''.join(row))