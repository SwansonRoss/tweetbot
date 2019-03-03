# A python program that uses the tweepy api to 
# post tweets to your twitter account
# v 0.0 - Ross Swanson - 3/03/19
# h/t https://medium.freecodecamp.org/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607

import tweepy
import json
import datetime
import time
import twtbot
import tokens


auth = tweepy.OAuthHandler(tokens.consumer_key, tokens.consumer_secret)
auth.set_access_token(tokens.access_token, tokens.access_token_secret)
api = tweepy.API(auth)

date = datetime.date.today()
today = str(date.year) + "-" + str(date.month) + "-" + str(date.day)

tweetQueue = []

#Pull in existing records
try:
    tmpArr = json.load(open('test.json', 'r'))
except:
    tmpArr = []

with open('test.json') as json_data:
    tweetData = json.load(json_data)

for tweet in tweetData:
    print(tweet['dropDate'])
    print(tweet['wasTweeted'] )
    if((tweet['dropDate'] == today) and (tweet['wasTweeted'] == False)):
        tweetQueue.append(tweet)


for tweet in tweetQueue:
    api.update_status(tweet['tweet'])
    print("tweeted: " + tweet['tweet'] + " at " + str(datetime.date.today()))
    tweet['wasTweeted'] = True
    time.sleep(2)

#add new tweets to existing JSON
for tweet in tweetQueue:
    tmpArr.append(tweet) 
    
#Remove duplicates
tmpArr = twtbot.dedupe(tmpArr)

#store array in JSON filw
with open('test.json', 'w') as outfile:
    json.dump(tmpArr, outfile)

