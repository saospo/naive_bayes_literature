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
    chapters = word_tokenize(ourtimes[ourtimes.find("chapter 1"):ourtimes.find("Here ends _The Inquest_")])
    hemingway_ourtimes = stopword_counts(chapters)
    print(hemingway_ourtimes)
    ##############################

    ### MELVILLE -- MOBY DICK ###
    white_whale = gutenberg.words("melville-moby_dick.txt")
    print(len(white_whale))
    # need to just .join here because white_whale ends up being a list of words
    # if it's a string then at least word_tokenize() will work on it in stopword_counts()
    melville_mobydick = stopword_counts(white_whale)
    print(melville_mobydick)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    main()
