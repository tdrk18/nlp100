# -*- coding: utf-8 -
__author__ = 'todoroki'

import problem30

def extract_verb_base(sentences):
    res = []
    for sentence in sentences:
        for morpheme in sentence:
            if morpheme['pos'] == '動詞':
                res.append(morpheme['base'])
    return res

if __name__ == "__main__":
    inputfile = 'neko.txt.mecab'
    outputfile = 'neko.mecab_verb_base.txt'
    f = open(inputfile, "r")
    g = open(outputfile, "w")
    sentences = problem30.mecab_reader(f)
    verb_bases = extract_verb_base(sentences)
    for verb in verb_bases:
        # print verb
        g.write(verb + '\n')
    f.close()
    g.close()
