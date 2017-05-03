import nltk

from EditorUtils import Navigate


class Categorize:
    # stores each word in a line in a list
    def text_dictionary(self):
        dict = {}
        tokens = nltk.word_tokenize(self)
        tagged = nltk.pos_tag(tokens)
        
        for item in tagged:
            key = item[1]
            if key not in dict:
                dict[key] = [item[0]]
            elif item[0] not in dict[key]:
                dict[key].append(item[0])
        return dict
    
    def list_to_string(self):
        result = ""
        for item in self:
            result += item + " "
        return result


def part_of_speech_to_tag(part_of_speech):
    tag = {'conjunction': ['CC'], 'number': ['CD'], 'determiner': ['DT'], 'preposition': ['IN'],
           'adjective': ['JJ', 'JJR', 'JJS'], 'noun': ['NN', 'NNS', 'NNP', 'NNPS'], 'pronoun': ['PRP', 'PRP$'],
           'adverb': ['RB', 'RBR', 'RBS'], 'verb': ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']}
    part_of_speech_acr = tag.get(part_of_speech)
    if part_of_speech_acr is not None:
        return part_of_speech_acr


def make_dict(body, text):
    # take the categorize dictionary
    categorize_dict = Categorize.text_dictionary(text)
    
    # make the new dictionary that we will return
    new_dict = {}
    
    # iterate through the current dictionary
    for key, value in categorize_dict.items():

        # iterate through the values because the dictionary contains a list of values as value
        for item in value:
            sublist = [item, Navigate.Navigate.get_line(item, text),
                       Navigate.Navigate.get_specific_column_number(item, text)]

            item_tuple = tuple(sublist)
            
            if key not in new_dict and item_tuple[0] in body:
                new_dict[key] = [item_tuple]
            elif key in new_dict and item_tuple not in new_dict[key]:
                new_dict[key].append(item_tuple)

    return new_dict
