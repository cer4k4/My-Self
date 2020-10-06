from urllib.request import urlretrieve
with open('TaylorSweeft.txt','r') as f:
	for line in f.readlines():
		url = line.split('/')[-2]
		name = url.replace("%20"," ")
		urlretrieve(line,name)

