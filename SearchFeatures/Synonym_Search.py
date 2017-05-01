from nltk.corpus import wordnet as wn

from EditorUtils import Navigate


def synonyms(word):
    word_list = []
    for i, j in enumerate(wn.synsets(word)):
        words = j.lemma_names()
        for item in words:
            if item not in word_list:
                word_list.append(item)
    return word_list


# dict = {}


# def find_word(word, the_text):
#     word_list = synonyms(word)
#
#     # iterate through the list of synonyms
#     for item in word_list:
#         sublist = []
#
#         # make sure not getting the same word
#         if not item == word:
#             # make a list and add item, page number, column number to it
#             sublist.append(item)
#             sublist.append(Navigate.Navigate.get_line(item, the_text))
#             sublist.append(Navigate.Navigate.get_specific_column_number(item, the_text))
#
#             # turn the list into tuple
#             item_tuple = tuple(sublist)
#             # if item in body and word not in dict:
#             if item in the_text and word not in dict:
#                 dict[word] = [item_tuple]
#             elif word in dict and item in the_text and item_tuple not in dict[word]:
#                 dict[word].append(item_tuple)


# def word_to_concepts(text):
#     words = text.split()
#     for word in words:
#         find_word(word, text)
#     return dict

def word_to_concepts(text):
    dict = {}
    words = text.split()
    for word in words:
        word_synonym_list = synonyms(word)
        # iterate through the list of synonyms
        for synonym in word_synonym_list:
            sublist = []
            # make sure not getting the same word
            if not synonym == word:
                # make a list and add item, page number, column number to it
                sublist.append(synonym)
                sublist.append(Navigate.Navigate.get_line(synonym, text))
                sublist.append(Navigate.Navigate.get_specific_column_number(synonym, text))

                # turn the list into tuple
                item_tuple = tuple(sublist)
                # if item in body and word not in dict:
                if synonym in text and word not in dict:
                    dict[word] = [item_tuple]
                elif word in dict and synonym in text and item_tuple not in dict[word]:
                    dict[word].append(item_tuple)
    return dict

