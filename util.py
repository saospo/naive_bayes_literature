from urllib import request

from nltk import word_tokenize
from nltk.corpus import gutenberg, stopwords
from collections import defaultdict


def pull_gutenberg(url):
    """given the url of a .txt version of a gutenberg book, pulls the length of the book into a string"""
    response = request.urlopen(url)
    raw = response.read().decode("utf8")

    return raw


def stopword_counts(chapters, punctuation = False):
    """gives counts of all stopwords in all chapters of a book, separated by chapter.
        can set flag to give counts of punctuation as well"""
    stops_by_chapter = []

    stop_words = set(stopwords.words('english'))

    if punctuation:
        print("right now this does nothing\n")

    for index in range(0, len(chapters)):

        temp_stops_in_chapter = defaultdict(int)

        chapter = word_tokenize(chapters[index])
        for word in chapter:
            if word in stop_words:
                temp_stops_in_chapter[word] += 1

        stops_by_chapter.append(temp_stops_in_chapter)

    return stops_by_chapter