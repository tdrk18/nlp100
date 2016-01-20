# -*- coding: utf-8 -*-
__author__ = 'todoroki'

def cipher(data):
    res = ""
    for s in data:
        if s.islower():
            res += chr(219-ord(s))
        else:
            res += s
    return res

string = "re1"
print u'暗号化:'
print cipher(string)
print u'復号化:'
print cipher(cipher(string))
