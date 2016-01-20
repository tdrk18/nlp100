# -*- coding: utf-8 -
__author__ = 'todoroki'

import problem30
import problem36
import matplotlib.pyplot as plt


def plot_words_hist_log(counter, file):
    from matplotlib.font_manager import FontProperties
    fp = FontProperties(fname='/usr/local/Cellar/ricty/3.2.4/share/fonts/Ricty-Regular.ttf')
    plt.figure()
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(sorted(list(counter.values()), reverse=True), range(1, len(list(counter))+1))
    plt.savefig(file)


if __name__ == '__main__':
    inputfile = 'neko.txt.mecab'
    outputfile = 'neko.mecab_words_hist_log.png'
    f = open(inputfile, 'r')
    words = []
    counts = []
    sentences = problem30.mecab_reader(f)
    counter = problem36.count_words(sentences)
    plot_words_hist_log(counter, outputfile)
    f.close()
