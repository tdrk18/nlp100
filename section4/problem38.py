# -*- coding: utf-8 -
__author__ = 'todoroki'

import problem30
import problem36
import pandas as pd

def plot_words_hist(freq, file):
    plot = freq.hist()
    fig = plot.get_figure()
    fig.savefig(file)

if __name__ == '__main__':
    inputfile = 'neko.txt.mecab'
    outputfile = 'neko.mecab_words_hist.png'
    f = open(inputfile, 'r')
    words = []
    counts = []
    sentences = problem30.mecab_reader(f)
    counter = problem36.count_words(sentences)
    freq = pd.Series(list(counter.values()), index=list(counter.keys()))
    plot_words_hist(freq, outputfile)
