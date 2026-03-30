import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

import spacy
nlp = spacy.load("en_core_web_sm")