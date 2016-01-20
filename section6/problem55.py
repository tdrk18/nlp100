# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import re

WORD = re.compile(r"<word>(\w+)</word>")
NER = re.compile(r"<NER>(\w+)</NER>")

token = ""
person = ""
f = open('nlp.txt.xml', 'r')
for line in f:
    line = line.strip()
    word = WORD.search(line)
    if word:
        token = word.group(1)
        continue
    ner = NER.search(line)
    if ner:
        if ner.group(1) == "PERSON":
            person = token
            print person
f.close()
