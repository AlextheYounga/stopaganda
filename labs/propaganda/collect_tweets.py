from services.tweets import Tweets
from core.helpers import *
from core.database.jsondb import JsonDB
import sys
import re

# python -m labs.propaganda.collect_tweets

def strip_unwanted(text):
    text = strip_urls_from_text(text)
    if (text[0] == 'R' and text[1] == 'T'):
        no_rt = text.split('RT', 1)[1]
        text = no_rt.split(':', 1)[1]
    return text.strip()

def main():
    all_tweets = {}
    tweets = Tweets()
    sources = JsonDB('data/sources.json').read()
    jsondb = JsonDB('data/tweets.json')

    for key, info in sources.items():
        handle = info['twitter_handle']
        name = info['name']
        source_tweets = tweets.check_latest_tweets(handle)
        all_tweets[key] = []
        print(f"Getting tweets for {name}")

        for status in source_tweets:
            jstatus = status._json
            id = jstatus['id']
            timestamp = jstatus['created_at']
            text = jstatus['full_text']
            text = strip_unwanted(text)
            status_urls = jstatus['entities'].get('urls', [])
            urls = [e['url'] for e in status_urls]

            tweet = {
                'id': id,
                'name': name,
                'handle': handle,
                'text': text,
                'urls': urls,
                'timestamp': timestamp
            }

            all_tweets[key].append(tweet)
        jsondb.write(all_tweets)


main()
