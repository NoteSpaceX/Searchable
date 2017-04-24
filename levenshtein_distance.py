import Navigate
import numbers

#Todo: 'NoneType' object is not iterable

def minimumEditDistance(s1,s2, the_text):
    # if the words in the text
    if s1 in the_text and s2 in the_text:
        if len(s1) > len(s2):
            s1,s2 = s2,s1
        distances = range(len(s1) + 1)
        for index2,char2 in enumerate(s2):
            newDistances = [index2+1]
            for index1,char1 in enumerate(s1):
                if char1 == char2:
                    newDistances.append(distances[index1])
                else:
                    newDistances.append(1 + min((distances[index1],
                                                 distances[index1+1],
                                                 newDistances[-1])))
            distances = newDistances
        result = distances[-1]
        sublist = []
        sublist.append(s1)
        sublist.append(s2)
        sublist.append(result)
        return sublist



dict = {}


def find_word(word, other_word, body, the_text):
    lev_list = minimumEditDistance(word,other_word, body)


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

print(minimumEditDistance("kitten","sitting","hey kitten sitting"))
print(find_word("kitten","sitting","hey kitten sitting","hey kitten sitting"))
# print(minimumEditDistance("Sunday", "Saturday"))