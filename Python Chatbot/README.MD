PYTHON CHATBOT \n
Version 0.0.1 \n

# Chatbot Client with Flask and JavaScript.

This chatbot is deployed within a Flask app with jinja template. \n
It can be configured so that the frontend is separated with the backend. \n
This will require you to use cors to enable the Cross Origin Resource Sharing \n

# Project Setup

This repo contains all the starter files. \n
\n
No need for a vitual environment.\n
Go ahead and clone the repo now. \n

$ git clone https://github.com/P-Nth/My-Python-Projects.git \n
$ cd "Python Chatbot" \n

# Install dependencies

$ pip install Flask torch torchvision nltk \n
$ pip install flask-cors #Only necesary if you want to create a separate frontend and communicate with the backend via api. \n

# Install nltk package
$ python \n

`> > >` import nltk \n
`> > >` nltk.download('punkt') \n

Modify dictionary.json with different intents and responses for your Chatbot \n

# Run

Path to use ~/My-Python-Projects/Python Chatbot \n

$ python tlior.py \n

This will dump data.pth file. And then run the following command to test it in the console. \n

# Then Deploy The File Server:

First you need to configure and implement the index.html. \n
And then configure scripts.js to post user input & fetch response from the backend. \n

$ python main.py \n

# Credits:

Credits go to NeuralNine for helping out with the training of the neural network. \n
And more credits got to Python Engeneer for helping out with intergrating the ChatBot with the Frontend. \n
