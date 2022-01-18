import os
directory = os.path.expanduser('~/Desktop/switch/switch-engine/')

from bs4 import BeautifulSoup

import csv

index = []

for file in os.listdir(directory):
     doc=open(os.path.join(directory,file),'rb')
     soup=BeautifulSoup(doc,'html.parser', from_encoding="windows-1252")
     title=soup.find(bgcolor='#666666').get_text(":", strip=True)
     author =soup.find(class_='DBoutput').find('table').find('a').get_text(":", strip=True)
     issue =soup.find(class_='DBoutput').find('table').find(align='right').find('a').get_text(":", strip=True)
     date =soup.find(class_='DBoutput').tr.next_sibling.next_sibling.a.next_sibling.replace('\n', '').replace('\r','').replace(' on       ','')
     item =[title, author, issue, date, file]
     index.append(item)

with open("out.csv", "w", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(index)
