from core.helpers import *
from core.database.jsondb import JsonDB
import datetime
import string
import sys

# python -m labs.wordcloud

def stripped_string(single_string):
    no_breaks = ' '.join(single_string.splitlines())
    plain_string = re.sub(r"[^a-zA-Z0-9 ]", "", no_breaks)
    string_final = plain_string.strip(string.punctuation)
    return string_final

def main():
    jsondb = JsonDB('data/tweets.json')
    statuses = jsondb.read()
    tweets = []
    for key, data in statuses.items():
        for ind, tweet in enumerate(data):
            text = tweet['text']
            tweets.append(text)

    single_string = str(' '.join(tweets))
    stripped = stripped_string(single_string)
    timestamp = str(datetime.datetime.now().timestamp()).replace('.', '_')
    create_wordcloud(stripped, output=f"news_cloud_{timestamp}.png")


main()
