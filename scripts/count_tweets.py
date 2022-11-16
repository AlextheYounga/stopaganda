from helpers.db import get_tweets

# python -m scripts.count_tweets

def main():
    tweets = get_tweets()
    print(len(tweets))
    

main()