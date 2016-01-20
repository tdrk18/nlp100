# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import re

WORD = re.compile(r"<word>(\w+)</word>")

f = open('nlp.txt.xml', 'r')
for line in f:
    word = WORD.search(line.strip())
    if word:
        print word.group(1)
f.close()

# java -Xmx5g -cp stanford-corenlp-3.6.0.jar:stanford-corenlp-models-3.6.0.jar:* edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,mention,coref -file nlp_line.txt -outputFormat xml
