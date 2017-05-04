import nltk
from nltk import tokenize, re


def ld_for_sentences(sentence, the_text, max_distance):
    # store each word in an array
    sentence_word = sentence.split()
    tags1 = nltk.pos_tag(sentence_word)
    word_length = len(sentence_word)
    list_one = []
    result = []
    dict = {"DT": 0, "PDT": 0, "CD": 1, "NN": 1, "NNS": 1, "NNP": 1, "NNPS": 1, "POS": 1, "PRP": 2, "PRP$": 2, "JJ": 3,
            "JJR": 3, "JJS": 3, "VB": 4, "VBD": 4, "VBG": 4, "VBN": 4, "VBP": 4, "VBZ": 4, "RB": 5, "RBR": 5, "RBS": 5,
            "CC": 6, "IN": 6, "EX": 7, "WDT": 8, "WP": 8, "WP$": 8, "WRB": 8, "FW": 9, "SYM": 9, "TO":0, "RP":0, "MD": 0}

    for item in tags1:
        # store the parts of speech at each word position for word_length in a list
        list_one.append(item[1])

    sentence_array = tokenize.sent_tokenize(the_text)

    for sentence in sentence_array:
        list_two = []
        other_sentence_word = sentence.split()
        tags2 = nltk.pos_tag(other_sentence_word)

        # find the number of words
        other_word_length = len(other_sentence_word)
        for item in tags2:
            # store the parts of speech at each word position for other_word_length in a list
            list_two.append(item[1])

        distance = 0

        if word_length > other_word_length:
            for item in range(0, other_word_length):
                distance = abs(dict[list_one[item]] - dict[list_two[item]]) + distance
            for item in range(other_word_length, word_length):
                distance = distance + dict[list_one[item]]
        elif other_word_length > word_length:
            for item in range(0, word_length):
                distance = abs(dict[list_one[item]] - dict[list_two[item]]) + distance
            for item in range(word_length, other_word_length):
                distance = distance + dict[list_two[item]]
        else:
            for item in range(0, word_length):
                distance = abs(dict[list_one[item]] - dict[list_two[item]]) + distance
        if distance <= max_distance:
            result.append(sentence)

    return result


def create_list(search_sentence, the_text, max_distance):
    the_list = []

    sentence_list = ld_for_sentences(search_sentence, the_text, max_distance)
    text_list = the_text.split("\n")

    for sentence in sentence_list:
        line_num = 1
        for text_sentence in text_list:

            # the very first number for each of the tuples
            start_list = [m.start() for m in re.finditer(sentence, text_sentence)]
            end_list = [m.end() for m in re.finditer(sentence, text_sentence)]

            if len(start_list) is not 0:
                the_list.append((str(line_num) + "." + str(start_list[0]), (str(line_num)) + "." + str(end_list[0])))

            line_num += 1
    return the_list

