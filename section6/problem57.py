# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import sys
import problem56

def dependToDot(i, dependency):
    header = "digraph sentence{0} ".format(i)
    body_head = "{ graph [rankdir = LR]; "
    body = ""
    for dep in dependency:
        governor, dependent, label = dep.find('governor').text, dep.find('dependent').text, dep.get('type')
        body += '"{gov}"->"{dep}" [label = "{label}"]; '.format(gov=governor, dep=dependent, label=label)

    dotString = header + body_head + body + "}"
    return dotString

def main(file):
    doc = problem56.StanfordDocument(file)
    sentences = doc.sentences.findall('sentence')
    dotSentences = []
    for i, sentence in enumerate(sentences):
        dependency = sentence.find("dependencies[@type='collapsed-dependencies']")
        dotSentences.append(dependToDot(i+1, dependency))
    return dotSentences

if __name__ == '__main__':
    dotSentences = main('nlp.txt.xml')
    if len(sys.argv) > 1:
        target = int(sys.argv[1]) - 1
        print dotSentences[target]
    else:
        for dotSentence in dotSentences:
            print dotSentence
