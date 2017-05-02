import nltk
from nltk import tokenize, re

# from EditorUtils.Navigate import Navigate, get_sentence
from EditorUtils.Navigate import Navigate


def LDforSentences(s1, the_text, max_distance):
    # store each word in an array
    str1 = s1.split()
    tags1 = nltk.pos_tag(str1)
    l1 = len(str1)
    ps1 = []
    ps2 = []
    result = []
    dict = {"DT": 0, "PDT": 0, "CD": 1, "NN": 1, "NNS": 1, "NNP": 1, "NNPS": 1, "POS": 1, "PRP": 2, "PRP$": 2, "JJ": 3,
            "JJR": 3, "JJS": 3, "VB": 4, "VBD": 4, "VBG": 4, "VBN": 4, "VBP": 4, "VBZ": 4, "RB": 5, "RBR": 5, "RBS": 5,
            "CC": 6, "IN": 6, "EX": 7, "WDT": 8, "WP": 8, "WP$": 8, "WRB": 8, "FW": 9, "SYM": 9}

    for i in tags1:
        # store the parts of speech at each word position for l1 in a list
        # list ps1
        ps1.append(i[1])
        # print(ps1)

    sentence_array = tokenize.sent_tokenize(the_text)

    for sentence in sentence_array:
        ps2 = []
        str2 = sentence.split()
        tags2 = nltk.pos_tag(str2)

        # find the number of words

        l2 = len(str2)
        for i in tags2:
            # store the parts of speech at each word position for l2 in a list
            # list ps2
            ps2.append(i[1])
        #print(ps2)

        ld = 0

        if l1 > l2:
            for i in range(0, l2):
                ld = abs(dict[ps1[i]] - dict[ps2[i]]) + ld
            for i in range(l2, l1):
                ld = ld + dict [ps1[i]]
        elif l2 > l1:
            for i in range(0, l1):
                ld = abs(dict[ps1[i]] - dict[ps2[i]]) + ld
            for i in range(l1, l2):
                ld = ld + dict[ps2[i]]
        else:
            for i in range(0, l1):
                ld = abs(dict[ps1[i]] - dict[ps2[i]]) + ld
        if ld <= max_distance:
            result.append(sentence)

    return result

def create_list(search_sentence, the_text, max_distance):
    the_list = []

    sentence_list = LDforSentences(search_sentence, the_text, max_distance)
    text_list = the_text.split("\n")
    # line_num = 1
    # start_list = []
    # end_list = []
    # index = 0

    for sentence in sentence_list:
        line_num = 1
        # print("sentence ", sentence)
        print('text list', text_list)
        for text_sentence in text_list:
            # print("text sentence ", text_sentence)
            # we have the very first number for each of the tuples
            start_list = [m.start() for m in re.finditer(sentence, text_sentence)]
            end_list = [m.end() for m in re.finditer(sentence, text_sentence)]
            # print('start_list: ', start_list)
            # print('end_list: ', end_list)

            if len(start_list) is not 0:
                the_list.append( (str(line_num) + "." + str(start_list[0]), (str(line_num)) + "." + str(end_list[0])) )

            # the_list.append((line_num,start_list[index],end_list[index]))
            print(line_num)
            line_num += 1




    return the_list

# print("ld for sentences: ", LDforSentences("i am a cat.", "i am a cat. i am a dog. you are a pig. my name is james.", 0))
print(create_list("i am a cat.", "i am a cat.\n i am a dog. you are a pig. \n my name is james. i am a ham." , 10))











# print("SENTENCE LIST", sentence_list)
#
# for sentence in sentence_list:
#     print('sentence: ', sentence)
#     # sentence = str(sentence_list)
#     sentence_length = len(sentence)
#     sentence_word = sentence.split(" ")
#
#     line = Navigate.get_line(sentence_word[0],the_text)
#     column = Navigate.get_specific_column_number(sentence_word[0], the_text)
#
#     start_end_tuple = ((str(line)+ "."+str(column)), (str(line)+"." +str(column + sentence_length)) )
#     the_list.append(start_end_tuple)

# the_list.append((str(line)+ "."+str(column)))
# the_list.append((str(line)+"." +str(column + sentence_length)))



# for word in sentence_word:
#
#     sublist = []
#
#     # make a list and add item, page number, column number to it
#     sublist.append(word)
#     sublist.append(get_sentence(word, the_text))
#     # sublist.append(Navigate.get_specific_column_number(word, the_text))
#
#     # turn the list into tuple
#     # item_tuple = tuple(sublist)
#     the_list.append(sublist)
#     # if word in the_text and word not in the_list:
#     #     the_list[word] = [item_tuple]
#     # elif word in the_list and word in the_text and item_tuple not in the_list[word]:
#     #     the_list[word].append(item_tuple)

# print("The list", the_list)