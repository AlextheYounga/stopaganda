from core.helpers import *
from core.database.jsondb import JsonDB
import datetime
import string
import sys

# python -m scripts.tweets_to_text

def stripped_string(single_string):
    no_breaks = ' '.join(single_string.splitlines())
    plain_string = re.sub(r"[^a-zA-Z0-9 ]", "", no_breaks)
    return plain_string

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
    single_string = str(' '.join(tweets))
    stripped = stripped_string(single_string)
    with open('data/tweets_string.txt', 'w') as f:
        f.write(stripped)
    

main()