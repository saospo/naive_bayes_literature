import argparse
from util import *
from nltk.corpus import gutenberg
from sklearn.naive_bayes import MultinomialNB
import numpy as np
from scipy.stats import entropy
from random import shuffle


def main():

    ### HEMINGWAY -- THE SUN ALSO RISES ###
    sun_url = "http://gutenberg.ca/ebooks/hemingwaye-sunalsorises/hemingwaye-sunalsorises-00-t.txt"
    sun = pull_gutenberg(sun_url, latin1encoding=True)
    # clears everything after the end of the final chapter (e.g. gutenberg licensing, text from back of book)
    # and before the first
    # then tokenizes the result
    sun = word_tokenize(sun[sun.find("CHAPTER"):sun.find("[End of")])
    hemingway_sun = np.asarray(stopword_probs(sun))
    ##############################

    ### HEMINGWAY -- THE OLD MAN AND THE SEA ###
    oldman_url = "http://gutenberg.ca/ebooks/hemingwaye-oldmanandthesea/hemingwaye-oldmanandthesea-00-t.txt"
    oldman = pull_gutenberg(oldman_url, latin1encoding=True)
    startindex = oldman.find("He was an old man who fished alone")
    endindex = oldman.find("The old man was dreaming about the lions")
    oldman = word_tokenize(oldman[startindex:endindex])
    hemingway_oldman = np.asarray(stopword_probs(oldman))
    ##############################

    ### HEMINGWAY -- AFTER THE STORM ###
    storm_url = "http://gutenberg.ca/ebooks/hemingwaye-oldmanandthesea/hemingwaye-oldmanandthesea-00-t.txt"
    storm = pull_gutenberg(storm_url, latin1encoding=True)
    startindex = storm.find("It wasn")
    endindex = storm.find("[End o")
    storm = word_tokenize(storm[startindex:endindex])
    hemingway_storm = np.asarray(stopword_probs(storm))
    ##############################

    ### MELVILLE -- MOBY DICK ###
    white_whale_url = "https://www.gutenberg.org/files/2701/2701-0.txt"
    white_whale = pull_gutenberg(white_whale_url)
    startindex = white_whale.find("Supplied by a Late Consumptive Usher")
    endindex = white_whale.find("only found another orphan")
    white_whale = word_tokenize(white_whale[startindex:endindex])
    melville_mobydick = np.asarray(stopword_probs(white_whale))
    ##############################

    ### MELVILLE -- BARTLEBY THE SCRIVENER ###
    bartleby_url = "http://www.gutenberg.org/cache/epub/11231/pg11231.txt"
    bartleby = pull_gutenberg(bartleby_url)
    startindex = bartleby.find("I am a rather elderly man.")
    endindex = bartleby.find("End of Project Gutenberg")
    bartleby = word_tokenize(bartleby[startindex:endindex])
    melville_bartleby = np.asarray(stopword_probs(bartleby))
    ##############################

    ### MELVILLE -- PIERRE ###
    pierre_url = "http://www.gutenberg.org/cache/epub/34970/pg34970.txt"
    pierre = pull_gutenberg(pierre_url)
    startindex = pierre.find("There are some strange summer mornings in the country")
    endindex = pierre.find("End of Project Gutenberg")
    pierre = word_tokenize(pierre[startindex:endindex])
    melville_pierre = np.asarray(stopword_probs(pierre))
    ##############################

    ### CARROLL -- ALICE IN WONDERLAND ###
    wonderland_url = "https://www.gutenberg.org/files/11/11-0.txt"
    wonderland = pull_gutenberg(wonderland_url)
    startindex = wonderland.find("Alice was beginning to get very tired of")
    endindex = wonderland.find("and the happy summer days")
    wonderland = word_tokenize(wonderland[startindex:endindex])
    carroll_wonderland = np.asarray(stopword_probs(wonderland))
    ##############################

    ### CARROLL -- THROUGH THE LOOKING GLASS ###
    glass_url = "https://www.gutenberg.org/files/12/12-0.txt"
    glass = pull_gutenberg(glass_url)
    startindex = glass.find("One thing was certain")
    endindex = glass.find("End of the Project Gutenberg")
    glass = word_tokenize(glass[startindex:endindex])
    carroll_glass = np.asarray(stopword_probs(glass))
    ##############################

    ### CARROLL -- SYLVIE AND BRUNO ###
    sylvie_url = "https://www.gutenberg.org/files/620/620-0.txt"
    sylvie = pull_gutenberg(sylvie_url)
    startindex = sylvie.find("LESS BREAD! MORE TAXES!")
    endindex = sylvie.find("End of the Project")
    sylvie = word_tokenize(sylvie[startindex:endindex])
    carroll_sylvie = np.asarray(stopword_probs(sylvie))
    ##############################

    print("data loading done")

    # TODO: multinomialNB: find a way to get a feature array (use .item() from moby dick to search dicts of others?)
    # then run a TON of tests, try to figure out how it does over many iterations

    # everything after this will be test, everything before will be train
    split_index = 1
    # lists to contain the different texts of each author
    hemingway = [hemingway_sun, hemingway_oldman, hemingway_storm]
    melville = [melville_mobydick, melville_bartleby, melville_pierre]
    carroll = [carroll_wonderland, carroll_glass, carroll_sylvie]

    # hemingway is 1, melville is 2, carroll is 3
    # there will always be two works by each author and they will always be presented in the following order
    authorID_array = ([1, 1, 2, 2, 3, 3])

    # number of tests to run set here
    tests = 10

    for index in range(tests):
        shuffle(hemingway)
        shuffle(melville)
        shuffle(carroll)

        training = np.array([hemingway[0], hemingway[1], melville[0], melville[1], carroll[0], carroll[1]])

        #print("\nFor trial ", index, ", multinomialNB predicts:")

    # TODO: KL and proportions. calculate similarity between different author pairs
    # in order to do KL divergence, we need to redo our stopword data as proportions
    # in order to compare the authors at the author level, rather than at the level of works,
    # all of their tokenized works included here are combined before being passed to stopword_probs()
    # additionally, since KL divergence is not a symmetrical metric, we calculate each comparison twice,
    # once from old to new and once from new to old
    # for fun I might add a further calculation which does a proportion based on melville and carroll combined
    hemingway_stop_probs = sun+storm+oldman
    hemingway_stop_probs = hemingway_stop_probs/hemingway_stop_probs.sum()
    melville_stop_probs = white_whale+bartleby+pierre
    melville_stop_probs = melville_stop_probs/melville_stop_probs.sum()
    carroll_stop_probs = wonderland+glass+sylvie
    carroll_stop_probs = carroll_stop_probs/carroll_stop_probs.sum()

    print(hemingway_stop_probs)

    hemingway_v_melville = entropy(hemingway_stop_probs, qk=melville_stop_probs)
    hemingway_v_carroll = entropy(hemingway_stop_probs, qk=carroll_stop_probs)

    melville_v_hemingway = entropy(melville_stop_probs, qk=hemingway_stop_probs)
    melville_v_carroll = entropy(melville_stop_probs, qk=carroll_stop_probs)

    carroll_v_hemingway = entropy(carroll_stop_probs, qk=hemingway_stop_probs)
    carroll_v_melville = entropy(carroll_stop_probs, qk=melville_stop_probs)

    print("Distance of Melville's stop probs from Hemingway's:", hemingway_v_melville)
    print("Distance of Carroll's stop probs from Hemingway's:", hemingway_v_carroll)
    print("Distance of Hemingway's stop probs from Melville's:", melville_v_hemingway)
    print("Distance of Carroll's stop probs from Melville's:", melville_v_carroll)
    print("Distance of Hemingway's stop probs from Carroll's:", carroll_v_hemingway)
    print("Distance of Melville's stop probs from Carroll's:", carroll_v_melville)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    main()
