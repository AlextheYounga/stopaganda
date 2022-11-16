import re

def is_article(word):
    articles = ['the', 'an', 'and', 'a',  'is', 'as', 'are', 'that']
    return word.strip().lower() in articles

def is_preposition(word):
    prepositions = [
        'about',
        'above',
        'across',
        'after',
        'against',
        'among',
        'around',
        'at',
        'before',
        'behind',
        'below',
        'beside',
        'between',
        'by',
        'down',
        'during',
        'for',
        'from',
        'in',
        'inside',
        'into',
        'near',
        'of',
        'off',
        'on',
        'out',
        'over',
        'through',
        'to',
        'toward',
        'under',
        'up',
        'with',
    ]
    return word.strip().lower() in prepositions

def is_pronoun(word):
    pronouns = [
        'he',
        'her',
        'hers',
        'herself',
        'him',
        'himself',
        'his',
        'I',
        'it',
        'itself',
        'many',
        'me',
        'mine',
        'most',
        'myself',
        'she',
        'that',
        'theirs',
        'theirself',
        'theirselves',
    ]
    return word.strip().lower() in pronouns

def strip_urls_from_text(text):
    return re.sub(r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?', '', text, flags=re.MULTILINE)
    