import nltk
from nltk.corpus import treebank
from nltk import pos_tag as tagger
from nltk.chunk import ne_chunk as identifier
test_sentence = """ At eight o'clock on Thursday morning
            Arthur didn't feel very good.
"""

tokens = nltk.word_tokenize(test_sentence)

tagged = tagger(tokens)

entities = identifier(tagged)

