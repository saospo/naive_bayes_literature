from urllib import request

from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict


def pull_gutenberg(url, latin1encoding=False):
    """given the url of a .txt version of a gutenberg book, pulls the length of the book into a string.
        flag assumes encoding in Latin-1 rather than utf8"""
    response = request.urlopen(url)

    if latin1encoding:
        raw = response.read().decode("latin-1")
    else:
        raw = response.read().decode("utf8")

    return raw


# two flags here: first adds punctuation to the stopword list
# (i think this might have an effect! think of how much longer the sentences are in older literature --
# might result in more semicolons and commas than something like hemingway, where it's extremely short
# and declarative)
# second flag determines whether the return is a list of defaultdicts going by chapter or a
# single defaultdict of stop words for the whole work
def stopword_counts(chapters, punctuation=False):
    """gives counts of all stopwords in a iterable of words.
        can set flag to give counts of punctuation as well.
        """

    stop_words = set(stopwords.words('english'))

    if punctuation:
        print("right now this does nothing, but maybe it will later\n")

    stops_in_work = defaultdict(int)

    for word in chapters:
        if word in stop_words:
            stops_in_work[word] += 1

    return stops_in_work
