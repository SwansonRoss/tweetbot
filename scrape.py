# A python webscraper using beautiful soup to get
#   info on Nike's upcoming shoe releases
# h/t: https://hackernoon.com/building-a-web-scraper-from-start-to-finish-bb6b95388184
# v 0.0 - Ross Swanson - 2/24/19

from bs4 import BeautifulSoup
import requests
import json
import twtbot

url         = 'https://www.nike.com/launch/?s=upcoming'
response    = requests.get(url, timeout=5)
content     = BeautifulSoup(response.content, "html.parser")

snkrArr = []
for snkr in content.findAll('figure', attrs={"class": "pb2-sm"}):
    destination = [a['href'] for a in snkr.findAll('a', href=True)]
    snkrObject = {
        "shoe":     snkr.find('h3', attrs={"class":    "ncss-brand"}).text.encode('utf-8'),
        "name":     snkr.find('h6', attrs={"class":    "ncss-brand"}).text.encode('utf-8'),
        "month":    snkr.find('p', attrs={"class":     "mod-h2"}).text.encode('utf-8'),
        "day":      snkr.find('p', attrs={"class":     "mod-h1"}).text.encode('utf-8'),
        "url":      "http://nike.com/" + destination[0]
    }
    snkrArr.append(snkrObject)


#Pull in existing records
try:
    tmpArr = json.load(open('tweets.json', 'r'))
except:
    tmpArr = []

#add new sneakers to existing JSON
for snkr in snkrArr:
    tmpArr.append(snkr)
    
#Remove duplicates
tmpArr = twtbot.dedupeScrapes(tmpArr)

#store array in JSON file
with open('scrapeData.json', 'w') as outfile:
    json.dump(tmpArr, outfile)
