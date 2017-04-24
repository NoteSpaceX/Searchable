import numbers

from EditorUtils import Navigate


#Todo: 'NoneType' object is not iterable

def minimum_edit_distance(s1, s2, the_text):
    # if the words in the text
    if s1 in the_text and s2 in the_text:
        if len(s1) > len(s2):
            s1,s2 = s2,s1
        distances = range(len(s1) + 1)
        for index2,char2 in enumerate(s2):
            new_distances = [index2+1]
            for index1,char1 in enumerate(s1):
                if char1 == char2:
                    new_distances.append(distances[index1])
                else:
                    new_distances.append(1 + min((distances[index1],
                                                 distances[index1+1],
                                                 new_distances[-1])))
            distances = new_distances
        result = distances[-1]
        sublist = [s1, s2, result]
        return sublist

dict = {}


def find_word(word, other_word, body, the_text):
    lev_list = minimum_edit_distance(word, other_word, body)


    # iterate through the list of synonyms
    for item in lev_list:
        sublist = []

        if isinstance(item,numbers.Number):
            continue

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

    return dict

print(minimum_edit_distance("kitten", "sitting", "hey kitten sitting"))
print(find_word("kitten","sitting","hey kitten sitting","hey kitten sitting"))
# print(minimumEditDistance("Sunday", "Saturday"))