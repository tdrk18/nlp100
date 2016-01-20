# -*- coding: utf-8 -*-
__author__ = 'todoroki'

string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans = {}
for i, s in enumerate(string.split(), 1):
    if i in index:
        ans[s[0]] = i
    else:
        ans[s[0:2]] = i
print ans
