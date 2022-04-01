from core.helpers import *
from core.database.jsondb import JsonDB
import datetime
import string
import sys

# python -m scripts.count_tweets

def get_tweets():
    jsondb = JsonDB('data/tweets.json')
    statuses = jsondb.read()
    tweets = []
    for key, data in statuses.items():
        for ind, tweet in enumerate(data):
            text = tweet['text']
            tweets.append(text)
    return tweets

def main():
    tweets = get_tweets()
    print(len(tweets))
    

main()