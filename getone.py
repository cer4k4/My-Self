import os
import bs4
import requests
import lxml
import urllib

masterlink = "http://dl2.beelody.com/Free/?dir=2020/"
downlink = "http://dl2.beelody.com/Free/2020/"

req = requests.get(masterlink,lxml)
soup = bs4.BeautifulSoup(req.text,"html.parser")
if os.path.isfile("playlist.txt") == False:
    os.mknod("playlist.txt")
print("####### These Are Categoris of cerMusic you can chouse it #######")

# This is get all categores
with open("playlist.txt","a")as f:
    for categores in soup.find_all('a',href=True):
        dataname = categores['data-name']+'\n'
        catlink = masterlink+categores['href']+'\n'
        print(dataname)
        f.write(catlink)
    print("####### For exit Program pelease make Ctrl+C #######")
# This get all singer
    singer = input()
    singerlink = masterlink+singer+"/"
    print(singerlink)
    req = requests.get(singerlink,lxml)
    soup = bs4.BeautifulSoup(req.text,"html.parser")
    for allsinger in soup.find_all('a',href=True):
        sngr = allsinger['data-name']+'\n'
        print(sngr)
    print("####### End Please enter you're singer #######")
# Now we get all of song by singer
    album = input()
    albumlink = singerlink+album
    print(albumlink)
    reqsinger = requests.get(albumlink)
    soupsinger = bs4.BeautifulSoup(reqsinger.text,"html.parser")
    for allsong in soupsinger.find_all('a',href=True):
        name = allsong['data-name']+'\n'
        print(name)
    print("####### End of songs #######")
# Download Music One By One
loop = -1
while loop < 0:
    songname = input()
    songlink = downlink+singer+"/"+album.replace(" ","%20").replace("(","%28").replace(")","%29").replace("[","%5B").replace("]","%5D")+"/"+songname.replace(" ","%20")
    path = os.path.join("cerMusic/AlenWalker/",songname)
    print(songlink)
    urllib.request.urlretrieve(songlink,path)
    print("\n\n\n")
    print("####### Easy Easy Tamam Tamam AkA ####### \nlotfan Yek Ahank Dg ro entkhab knid\nYa Ctrl+D Ro begir az barname kharej sho")
    loop -= 1

