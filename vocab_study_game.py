import sys
from random import randint

words = [ {"capital":"the most important city or town of a country or region, usually its seat of government and administrative center."},
         {"abjure":"solemnly renounce to something"},
         {"nonplussed":"surprised and confused so much that they are unsure how to react."},
         {"genuine":"truly what something is said to be; authentic."}]
def generate_word(word):

    random_key = key,word[randint(0,len(word)-1)]
    return random_word

def print_def(word,key):
    print(word[key])
