# word_validator.py

import nltk

# Download the NLTK English wordlist
nltk.download('words')

def is_valid_word(word):
    # Check if the lowercase version of the input word is in the NLTK wordlist
    return word.lower() in set(nltk.corpus.words.words())
