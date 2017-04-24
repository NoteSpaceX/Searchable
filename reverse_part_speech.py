import nltk

def text_dictionary(text):

    # sentences = nltk.sent_tokenize(self)
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)

    for item in tagged:
        key = item[0]
        if key not in dict:
            dict[key] = [item[1]]
        elif item[1] not in dict[key]:
            dict[key].append(item[1])
    return dict

dict = {}

print(text_dictionary("Hi I am a cat."))