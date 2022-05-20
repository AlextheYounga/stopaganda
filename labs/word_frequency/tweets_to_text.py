from core.helpers import *
from datetime import datetime
from ..propaganda.tweets import get_tweets

# python -m labs.word_frequency.tweets_to_text

def stripped_string(single_string):
    no_breaks = ' '.join(single_string.splitlines())
    plain_string = re.sub(r"[^a-zA-Z0-9 ]", "", no_breaks)
    return plain_string

def main():
    tweets = get_tweets()
    single_string = str(' '.join(tweets))
    stripped = stripped_string(single_string)
    timestamp = '{:%Y_%b_%d}'.format(datetime.now())
    with open(f"data/strings/tweets_string_{timestamp}.txt", 'w') as f:
        f.write(stripped)

main()