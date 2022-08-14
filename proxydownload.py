from bs4 import BeautifulSoup
from urllib.request import urlopen,urlretrieve
import urllib.request as request
import re
import requests
from datetime import datetime
from time import time
start = time()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

authinfo = request.HTTPBasicAuthHandler()
proxies = {'https':'https://116.202.13.106:8080'}
proxy_support = request.ProxyHandler(proxies)
opener = request.build_opener(proxy_support, authinfo,
                                     request.CacheFTPHandler)
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
request.install_opener(opener)
html_page = urlopen('https://www.boredpanda.com/woman-portrait-photography-noroc-michaela-north-korea/')
soup = BeautifulSoup(html_page)
images = []
saveloc = "C:\\Users\\Buffalo\\Pictures\\Korean\\" # Save in this location

for img in soup.findAll('img'):
    images.append(img.get('src'))
print(images)

i=0
for link in images:
    if link.find("jpg") !=-1:
        print (link)
        try:
            urlretrieve( link.replace("_296x1000",""),saveloc+ str(i) + ".jpg") # modify this line to match the actual image syntax in your site compared with the printed ones
            
            print (str(i) + ".jpg")
            seconds = time() - start
            print('Time taken to run ' + str(seconds))
            start = time()
        except:
            i=i-1
    else:
        continue
    i=i+1
