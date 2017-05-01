import nltk
from nltk import tokenize


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


#print(LDforSentences("i am a cat.", "i am a cat. i am a dog. you are a pig. my name is james.", 3))
