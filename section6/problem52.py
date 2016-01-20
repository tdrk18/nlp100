# -*- coding: utf-8 -*-
__author__ = 'todoroki'

from nltk.stem.porter import PorterStemmer

if __name__ == "__main__":
    f = open('nlp_word.txt')
    for line in f:
        stemmer = PorterStemmer()
        l = line.strip()
        if len(l) > 0:
            print "%s\t%s" % (l, stemmer.stem(l))
        else:
            print ""
    f.close()
