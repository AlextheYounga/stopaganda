from collections import Counter
import string
from helpers.api import api_fetch_tweets
from helpers.db import get_tweets
from helpers.helpers import *
import re
import json
import spacy


# python -m labs.word_frequency.subjects
# https://subscription.packtpub.com/book/data/9781838987312/2/ch02lvl1sec16/extracting-subjects-and-objects-of-the-sentence

def get_subject_phrase(doc):
    for token in doc:
        if ("subj" in token.dep_):
            subtree = list(token.subtree)
            start = subtree[0].i
            end = subtree[-1].i + 1
            return doc[start:end]


def get_object_phrase(doc):
    for token in doc:
        if ("dobj" in token.dep_):
            subtree = list(token.subtree)
            start = subtree[0].i
            end = subtree[-1].i + 1
            return doc[start:end]


def stripped_string(single_string):
    no_breaks = ' '.join(single_string.splitlines())
    plain_string = re.sub(r"[^a-zA-Z0-9 ]", "", no_breaks)
    string_final = plain_string.strip(string.punctuation)
    return string_final


def count_frequency(lexicon):
    counts = Counter(lexicon).most_common(500)
    counts = dict((k[0], k[1:][0]) for k in counts)  # Converting Python's most_common results into dictionary

    return counts


def word_analyzer(lexicon):
    frequency = count_frequency(lexicon)
    print(json.dumps(frequency, indent=1))


def main():
    topics = []
    nlp = spacy.load("en_core_web_sm")
    api_fetch_tweets()
    tweets = get_tweets()

    for tweet in tweets:
        doc = nlp(tweet)
        subject_phrase = get_subject_phrase(doc)
        object_phrase = get_object_phrase(doc)

        if (subject_phrase or object_phrase):
            if (subject_phrase and object_phrase):
                topic = f"{subject_phrase} {object_phrase}"
                topics.append(topic)
                continue
            topics.append(subject_phrase or object_phrase)

    word_analyzer(topics)



    
