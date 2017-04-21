from tkinter import END

import nltk
from nltk.corpus import wordnet as wn

import Navigate


def synonyms(word):
    word_list = []
    for i, j in enumerate(wn.synsets(word)):
        words = j.lemma_names()
        for item in words:
            if item not in word_list:
                word_list.append(item)
    return word_list


dict = {}


def find_word(word, body, the_text):
    word_list = synonyms(word)


    # iterate through the list of synonyms
    for item in word_list:
        sublist = []

        # TODO: fix "sample.txt"

        # make sure not getting the same word
        if not item == word:
            # make a list and add item, page number, column number to it
            sublist.append(item)
            sublist.append(Navigate.Navigate.get_line(item, the_text))
            sublist.append(Navigate.Navigate.get_specific_column_number(item, the_text))

            # turn the list into tuple
            item_tuple = tuple(sublist)
            if item in body and word not in dict:
                dict[word] = [item_tuple]
            elif word in dict and item in body and item_tuple not in dict[word]:
                dict[word].append(item_tuple)


def word_to_concepts(text, the_text):
    # text_file = open(file_name,"r")
    # text = text_file.read()
    text = text.split()

    for item in text:
        find_word(item, text, the_text)
    return dict


# print(word_to_concepts(text))
