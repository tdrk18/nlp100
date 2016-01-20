# -*- coding: utf-8 -*-
__author__ = 'todoroki'

string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
ans = []

for s in string.split():
    s = s.replace(",", "").replace(".", "")
    ans.append(len(s))
print ans
