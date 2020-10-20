from urllib.request import urlretrieve
import os 
with open("Alenwalker.txt","r") as f:
   for line in f.readlines():
        urls = line.split('/')[-1]
        name = urls.replace("%20"," ")
        fullname = os.path.join("cerMusic/AlenWalker/",name)
        print(name)
        urlretrieve(line,fullname)
