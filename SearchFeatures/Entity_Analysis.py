import urllib

import requests

from EditorUtils import Navigate
from SearchFeatures import Synonym_Search, credentials


class GetData:
    # Not used
    @staticmethod
    def classifier(text_str):
        base_url = 'https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers/10D41B-nlc-1/classify?text='
        end_url = '/10D41B-nlc-1'
        text_to_url = urllib.parse.quote(text_str)
        response = requests.get(base_url + text_to_url + end_url, auth=(credentials.username, credentials.password))
        print(response)

    @staticmethod
    def get_sentiment(text_str):
        base_url = 'https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2017-02-27&text='
        end_url = '.&features=sentiment'
        text_to_url = urllib.parse.quote(text_str)
        response = requests.get(base_url + text_to_url + end_url, auth=(credentials.username, credentials.password))
        result = response.json()
        return 'score:', result['sentiment']['document']['score'], '\nlabel: ', result['sentiment']['document']['label']

    @staticmethod
    def get_emotion(text_str):
        base_url = 'https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2017-02-27&text='
        end_url = '.&features=sentiment,emotion'
        text_to_url = urllib.parse.quote(text_str)
        response = requests.get(base_url + text_to_url + end_url, auth=(credentials.username, credentials.password))
        result = response.json()

        emotions = result['emotion']['document']['emotion']
        return emotions

    @staticmethod
    def find_type(text_str, search_word):
        lower_search_word = str.lower(search_word)
        base_url = 'https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2017-02-27&text='
        end_url = '.&features=sentiment,relations'
        text_to_url = urllib.parse.quote(text_str)
        response = requests.get(base_url + text_to_url + end_url, auth=(credentials.username, credentials.password))
        result = response.json()
        relations = result['relations']
        word_types = [search_word]
        for relation in relations:
            arguments = relation['arguments']
            for argument in arguments:
                entities = argument['entities']
                for entity in entities:
                    print('entity', entity)
                    entity_type = str.lower(entity['type'])
                    if entity_type == lower_search_word and entity['text'] not in word_types:
                        word_types.append(entity['text'])
                        synonyms_text = Synonym_Search.synonyms(entity['text'])
                        synonyms = Synonym_Search.synonyms(entity['type'])
                        # Using synonyms of words in text
                        for synonym in synonyms_text:
                            lower_synonym = str.lower(synonym)
                            lower_text_str = str.lower(text_str)
                            if lower_synonym in lower_text_str and lower_synonym not in word_types:
                                word_types.append(synonym)
                        # Using synonyms of results
                        for synonym in synonyms:
                            lower_synonym = str.lower(synonym)
                            lower_text_str = str.lower(text_str)
                            if lower_synonym in lower_text_str and lower_synonym not in word_types:
                                word_types.append(synonym)
        print('word types:', word_types)
        return word_types


def create_dict(word, text):
    print("text: ", text)
    text_words = text.split(" ")

    dict = {}
    print(word)
    word_list = GetData.find_type(text, word)
    print("word_list: ", word_list)

    # iterate through the list of synonyms
    sublist = []
    for word_from_list in word_list:
        for each_word in text_words:
            if word_from_list == each_word:

                # make a list and add word, page number, column number to it
                if word_from_list not in sublist:
                    sublist.append(word_from_list)
                    print('column#', Navigate.Navigate.get_tuple(word_from_list, text))
                    sublist.append(Navigate.Navigate.get_tuple(word_from_list, text))

                if word_from_list in text and word_from_list not in dict:
                    dict[word] = sublist
                elif word_from_list in dict and sublist not in dict[word_from_list]:
                    dict[word_from_list].append(sublist)

    return dict
