# -*- coding: utf-8 -*-
__author__ = 'todoroki'

string1 = u"パトカー"
string2 = u"タクシー"
ans = u""

for a, b in zip(string1, string2):
    ans += a + b
print ans
