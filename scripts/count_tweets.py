from core.helpers import *
from core.database.jsondb import JsonDB
from ..labs.propaganda.tweets import get_tweets

# python -m scripts.count_tweets

def main():
    tweets = get_tweets()
    print(len(tweets))
    

main()