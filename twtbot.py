# Some helper code for scrape, parse, and tweet.py
# v 0.0 - Ross Swanson - 3/03/19

def dedupe(arr):
    dedupeArr = { each['tweet'] : each for each in arr}.values()
    return dedupeArr

def dedupeScrapes(arr):
    dedupeArr = { each['url'] : each for each in arr}.values()
    return dedupeArr


def findDayBefore(i, year):
    tweetObj = i
    dropMonth = months.get(i['month'])
    tweetMonth = 12 if (dropMonth == 1) else (dropMonth - 1)
    
    if (dropMonth == 1):
        tweetMonth = 12
        year = year - 1
    else:
        tweetMonth = dropMonth - 1

    if(tweetMonth == 2):
        tweetDay = 28
    elif(tweetMonth == 4 or tweetMonth == 6 or tweetMonth == 9 or tweetMonth == 11):
        tweetDay = 30
    else:
        tweetDay = 31

    tweetDate = {
        "year": str(year),
        "month": str(tweetMonth),
        "day": str(tweetDay)
    }

    return tweetDate

months = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}