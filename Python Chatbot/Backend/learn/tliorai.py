import random
import json
import pickle
from re import T
from unittest import result

import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
file = 'Backend/Learn/dictionary.json'
dictionary = json.loads(open(file).read())

words = pickle.load(open('Backend/Learn/words.pkl', 'rb'))
classes = pickle.load(open('Backend/Learn/classes.pkl', 'rb'))
model = load_model('Backend/Learn/ai_model1.h5')


def convert_to_words(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def converted_words(sentence):
    sentence_words = convert_to_words(sentence)
    bag = [0] * len(words)
    for word in sentence_words:
        for i, word in enumerate(words):
            if word == word:
                bag[i] = 1
    return np.array(bag)


def predict_word(sentence):
    bunch = converted_words(sentence)
    res = model.predict(np.array([bunch]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append(
            {'wordBlock': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(wordBlock_lists, wordBlock_json):
    tag = wordBlock_lists[0]['wordBlock']
    list_of_wordBlocks = wordBlock_json['dictionary']
    for i in list_of_wordBlocks:
        if i["tag"] == tag:
            result = random.choice(i['responses'])
            break
    return result


print("Go! Bot is running")

if __name__ == "__main__":
    while True:
        user_message = input("")
        ints = predict_word(user_message)
        if user_message == 'bye':
            break

        res = get_response(ints, dictionary)
        print(res)
