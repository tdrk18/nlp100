# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import problem41
import problem45

if __name__ == "__main__":
    f = open("neko.txt.cabocha", "r")
    sentences = problem41.read_chunk(f)
    f.close()
    verbPatterns = []
    for sentence in sentences:
        verbPatterns.append(problem45.extractVerbPatern(sentence))

    for verbPattern in verbPatterns:
        for verb, src_chunks in verbPattern:
            col1 = verb.morphs_of_pos('動詞')[-1].base
            tmp = [(src_chunk.morphs_of_pos1('格助詞')[-1].base, str(src_chunk)) for src_chunk in src_chunks]
            tmp = sorted(tmp, key=lambda x:x[0])
            col2 = " ".join([col[0] for col in tmp])
            col3 = " ".join([col[1] for col in tmp])
            print "%s\t%s\t%s" % (col1, col2, col3)
