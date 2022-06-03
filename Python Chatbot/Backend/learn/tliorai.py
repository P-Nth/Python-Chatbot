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
dictionary = json.loads(open('dictionary.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('ai_model1.h5')


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
    for r in result:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(wordBlock_lists):
    tag = wordBlock_lists[0]['wordBlock']
    list_of_wordBlocks = wordBlock_json['wordBlocks']
    for i in list_of_wordBlocks:
        if i["tag"] == tag:
            result = random.choice(i['responses'])
            break
    return result


print("Go! Bot is running")

while True:
    message = input("")
    wblks = predict_word(message)
    res = get_response(wblks)
    print(res)
