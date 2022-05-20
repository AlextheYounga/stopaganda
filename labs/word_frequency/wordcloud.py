from turtle import update
from core.helpers import *
from core.database.jsondb import JsonDB
import datetime
import string
from ..propaganda.fetch_tweets import fetch_tweets, get_latest_tweets_file
    
# import sys
from wordcloud import WordCloud, STOPWORDS

# python -m labs.word_frequency.wordcloud

def stripped_string(single_string):
    no_breaks = ' '.join(single_string.splitlines())
    plain_string = re.sub(r"[^a-zA-Z0-9 ]", "", no_breaks)
    string_final = plain_string.strip(string.punctuation)
    return string_final

def get_tweets():
    jsondb = JsonDB(get_latest_tweets_file())
    statuses = jsondb.read()
    tweets = []
    for key, data in statuses.items():
        for ind, tweet in enumerate(data):
            text = tweet['text']
            tweets.append(text)
    return tweets

def create_wordcloud(text, output):
    mask = np.array(Image.open(path.join(get_project_path(), 'core', 'cloud.png')))

    stopwords = set(STOPWORDS)

    # create wordcloud object
    wc = WordCloud(background_color="white",
                   color_func=lambda *args,
                   **kwargs: "black",
                   mask=mask,
                   stopwords=stopwords)

    wc.generate(text)

    # save wordcloud
    wc.to_file(path.join(get_project_path(), 'core', 'clouds', output))


def main():
    fetch_tweets()
    tweets = get_tweets()
    single_string = str(' '.join(tweets))
    stripped = stripped_string(single_string)
    # timestamp = str(datetime.datetime.now().timestamp()).replace('.', '_')
    timestamp = '{:%Y_%b_%d}'.format(datetime.datetime.now())
    create_wordcloud(stripped, output=f"news_cloud_{timestamp}.png")


main()
