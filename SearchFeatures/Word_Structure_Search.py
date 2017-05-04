from __future__ import print_function
from __future__ import division

import numbers

from EditorUtils import Navigate


def _edit_dist_init(len1, len2):
    lev = []
    # initialize 2D array to zero
    for i in range(len1):
        lev.append([0] * len2)

    # column 0: 0,1,2,3,4,...
    for i in range(len1):
        lev[i][0] = i
    # row 0: 0,1,2,3,4,...
    for j in range(len2):
        lev[0][j] = j
    return lev


def _edit_dist_step(lev, i, j, s1, s2):
    c1 = s1[i - 1]
    c2 = s2[j - 1]

    # skipping a character in s1
    a = lev[i - 1][j] + 1
    # skipping a character in s2
    b = lev[i][j - 1] + 1
    # substitution
    c = lev[i - 1][j - 1] + (1 if c1 != c2 else 0)

    # transposition
    d = c + 1  # never picked by default
    if False and i > 1 and j > 1:
        if s1[i - 2] == c2 and s2[j - 2] == c1:
            d = lev[i - 2][j - 2] + 1

    # pick the cheapest
    lev[i][j] = min(a, b, c, d)


def edit_distance(s1, the_text, max_distance):

    len1 = len(s1)

    words = the_text.split()
    leven_distances = []
    if s1 in the_text and max_distance >= 0:
        for word in words:
            len2 = len(word)
            lev = _edit_dist_init(len1 + 1, len2 + 1)

            # iterate over the array
            for i in range(len1):
                for j in range(len2):
                    _edit_dist_step(lev, i + 1, j + 1, s1, word)
            result = lev[len1][len2]
            if result <= max_distance:
                leven_distances.append(word)
                # print(leven_distances)
        return leven_distances


def find_word(word,max_distance,  the_text):
    dict = {}
    lev_list = edit_distance(word, the_text, max_distance)

    # iterate through the list of synonyms
    for item in lev_list:
        sublist = []

        if isinstance(item, numbers.Number):
            continue

        # make a list and add item, page number, column number to it
        sublist.append(item)
        sublist.append(Navigate.Navigate.get_line(item, the_text))
        sublist.append(Navigate.Navigate.get_specific_column_number(item, the_text))

        # turn the list into tuple
        item_tuple = tuple(sublist)
        if item in the_text and word not in dict:
            dict[word] = [item_tuple]
        elif word in dict and item in the_text and item_tuple not in dict[word]:
            dict[word].append(item_tuple)

    return dict
