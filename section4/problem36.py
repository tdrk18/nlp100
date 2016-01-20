# -*- coding: utf-8 -
__author__ = 'todoroki'

import problem30
from collections import Counter

def count_words(sentences):
    words = []
    for sentence in sentences:
        for morpheme in sentence:
            words.append(morpheme['surface'])
    return Counter(words)

if __name__ == "__main__":
    inputfile = "neko.txt.mecab"
    outputfile = "neko.mecab_words.txt"
    f = open(inputfile, 'r')
    g = open(outputfile, 'w')
    sentences = problem30.mecab_reader(f)
    counter = count_words(sentences)
    for word, count in counter.most_common():
        # print word, count
        g.write("%s %s\n" % (word, count))
    f.close()
    g.close()
