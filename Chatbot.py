## read data

import numpy as np

from keras.models import Sequential

from keras.layers import Dense, Activation, Dropout

from keras.optimizers import SGD

import random

import nltk

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

import json

import pickle

intents_file = open('/Users/liujiaqi/Downloads/python-project-chatbot-codes/intents.json').read()

intents = json.loads(intents_file)
