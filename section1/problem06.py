# -*- coding: utf-8 -*-
__author__ = 'todoroki'

def ngram(data, n):
    res = []
    for i in xrange(len(data) - 1):
        res.append(data[i:i + n])
    return res

string1 = 'paraparaparadise'
string2 = 'paragraph'

X = ngram(string1, 2)
Y = ngram(string2, 2)

print u"和集合:"
print list(set(X).union(set(Y)))
print u"積集合:"
print list(set(X).intersection(set(Y)))
print u"差集合:"
print list(set(X).difference(set(Y)))

print u'\'se\'がXに含まれているか?'
print "se" in X
print u'\'se\'がYに含まれているか?'
print "se" in Y
