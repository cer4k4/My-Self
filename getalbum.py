import bs4
import requests
import os
import lxml

with open('playlist.txt','r') as f:
    for link in f.readline():
        for i in range (10):
            i = i+1
            if link == i:
                print(link)
