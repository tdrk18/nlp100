# -*- coding: utf-8 -*-
__author__ = 'todoroki'

def ngram(data, n):
    res = []
    for i in xrange(len(data) - 1):
        res.append(data[i:i + n])
    return res

string = 'I am an NLPer'
print u'文字リストのbi-gram:'
print ngram(string.split(), 2)
print u'文字列のbi-gram:'
print ngram(string, 2)