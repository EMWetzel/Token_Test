#Need to download NLTK (Natural Language Toolkit)

#pip install nltk


import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize

text = "This test is meant to show how large language models break sentences into tokens. This is a fundamental step in understanding natural language text"

words = word_tokenize(text)
print("Word Tokens:", words)

sentences = sent_tokenize(text)
print("Sentence Tokens:", sentences)

