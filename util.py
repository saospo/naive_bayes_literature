from urllib import request

from nltk import word_tokenize
from nltk.corpus import gutenberg, stopwords
from collections import defaultdict


def pull_gutenberg(url):
    """given the url of a .txt version of a gutenberg book, pulls the length of the book into a string"""
    response = request.urlopen(url)
    raw = response.read().decode("utf8")

    return raw


# two flags here: first adds punctuation to the stopword list
# (i think this might have an effect! think of how much longer the sentences are in older literature --
# might result in more semicolons and commas than something like hemingway, where it's extremely short
# and declarative)
# second flag determines whether the return is a list of defaultdicts going by chapter or a
# single defaultdict of stop words for the whole work
def stopword_counts(chapters, punctuation=False, by_chapters=False):
    """gives counts of all stopwords in all chapters of a book.
        can set flag to give counts of punctuation as well.
        third tag allows return to separate stopword counts by chapter.

        DO NOT PASS A STRING TO THIS: CHAPTERS MUST BE AN ITERABLE, EVEN IF
        LEN(CHAPTERS) == 1
        """
    # set var which will become return value
    stops = 0

    stop_words = set(stopwords.words('english'))

    if punctuation:
        print("right now this does nothing, but maybe it will later\n")

    # if the flag is set to give a return separated by chapters
    if by_chapters:
        stops_by_chapter = []

        for index in range(0, len(chapters)):

            temp_stops_in_chapter = defaultdict(int)

            chapter = word_tokenize(chapters[index])
            for word in chapter:
                if word in stop_words:
                    temp_stops_in_chapter[word] += 1

            stops_by_chapter.append(temp_stops_in_chapter)

        # assign return value the list of stopword defaultdicts
        stops = stops_by_chapter
    # otherwise, i.e. whole book, return the entire work of stopword counts together
    else:
        stops_in_work = defaultdict(int)

        for index in range(0, len(chapters)):
            chapter = word_tokenize(chapters[index])
            for word in chapter:
                if word in stop_words:
                    stops_in_work[word] += 1

        stops = stops_in_work

    return stops
