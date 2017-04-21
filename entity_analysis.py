import Navigate
import credentials
import requests
import urllib
from watson_developer_cloud import NaturalLanguageClassifierV1

# TODO: if word is not in the text
# TODO: if word is two words
class GetData:
    @staticmethod
    def classifier(text_str):
        base_url = 'https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers/10D41B-nlc-1/classify?text='
        end_url = '/10D41B-nlc-1'
        text_to_url = urllib.parse.quote(text_str)
        response = requests.get(base_url + text_to_url + end_url, auth=(credentials.username, credentials.password))
        print(response)
        # natural_language_classifier = NaturalLanguageClassifierV1(
        #     username=credentials.username,
        #     password=credentials.password)
        #
        # classes = natural_language_classifier.classify('10D41B-nlc-1', 'How hot will it be today?')
        # print(json.dumps(classes, indent=2))

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
        # print(result)
        # print(result['emotion']['document']['emotion'])
        emotions = result['emotion']['document']['emotion']
        print(emotions)
        emotion_result = []
        for emotion in emotions:
            if emotions[emotion] > 0.2:
                emotion_result.append(emotion)
        return emotion_result

    @staticmethod
    def find_type(text_str, search_word):
        #search_word = 'Person'
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
                    entity_type = str.lower(entity['type'])
                    # entity_text = str.lower(entity['text'])
                    if entity_type == lower_search_word and entity['text'] not in word_types:
                        word_types.append(entity['text'])
                        #TODO: NLTK CODE - TO GET SYNONYMS
                        # synonyms = searchable.concept_search.synonyms(entity_text)
                        #TODO: Remove below temp code
                        synonyms = ['customer', 'body', 'character', 'guy', 'human', 'man', 'woman', 'being', 'somebody', 'individual']
                        for synonym in synonyms:
                            lower_synonym = str.lower(synonym)
                            lower_text_str = str.lower(text_str)
                            if lower_synonym in lower_text_str and lower_synonym not in word_types:
                                word_types.append(synonym)
                    # if entity_text == lower_search_word and entity_type not in word_types:
                    #     print('hello')
                    #     word_types.append(entity_type)
        return word_types

text_str = 'videos of a United Airlines passenger being forcibly dragged from his seat on a Sunday overbooked flight at O\'Hare International Airport have been viewed more than 1 million times, and the airline\'s CEO on Monday called the incident \"an upsetting event to all of us here at United. I apologize for having to re-accommodate these customers. Our team is moving with a sense of urgency to work with the authorities and conduct our own detailed review of what happened,\" United CEO Oscar Munoz said in a statement Monday. Munoz said the airline is trying to reach the passenger to further address and resolve this situation.In videos of the incident aboard a flight bound for Louisville, Ky., a man screams as security officers pull him from his seat. He then falls silent as they drag him by the hands, with his glasses askew and his shirt pulled up over his abdomen, down the aisle. Several passengers yell at the officers. \"Oh my God, look at what you did to him,\" one woman yells'

GetData.classifier(text_str)

types = GetData.find_type(text_str, 'Person')
print('types:', types)

emotion = GetData.get_emotion(text_str)
print('emotion(s):', emotion)

sentiment = GetData.get_sentiment(text_str)
print(sentiment)



dict = {}

def create_dict(word,body, text):
    word_list = GetData.find_type(body, word)

    # iterate through the list of synonyms
    for item in word_list:
        sublist = []

        # TODO: fix "sample.txt"

        # make sure not getting the same word
        if not item == word:
            # make a list and add item, page number, column number to it
            sublist.append(item)
            sublist.append(Navigate.Navigate.get_line(item, text))
            sublist.append(Navigate.Navigate.get_specific_column_number(item, text))

            # turn the list into tuple
            item_tuple = tuple(sublist)
            if item in body and word not in dict:
                dict[word] = [item_tuple]
            elif word in dict and item in body and item_tuple not in dict[word]:
                dict[word].append(item_tuple)
    return dict

#
# def word_to_concepts(text, the_text):
#     # text_file = open(file_name,"r")
#     # text = text_file.read()
#     text = text.split()
#
#     for item in text:
#         create_dict(item, text, the_text)
#     return dict

            # text_str = 'New York will be the only state in the country to offer universal public college tuition coverage for working- and middle-class residents after the program was included in the budget package approved Sunday night. The state\'s Excelsior Scholarship program will be rolled out in tiers over the next three years, starting with full coverage of four-year college tuition this fall for students whose families make less than $100,000. The income cap will increase to $110,000 in 2018 and $125,000 in 2019. While states like California and Georgia have comprehensive grant and scholarship programs for four-year college as well, New York\'s is the nation\'s only truly universal program — with no requirements other than residency and income, and no caps on the amount of residents who can receive full tuition."With this budget, New York has the nation\'s first accessible college program. It\'s a different model," said Governor Andrew Cuomo Saturday in a statement. "Today, college is what high school was—it should always be an option even if you can\'t afford it.'
