import json
import os
import sys
import colored
from colored import stylize
from dotenv import load_dotenv
import twitter
import tweepy
load_dotenv()

class Tweets:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(os.environ.get("TWITTER_API_KEY"), os.environ.get("TWITTER_SECRET_KEY"))
        self.auth.set_access_token(os.environ.get("TWITTER_ACCESS_KEY"), os.environ.get("TWITTER_ACCESS_SECRET"))
        self.tweepy = tweepy.API(self.auth)
        self.twitter = twitter.Api(consumer_key=os.environ.get("TWITTER_API_KEY"),
                                   consumer_secret=os.environ.get("TWITTER_SECRET_KEY"),
                                   access_token_key=os.environ.get("TWITTER_ACCESS_KEY"),
                                   access_token_secret=os.environ.get("TWITTER_ACCESS_SECRET"))

    def check_latest_tweets(self, handle):
        timeline = self.tweepy.user_timeline(screen_name=handle, exclude_replies=True, tweet_mode='extended')
        if (timeline):
            return timeline

    def get_tweet(self, tweet_id):
        return self.tweepy.get_status(tweet_id)