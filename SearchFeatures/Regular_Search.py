from EditorUtils import Navigate


def word_search(search_word, text):
    dict = {}
    words = text.split()
    word_list = []
    for word in words:
        if search_word in word:
            word_list.append(word)
    print(word_list)
    for w in word_list:
        sublist = []
        # make a list and add item, page number, column number to it
        sublist.append(w)
        sublist.append(Navigate.Navigate.get_line(w, text))
        sublist.append(Navigate.Navigate.get_specific_column_number(w, text))

        # turn the list into tuple
        item_tuple = tuple(sublist)
        # if item in body and word not in dict:
        if w in text and word not in dict:
            dict[word] = [item_tuple]
        elif word in dict and w in text and item_tuple not in dict[word]:
            dict[word].append(item_tuple)
    return dict

#print(word_search("view","hello i viewed your views with a great view"))