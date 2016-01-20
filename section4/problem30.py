# -*- coding: utf-8 -
__author__ = 'todoroki'

def mecab_reader(mecabfile):
    sentences = []
    sentence = []
    for line in mecabfile:
        if line == "EOS\n":
            if len(sentence) > 0:
                sentences.append(sentence)
            sentence = []
        else:
            surface, features = line.split("\t")
            features = features.split(",")
            dic = {
                'surface': surface,
                'base': features[6],
                'pos': features[0],
                'pos1': features[1]
            }
            sentence.append(dic)
    return sentences

if __name__ == '__main__':
    inputfile = 'neko.txt.mecab'
    outputfile = 'neko.mecab_dic.txt'
    f = open(inputfile, 'r')
    g = open(outputfile, 'w')
    sentences = mecab_reader(f)

    for s in sentences:
        # print str(s).decode("string-escape")
        g.write(str(s).decode("string-escape") + "\n")

    f.close()
    g.close()

# mecab neko.txt -o neko.txt.mecab
