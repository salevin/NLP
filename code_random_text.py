# Natural Language Toolkit: code_random_text
import random

import nltk
from nltk.corpus import brown


def generate_model(cfdist, word, num=15, words=5):
    for i in range(num):
        print word,
        lwords = cfdist[word].most_common(words)
        word = random.choice(lwords)[0]


text = brown.words()
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)  # [_bigram-condition]

if __name__ == '__main__':
    generate_model(cfd, "one")
