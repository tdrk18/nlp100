# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import problem41
import problem45

def extractSahen(src_chunks):
    for i, src_chunk in enumerate(src_chunks):
        morphs = src_chunk.morphs
        if len(morphs) > 1:
            if morphs[-2].pos1 == "サ変接続" and morphs[-1].pos == "助詞" and morphs[-1].base == "を":
                src_chunks.pop(i)
                return src_chunk, src_chunks
    return None

if __name__ == "__main__":
    f = open("neko.txt.cabocha", "r")
    sentences = problem41.read_chunk(f)
    f.close()
    verbPatterns = []
    for sentence in sentences:
        verbPatterns.append(problem45.extractVerbPatern(sentence))

    for verbPattern in verbPatterns:
        for verb, src_chunks in verbPattern:
            sahen_chunks_set = extractSahen(src_chunks)
            if sahen_chunks_set:
                sahen_chunk, other_chunks = sahen_chunks_set
                col1 = str(sahen_chunk) + verb.morphs_of_pos('動詞')[-1].base
                tmp = [(other_chunk.morphs_of_pos1('格助詞')[-1].base, str(other_chunk)) for other_chunk in other_chunks]
                tmp = sorted(tmp, key=lambda x: x[0])
                col2 = " ".join([col[0] for col in tmp])
                col3 = " ".join([col[1] for col in tmp])
                print "%s\t%s\t%s" % (col1, col2, col3)

# python problem47.py | cut -f 1 | sort | uniq -c | sort -nr
# python problem47.py | cut -f 1,2 | sort | uniq -c | sort -nr
