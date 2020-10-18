import bs4
import requests as r
import lxml

#This Is Request To Example Page Or Site And Get All Data
req = r.get("http://dl2.beelody.com/Free/?dir=2020/8/This%20Is%20Taylor%20Swift%20%5BBeelody%5D",lxml)

soup = bs4.BeautifulSoup(req.text)
#print(soup)
with open('TaylorSweeft.txt','w') as f:
	for links in soup.find_all('a',href=True):
			geturl = 'dl2.beelody.com/Free/'+links['href']+'\n'
			f.write(geturl)
			print('dl2.beelody.com/Free/'+links['href']+'\n')

print("Easy Easy Tamam Tamam AkA")
