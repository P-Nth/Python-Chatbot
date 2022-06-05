PYTHON CHATBOT \n
Version 0.0.1 \n

# Chatbot Client with Flask and JavaScript.

This chatbot is deployed within a Flask app with jinja template.
It can be configured so that the frontend is separated with the backend.
This will require you to use cors to enable the Cross Origin Resource Sharing

# Project Setup

This repo contains all the starter files.

No need for a vitual environment.
Go ahead and clone the repo now.

`$ git clone https://github.com/P-Nth/My-Python-Projects.git \n
$ cd "Python Chatbot"`

# Install dependencies

`$ pip install Flask torch torchvision nltk `
`$ pip install flask-cors` #Only necesary if you want to create a separate frontend and communicate with the backend via api.

# Install nltk package
`$ python`

`> > > import nltk`
`> > > nltk.download('punkt')`

Modify dictionary.json with different intents and responses for your Chatbot \n

# Run

Path to use `~/My-Python-Projects/Python Chatbot`

`$ python tlior.py`

This will dump data.pth file. And then run the following command to test it in the console.

# Then Deploy The File Server:

First you need to configure and implement the index.html.
And then configure scripts.js to post user input & fetch response from the backend.

`$ python main.py`

# Credits:

Credits go to NeuralNine for helping out with the training of the neural network.
And more credits got to Python Engeneer for helping out with intergrating the ChatBot with the Frontend.
