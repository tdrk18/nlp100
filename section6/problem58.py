# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import problem56

def extractTuples(sentence):
    dependencies = sentence.find("dependencies[@type='collapsed-dependencies']")
    dep_triple = []
    dep_dic = {}

    for dep in dependencies:
        gov = (dep.find('governor').get('idx'), dep.find('governor').text)
        if dep.get('type') in ['nsubj', 'dobj']:
            dep_dic.setdefault(gov, []).append((dep.get('type'), dep.find('dependent').text))

    verbs = [key for key, value in dep_dic.iteritems() if set([t for (t, d) in value]) == set(['nsubj', 'dobj'])]

    for verb in verbs:
        nsubj = [d for (t, d) in dep_dic[verb] if t == 'nsubj']
        dobj = [d for (t, d) in dep_dic[verb] if t == 'dobj']
        dep_triple += [[verb[1], n, d] for n in nsubj for d in dobj]

    return dep_triple

def main(file):
    doc = problem56.StanfordDocument(file)
    sentences = doc.sentences.findall('sentence')
    dep_triple = []

    for sentence in sentences:
        dep_triple.append(extractTuples(sentence))

    return dep_triple

if __name__ == '__main__':
    dep_triple = main('nlp.txt.xml')
    for dep in dep_triple:
        for dt in dep:
            print "%s\t%s\t%s" % (dt[1], dt[0], dt[2])
