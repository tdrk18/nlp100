# -*- coding: utf-8 -
__author__ = 'todoroki'

import problem30

def extract_sahen(sentences):
    res = []
    for sentence in sentences:
        for morpheme in sentence:
            if morpheme['pos1'] == 'サ変接続':
                res.append(morpheme['surface'])
    return res

if __name__ == "__main__":
    inputfile = 'neko.txt.mecab'
    outputfile = 'neko.mecab_sahen.txt'
    f = open(inputfile, "r")
    g = open(outputfile, "w")
    sentences = problem30.mecab_reader(f)
    sahens = extract_sahen(sentences)
    for sahen in sahens:
        # print sahen
        g.write(sahen + '\n')
    f.close()
    g.close()
