# -*- coding: utf-8 -
__author__ = 'todoroki'

import problem30

def extract_seqs(sentences):
    seqs = []
    seq = []
    for sentence in sentences:
        for morpheme in sentence:
            if morpheme['pos'] == "名詞":
                seq.append(morpheme['surface'])
            else:
                if len(seq) > 1:
                    seqs.append(seq)
                seq = []
    return seqs

if __name__ == "__main__":
    inputfile = 'neko.txt.mecab'
    outputfile = 'neko.mecab_sequences.txt'
    f = open(inputfile, "r")
    g = open(outputfile, "w")
    sentences = problem30.mecab_reader(f)
    sequences = extract_seqs(sentences)
    for sequence in sequences:
        # print "".join(sequence)
        g.write("".join(sequence) + '\n')
    f.close()
    g.close()
