from collections import Counter
import json
from core.helpers import get_latest_file
from .utils import *

# python -m labs.word_frequency.word_ranks

def remove_unwanted(lexicon):
    new_lexicon = []
    for word in lexicon:
        if (is_preposition(word) or is_article(word) or is_pronoun(word)):
            continue
        new_lexicon.append(word)
    return new_lexicon


def count_frequency(lexicon):
    lexicon = remove_unwanted(lexicon)
    counts = Counter(lexicon).most_common(500)
    counts = dict((k[0], k[1:][0]) for k in counts)  # Converting Python's most_common results into dictionary

    return counts


def word_analyzer(lexicon):
    frequency = count_frequency(lexicon)
    print(json.dumps(frequency, indent=1))


def main():
    lexicon = []
    full_text = ""
    latest_string = get_latest_file('data/strings/*')

    if (latest_string):
        txt = open(latest_string, 'r').read()
        lexicon.extend(txt.split())  # converting string into list
        word_analyzer(lexicon)
    
