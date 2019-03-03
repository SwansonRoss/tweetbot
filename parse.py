# A python program to parse the JSON file created by scrape.py
# and make/store tweet objects
# v 0.0 - Ross Swanson - 3/03/19

import json
import datetime
import twtbot
    
#get the current date
currentDT = datetime.datetime.now()

#Open up your scraped data
with open('scrapeData.json') as json_data:
    jsonData = json.load(json_data)

tweetArr = []

#Loop through scraped data -- create an announcement tweet object and a day-before tweet object
for i in jsonData:
    year = (currentDT.year + 1) if (i['month'] == 'jan' and currentDT.month == 12) else currentDT.year
    tweetObject1 = {
        "dropDate": str(currentDT.year) + "-" + str(currentDT.month) + "-" + str(currentDT.day),
        "tweet": i['shoe'] + i['name'] + "dropping " + i['month'] + " " + i['day'] + " " + i['url'],
        "wasTweeted": False
    }
    tweetArr.append(tweetObject1)
    if (i['day'] == 1):
        dayBefore = twtbot.findDayBefore(i, year)
        tweetObject2 = {
        "dropDate": dayBefore['year'] + "-" + dayBefore['month'] + "-" + dayBefore['day'],
        "tweet": "Dropping Tomorrow: " + i['shoe'] + i['name'] +  " " + i['url'],
        "wasTweeted": False
    }
    tweetObject2 = {
        "dropDate": str(year) + "-" + str(twtbot.months.get(i['month'])) + "-" + str(i['day']),
        "tweet": "Dropping Tomorrow: " + i['shoe'] + i['name'] +  " " + i['url'],
        "wasTweeted": False
    }
    tweetArr.append(tweetObject2)

#Pull in existing records
try:
    tmpArr = json.load(open('tweets.json', 'r'))
except:
    tmpArr = []

#add new tweets to existing JSON
for tweet in tweetArr:
    print(tweet)
    print("\n")
    tmpArr.append(tweet) 
    
#Remove duplicates
tmpArr = twtbot.dedupe(tmpArr)

#store array in JSON filw
with open('tweets.json', 'w') as outfile:
    json.dump(tmpArr, outfile)