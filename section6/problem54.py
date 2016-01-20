# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import re

WORD = re.compile(r"<word>(\w+)</word>")
LEMMA = re.compile(r"<lemma>(\w+)</lemma>")
POS = re.compile(r"<POS>(\w+)</POS>")

f = open("nlp.txt.xml", "r")
words = []
for line in f:
    if len(words) == 3:
        print "\t".join(words)
        words = []
    else:
        line = line.strip()
        word = WORD.search(line)
        if len(words) == 0 and word:
            words.append(word.group(1))
            continue
        lemma = LEMMA.search(line)
        if len(words) == 1 and lemma:
            words.append(lemma.group(1))
            continue
        pos = POS.search(line)
        if len(words) == 2 and pos:
            words.append(pos.group(1))
f.close()
