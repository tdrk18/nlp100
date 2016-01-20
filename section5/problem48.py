# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import problem41

def extractPath(chunk, sentence):
    path = [chunk]
    dst = chunk.dst
    while dst != -1:
        path.append(sentence[dst])
        dst = sentence[dst].dst
    return path

if __name__ == "__main__":
    f = open("neko.txt.cabocha", "r")
    sentences = problem41.read_chunk(f)
    f.close()
    paths = []
    for sentence in sentences:
        for chunk in sentence:
            if chunk.include_pos('名詞') and chunk.dst != -1:
                paths.append(extractPath(chunk, sentence))

    for path in paths:
        print " -> ".join([str(chunk) for chunk in path])
