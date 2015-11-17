import CounterWorkaround
import nltk

tags = nltk.corpus.brown.tagged_words()

if __name__ == '__main__':
    occurs = CounterWorkaround.Counter([i[0] for i in tags])
    most_common = occurs.most_common(1)[0][0]
    over_two = list(i for i in occurs if occurs.get(i) >= 2)
    print("The most common word is \"%s\"" % most_common)
    print("There are %s words with over two occurrences" % len(over_two))
