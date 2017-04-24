# def part_of_speech_to_tag(part_of_speech):
#     tag = {'adjective': 'ADJ', 'adposition': 'ADP', 'adverb': 'ADV', 'conjunction': 'CONJ', 'determiner': 'DET',
#            'article': 'DET', 'noun': 'NOUN', 'number': 'NUM', 'particle': 'PRT', 'pronoun': 'PRON', 'verb': 'VERB',
#            'punctuation': '.', 'other': 'X'}
#     return tag(part_of_speech);


def part_of_speech_to_tag(part_of_speech):
    tag = {'conjunction': ['CC'], 'number': ['CD'], 'determiner': ['DT'], 'preposition': ['IN'],
           'adjective': ['JJ', 'JJR', 'JJS'], 'noun': ['NN', 'NNS', 'NNP', 'NNPS'], 'pronoun': ['PRP', 'PRP$'],
           'adverb': ['RB', 'RBR', 'RBS'], 'verb': ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']}
    part_of_speech_acr = tag.get(part_of_speech)
    if part_of_speech_acr is not None:
        return part_of_speech_acr

# 4.	EX	Existential there
# 5.	FW	Foreign word
# 10.	LS	List item marker
# 11.	MD	Modal
# 16.	PDT	Predeterminer
# 17.	POS	Possessive ending
#
# 23.	RP	Particle
# 24.	SYM	Symbol
# 25.	TO	to
# 26.	UH	Interjection
#
# 33.	WDT	Wh-determiner
# 34.	WP	Wh-pronoun
# 35.	WP$	Possessive wh-pronoun
# 36.	WRB	Wh-adverb