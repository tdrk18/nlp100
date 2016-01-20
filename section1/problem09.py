# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import random

def typoglycemia(data):
    res = []
    for d in data.split():
        if len(d) > 4:
            pre = d[0]
            suf = d[-1]
            word = list(d[1:-1])
            random.shuffle(word)
            res.append(pre + "".join(word) + suf)
        else:
            res.append(d)
    return " ".join(res)

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print typoglycemia(sentence)
