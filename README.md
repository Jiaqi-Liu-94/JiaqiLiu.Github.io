Tensorflow Chatbot
====================


Overview
--------
This is the full code for how to make a simple chatbot.
In this demo code, I implement Tensorflows Sequence to Sequence model to train a chatbot on the dataset. 
After training, the bot is able to hold a fun conversation.

Dependencies
------------
numpy

scipy

Keras

NLTK

tensorflow (https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html)

Use pip to install any missing dependencies

File 
----
All files can be downloaded from zip folder

**Train_chatbot.py **

- In this file, we will build and train the deep learning model that can classify and identify what the user is asking to the bot.

**Gui_Chatbot.py **

- This file is where we will build a graphical user interface to chat with our trained chatbot.

**Intents.json **

- The intents file has all the data that we will use to train the model. It contains a collection of tags with their corresponding patterns and responses.

**Chatbot_model.h5 **

- This is a hierarchical data format file in which we have stored the weights and the architecture of our trained model.

**Classes.pkl **

- The pickle file can be used to store all the tag names to classify when we are predicting the message.

**Words.pkl **

- The words.pkl pickle file contains all the unique words that are the vocabulary of our model.
