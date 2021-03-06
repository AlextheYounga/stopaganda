from datetime import datetime
from services.tweets import Tweets
from core.helpers import *
from core.database.jsondb import JsonDB

def strip_unwanted(text):
    text = strip_urls_from_text(text)
    if (text[0] == 'R' and text[1] == 'T'):
        no_rt = text.split('RT', 1)[1]
        text = no_rt.split(':', 1)[1]
    return text.strip()

def check_if_needs_update():
    today = '{:%Y_%b_%d}'.format(datetime.now())
    latest = get_latest_file('data/tweets/*')
    needs_updating = today not in latest
    return needs_updating

def get_tweets():
    jsondb = JsonDB(get_latest_file('data/tweets/*'))
    statuses = jsondb.read()
    tweets = []
    for key, data in statuses.items():
        for ind, tweet in enumerate(data):
            text = tweet['text']
            tweets.append(text)
    return tweets

def api_fetch_tweets():
    all_tweets = {}
    tweets = Tweets()
    # Handle Json files
    if (check_if_needs_update()):
        timestamp = '{:%Y_%b_%d}'.format(datetime.now())
        tweets_path = f"data/tweets/tweets_{timestamp}.json"
        sources = JsonDB('data/sources.json').read()
        jsondb = JsonDB(tweets_path)

        for key, info in sources.items():
            handle = info['twitter_handle']
            name = info['name']
            source_tweets = tweets.check_latest_tweets(handle)
            all_tweets[key] = []
            print(f"Getting tweets for {name}")

            for status in source_tweets:
                # The undocumented way of getting full text from tweets
                jstatus = status._json
                id = jstatus['id']
                timestamp = jstatus['created_at']
                text = jstatus['full_text']
                # Retweets must be handled slightly differently.
                if (jstatus.get('retweeted_status', False)):
                    text = jstatus['retweeted_status']['full_text']
                text = strip_unwanted(text) # Get that shit out of here
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