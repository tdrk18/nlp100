# -*- coding: utf-8 -
__author__ = 'todoroki'

import problem30
import problem36
import matplotlib.pyplot as plt

def plot_words(words, counts, file):
    from matplotlib.font_manager import FontProperties
    fp = FontProperties(fname='/usr/local/Cellar/ricty/3.2.4/share/fonts/Ricty-Regular.ttf')
    plt.bar(range(10), counts, align='center')
    plt.xticks(range(0, 10), words, fontproperties=fp)
    plt.savefig(file)

if __name__ == '__main__':
    inputfile = 'neko.txt.mecab'
    outputfile = 'neko.mecab_words.png'
    f = open(inputfile, 'r')
    words = []
    counts = []
    sentences = problem30.mecab_reader(f)
    counter = problem36.count_words(sentences)
    for word, count in counter.most_common(10):
        # print word, count
        words.append(word.decode('utf8'))
        counts.append(count)
    plot_words(words, counts, outputfile)
    f.close()
