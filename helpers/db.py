import os
import json
import glob
from database.jsondb import JsonDB

def read_json_file(filepath):
    txtfile = open(filepath, "r")
    return json.loads(txtfile.read())

def get_latest_file(directory):
    list_of_files = glob.glob(directory)
    if (list_of_files):
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file
    return []

def get_tweets():
    jsondb = JsonDB(get_latest_file('database/storage/tweets/*'))
    statuses = jsondb.read()
    tweets = []
    for key, data in statuses.items():
        for ind, tweet in enumerate(data):
            text = tweet['text']
            tweets.append(text)
    return tweets
