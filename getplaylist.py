import os
import bs4
import requests
import lxml

masterlink = "http://dl2.beelody.com/Free/?dir=2020/"
req = requests.get(masterlink,lxml)
os.mknod("playlist.txt")
soup = bs4.BeautifulSoup(req.text)
with open("playlist.txt","w")as f:
    for playlist in soup.find_all('a',href=True):
        dataname = playlist['data-name']+'\n'
        link = masterlink+playlist['href']+'\n'
        print(dataname)
        f.write(dataname)
        print(link)
        f.write(link)
