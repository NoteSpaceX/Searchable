import nltk
from nltk.compat import raw_input

import Navigate


class Categorize:
    # stores each word in a line in a list
    def text_dictionary(self):
        dict = {}
        # sentences = nltk.sent_tokenize(self)
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


def make_dict(word, body, text):
    # take the categorize dictionary
    categorize_dict = Categorize.text_dictionary(text)
    
    # make the new dictionary that we will return
    new_dict = {}
    
    # iterate through the current dictionary
    for key, value in categorize_dict.items():
        
        
        # iterate through the values because the dictionary contains a list of values as value
        for item in value:
            sublist = []
            
            sublist.append(item)
            sublist.append(Navigate.Navigate.get_line(item, text))
            sublist.append(Navigate.Navigate.get_specific_column_number(item, text))
            
            item_tuple = tuple(sublist)
            
            if key not in new_dict and item_tuple[0] in body:
                new_dict[key] = [item_tuple]
            elif key in new_dict and item_tuple not in new_dict[key]:
                new_dict[key].append(item_tuple)

    return new_dict


# def main():
#     # print("Enter a file name: ")
#     # file_name = raw_input()
#     text_file = open("sample.txt", 'r')
#     text = text_file.read()
#
#     dict = Categorize.text_dictionary(text)
#     print(dict)
#
#     new_dict = make_dict("", text)
#     print(new_dict)
#
#
# if __name__ == "__main__":
#     main()
#

