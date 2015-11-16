import nltk
from collections import Counter

if __name__ == '__main__':
    tags = nltk.corpus.brown.tagged_words()
    keys = [i[0] for i in tags]
    occurs = Counter(keys)
    most_common = occurs.most_common(1)[0][0]
    print("The most common word is \"%s\"" % most_common)

    over_two = list(i for i in occurs if occurs.get(i) >= 2)
    print(over_two)