#
# types = GetData.find_type(text_str)
# print('types:', types)
#
# emotion = GetData.get_emotion(text_str)
# print('emotion(s):', emotion)
#
# sentiment = GetData.get_sentiment(text_str)
# print(sentiment)
#
# text_str = 'Two years ago, Eugene Yoon made the \"craziest decision of his life.\"\"I remember kind of just like looking up at the sky and being like, \'God, are you sure about this? \'Cause I\'m pretty happy right now,\'\" Eugene said. \"It felt like a calling.\"What Eugene felt called to do was one really big random act of kindness. He didn\'t know who he was supposed to help or how, all he knew was that he had to help someone and it had to be life-altering.\r\nAnd that\'s when a video came across his Facebook page.\r\n\r\nA guy he never met named Arthur Renowitzky had been mugged, shot and paralyzed 10 years ago. Arthur vowed that he would walk again someday. And when Eugene heard about that, he called Arthur immediately.\r\n\r\n\"He wasn\'t going to give up until I was walking again,\" Arthur said.\r\n\r\nEugene did not have a medical degree. \"I have a film degree,\" he said.\r\n\r\nWhich makes you wonder then, how was Eugene going to make him walk again? \"This is the part... I had no idea,\" he said.\r\n'
#
# types = GetData.find_type(text_str)
# print('types:', types)
#
# emotion = GetData.get_emotion(text_str)
# print('emotion(s):', emotion)
#
# sentiment = GetData.get_sentiment(text_str)
# print(sentiment)

# response = requests.get("https://wikisynonyms.p.mashape.com/person", headers={"X-Mashape-Key": "8o7M3xeO6FmshznigNYYHfrfIOLZp1xOGE8jsnAY1spG2JnZwz", "Accept": "application/json"})
# print(response.json())

        # @staticmethod
        # def get_emotion_url(url):
        #     response = requests.get(url, auth=(credentials.username, credentials.password))
        #     result = response.json()
        #     print(result['emotion']['document']['emotion'])
        #     emotions = result['emotion']['document']['emotion']
        #     emotion_result = []
        #     for emotion in emotions:
        #         if emotions[emotion] > 0.5:
        #             emotion_result.append(emotion)
        #     return emotion_result


        # print(result['emotion']['document']['emotion'])
        # emotions = result['emotion']['document']['emotion']
        # emotion_result = []
        # for emotion in emotions:
        #     if emotions[emotion] > 0.2:
        #         emotion_result.append(emotion)
        # return emotion_result

    # @staticmethod
    # def get_emotion(file):
    #     with open(file) as myfile:
    #         text_str = myfile.read()
    #         print(text_str)
    #     url = urllib.parse.quote(text_str)
    #     print(url)
    #     base_url = 'https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2017-02-27&text='
    #     end_url = '.&features=sentiment,keywords'
    #     response = requests.get(base_url + url + end_url, auth=(credentials.username, credentials.password))
    #     result = response.json()
    #     print(type(result))
    #     return result


# url = 'https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2017-02-27&text=I' \
#           '%20still%20have%20a%20dream%2C%20a%20dream%20deeply%20rooted%20in%20the%20American%20dream%20%E2%80%93' \
#           '%20one%20day%20this%20nation%20will%20rise%20up%20and%20live%20up%20to%20its%20creed%2C%20%22We%20hold' \
#           '%20these%20truths%20to%20be%20self%20evident%3A%20that%20all%20men%20are%20created%20equal.&features' \
#           '=sentiment,emotion'

# data = GetData.get_data_url(url)
# print(data)
# print(data['sentiment']['document']['score'])
# print(data['keywords'])
# print(data['keywords'][0]['text'])

# data = GetData.get_data('Building mr concerns servants in he outlived am breeding. He so lain good miss when sell some at if. Told hand so an rich gave next. How doubt yet again see son smart. While mirth large of on front. Ye he greater related adapted proceed entered an. Through it examine express promise no. Past add size game cold girl off how old. To sorry world an at do spoil along. Incommode he depending do frankness remainder to. Edward day almost active him friend thirty piqued. People as period twenty my extent as. Set was better abroad ham plenty secure had horses. Admiration has sir decisively excellence say everything inhabiting acceptance. Sooner settle add put you sudden him. Delightful remarkably mr on announcing themselves entreaties favourable. About to in so terms voice at. Equal an would is found seems of. The particular friendship one sufficient terminated frequently themselves. It more shed went up is roof if loud case. Delay music in lived noise an. Beyond genius really enough passed is up. ')

# emotions = GetData.get_emotion(text)
# types = GetData.find_type(text)
# print(emotions)
# print(types)
