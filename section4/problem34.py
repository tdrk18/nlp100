# -*- coding: utf-8 -
__author__ = 'todoroki'

import problem30

def extract_AofB(sentences):
    res = []
    for sentence in sentences:
        for k in xrange(len(sentence)-3):
            triple = sentence[k:k+3]
            b1 = triple[0]['pos'] == '名詞'
            b2 = triple[1]['surface'] == 'の'
            b3 = triple[2]['pos'] == '名詞'
            if b1 and b2 and b3:
                res.append(t['surface'] for t in triple)
    return res

if __name__ == "__main__":
    inputfile = 'neko.txt.mecab'
    outputfile = 'neko.mecab_AofB.txt'
    f = open(inputfile, "r")
    g = open(outputfile, "w")
    sentences = problem30.mecab_reader(f)
    res = extract_AofB(sentences)
    for r in res:
        # print "".join(r)
        g.write("".join(r) + '\n')
    f.close()
    g.close()
