# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import problem41

def make_chunk_pair(sentence):
    pairs = []
    for chunk in sentence:
        if chunk.dst != -1:
            pairs.append((chunk, sentence[chunk.dst]))
    return pairs

if __name__ == "__main__":
    f = open("neko.txt.cabocha")
    sentences = problem41.read_chunk(f)
    pair_sentences = []
    for sentence in sentences:
        pair = make_chunk_pair(sentence)
        pair_sentences.append(pair)
    for sentence in pair_sentences:
        for pair in sentence:
            print "\t".join([str(chunk) for chunk in pair])
    f.close()
