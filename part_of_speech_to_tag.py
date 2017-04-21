def part_of_speech_to_tag(part_of_speech):
    tag = {'adjective': 'ADJ', 'adposition': 'ADP', 'adverb': 'ADV', 'conjunction': 'CONJ', 'determiner': 'DET',
           'article': 'DET', 'noun': 'NOUN', 'number': 'NUM', 'particle': 'PRT', 'pronoun': 'PRON', 'verb': 'VERB',
           'punctuation': '.', 'other': 'X'}
    return tag(part_of_speech);