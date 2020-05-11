import argparse
import PyPDF2 as pdf
from util import *

def main():
    hemingway_url = "https://www.gutenberg.org/files/61085/61085-0.txt"

    ourtimes = pull_gutenberg(hemingway_url)

    print(len(ourtimes))

    # clears everything after the end of the final chapter (e.g. gutenberg licensing, text from back of book)
    chapters = ourtimes.split("Here ends _The Inquest_")

    chapters = chapters[0].split("chapter")

    chapters = chapters[1:]
    chapters = [chapter.strip() for chapter in chapters]

    # should be 18
    print(len(chapters))

    hemingway_ourtimes = stopword_counts(chapters)

    print(hemingway_ourtimes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    main()