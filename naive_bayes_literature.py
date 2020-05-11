import argparse
import PyPDF2 as pdf
from util import *
from nltk.corpus import gutenberg


def main():
    ### HEMINGWAY -- OUR TIMES ###
    hemingway_url = "https://www.gutenberg.org/files/61085/61085-0.txt"
    ourtimes = pull_gutenberg(hemingway_url)
    # clears everything after the end of the final chapter (e.g. gutenberg licensing, text from back of book)
    # and before the first
    # then tokenizes the result
    ourtimes = word_tokenize(ourtimes[ourtimes.find("chapter 1"):ourtimes.find("Here ends _The Inquest_")])
    print(len(ourtimes))
    hemingway_ourtimes = stopword_counts(ourtimes)
    print("hemingway_ourtimes\n", hemingway_ourtimes)
    ##############################

    ### MELVILLE -- MOBY DICK ###
    white_whale = gutenberg.words("melville-moby_dick.txt")
    print(len(white_whale))
    # need to just .join here because white_whale ends up being a list of words
    # if it's a string then at least word_tokenize() will work on it in stopword_counts()
    melville_mobydick = stopword_counts(white_whale)
    print("melville_mobydick\n", melville_mobydick)
    ##############################

    ### MELVILLE -- THE APPLE TREE TABLE ###
    bartleby_url = "http://www.gutenberg.org/cache/epub/11231/pg11231.txt"
    bartleby = pull_gutenberg(bartleby_url)
    startindex = bartleby.find("I am a rather elderly man.")
    endindex = bartleby.find("End of Project Gutenberg")
    bartleby = word_tokenize(bartleby[startindex:endindex])
    print(len(bartleby))
    melville_bartleby = stopword_counts(bartleby)
    print("melville_bartleby\n", melville_bartleby)
    ##############################

    ### MELVILLE -- PIERRE ###
    pierre_url = "http://www.gutenberg.org/cache/epub/34970/pg34970.txt"
    pierre = pull_gutenberg(pierre_url)
    startindex = pierre.find("There are some strange summer mornings in the country")
    endindex = pierre.find("End of Project Gutenberg")
    pierre = word_tokenize(pierre[startindex:endindex])
    print(len(pierre))
    melville_pierre = stopword_counts(pierre)
    print("melville_pierre\n", melville_pierre)
    ##############################

    ### CARROLL -- ALICE IN WONDERLAND ###
    wonderland = gutenberg.words("carroll-alice.txt")
    print(len(wonderland))
    # need to just .join here because white_whale ends up being a list of words
    # if it's a string then at least word_tokenize() will work on it in stopword_counts()
    carroll_alice = stopword_counts(wonderland)
    print("carroll_alice\n", carroll_alice)

    ##############################

    ### MILTON -- PARADISE LOST ###
    paradise = gutenberg.words("milton-paradise.txt")
    print(len(paradise))
    # need to just .join here because white_whale ends up being a list of words
    # if it's a string then at least word_tokenize() will work on it in stopword_counts()
    milton_paradise = stopword_counts(paradise)
    print("milton_paradise\n", milton_paradise)
    ##############################


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    main()
