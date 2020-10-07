from urllib.request import urlretrieve
 
with open("TaylorSweeft.txt","r") as f:
   for line in f.readlines():
        urls = line.split('/')[-1]
        name = urls.replace("%20"," ")
        print(name)
        urlretrieve(line,name)

