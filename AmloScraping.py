from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date, datetime
import csv

top_posts = 661
url = 'https://lopezobrador.org.mx/page/'
print(list(range(1, top_posts + 1)))

def getMonth(m):
    months = {'enero':'1', 'febrero':'2',
              'marzo':'3', 'abril':'4',
              'mayo':'5', 'junio':'6',
              'julio':'7','agosto':'8',
              'septiembre':'9','octubre':'10',
              'noviembre':'11','diciembre':'12'}

    return months[m]

def preprocess_date(d):
    f = d.split(' ')
    date = datetime(year=int(f[2]), month=int(getMonth(f[0])), day=int(f[1].replace(',', '')))

    return date

speechs = []
speech_id = 0

for i in range(1, top_posts + 1):
    print("processing: ", i)
    speech_id += i
    url = 'https://lopezobrador.org.mx/page/' + str(i) + '/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    articles = soup.find_all('div', class_='row isotope-container')
    for s in articles:
        for element in s.findChildren('article'):
            title = element.find_all('h2',class_='entry-title')
            date = element.find_all('span',class_='entry-date')
            dte = preprocess_date(date[0].text) 
            uinternal_url = title[0].find_all('a',href=True)[0]['href']       
            npage = requests.get(uinternal_url)
            nsoup = BeautifulSoup(npage.content, 'html.parser')
            content = nsoup.find_all('div', class_='entry-content')
            if content[0].em is not None:
                content[0].em.clear()
            dct = {'id_speech': speech_id, 'date': dte, 'title': title[0].text , 'url': uinternal_url, 'content': content[0].text}
            speechs.append(dct)
            speech_id += i

print("saving speechs")
keys = speechs[0].keys()
with open('amlo_speechs.csv', 'w', encoding='utf8', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(speechs)    