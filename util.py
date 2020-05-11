from urllib import request
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import numpy as np


def pull_gutenberg(url, latin1encoding=False):
    """given the url of a .txt version of a gutenberg book, pulls the length of the book into a string.
        flag assumes encoding in Latin-1 rather than utf8"""
    response = request.urlopen(url)

    if latin1encoding:
        raw = response.read().decode("latin-1")
    else:
        raw = response.read().decode("utf8")

    return raw


# takes in a list of documents, 2 from each author (1 held elsewhere for test)
# and uses these to make a sparse array of features for use in a multinomial naive bayes .fit()
def stopword_probs(chapters, punctuation=False, give_proportions=False):
    """gives probability of all stopwords in a iterable of words.
        can set flag to give counts of punctuation as well.
        """
    # take down a list of english stopwords
    featurelist = list(stopwords.words('english'))
    # then make it into a dict, where index is found by the word
    # this allows us to make only one pass through the document at hand,
    # and get a row number quickly regardless of the stopword we are hitting
    featuredict = {featurelist[i]: i for i in range(len(featurelist))}

    if punctuation:
        print("right now this does nothing, but maybe it will later\n")

    total_stops = 0
    stopword_counts = np.zeros(len(featurelist))

    # uses the dictionary of feature words to get a quick lookup of the proper index
    # it ain't pretty but it works
    for word in chapters:
        if word in featurelist:
            index = featuredict[word]
            stopword_counts[index] += 1
            total_stops += 1

    output = stopword_counts

    if give_proportions:
        # now go back over and turn counts into proportions
        print(stopword_counts.sum(), total_stops)

        # Laplace normalizing. there are 179 stopwords.
        stopword_counts = stopword_counts+1
        total_stops + 179

        output = stopword_counts/total_stops

    return output
