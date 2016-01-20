# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import re
import xml.etree.ElementTree as et
from functools import partial

LRB = re.compile(r"-LRB- ")
RRB = re.compile(r" -RRB-")
NOTATION = re.compile(r" ([,\.:;])")
LDQ = re.compile(r"`` ")
RDQ = re.compile(r" \'\'")
SQ = re.compile(r" \'")
SQS = re.compile(r" \'s")

class StanfordDocument():
    def __init__(self, file):
        self.xmltree = et.parse(file)
        root = self.xmltree.getroot()
        self.sentences = root.find('document/sentences')
        self.coreferences = root.find('document/coreference')

    def getListOfSentences(self):
        sentences = []
        for sentence in self.sentences.findall('sentence'):
            sentences.append([word.text for word in sentence.findall('tokens/token/word')])
        return sentences

def main(file):
    doc = StanfordDocument(file)
    sentences = doc.getListOfSentences()

    for coref in doc.coreferences.findall('coreference'):
        mentions = coref.findall('mention')
        represent = coref.find('mention[@representative="true"]')
        for mention in mentions:
            if mention != represent:
                sentence_i = int(mention.find('sentence').text) - 1
                start_i = int(mention.find('start').text) - 1
                end_i = int(mention.find('end').text) - 2

                target_sentence = sentences[sentence_i]
                target_sentence[start_i] = represent.find('text').text.strip() + ' (' + target_sentence[start_i]
                # print list(represent)
                # target_sentence[start_i] = "[" + str(sentence_i) +","+ str(start_i) +","+ str(end_i) +","+str(sentences[sentence_i][start_i])+ "]" + ' (' + target_sentence[start_i]
                target_sentence[end_i] = target_sentence[end_i] + ')'
    return sentences

def prettifySentence(sentence):
    s = " ".join(sentence)
    partials = map(
        lambda x: partial(x[0], x[1]),
        [
            (LRB.sub, '('),
            (RRB.sub, ')'),
            (LDQ.sub, '\"'),
            (RDQ.sub, '\"'),
            (SQS.sub, "\'s"),
            (SQ.sub, "\'"),
            (NOTATION.sub, r'\1')
        ]
    )
    for part in partials:
        s = part(s)
    return s

if __name__ == "__main__":
    file = "nlp.txt.xml"
    sentences = main(file)
    for sentence in sentences:
        s = prettifySentence(sentence)
        print s
