# -*- coding: utf-8 -*-
__author__ = 'todoroki'

inputfile1 = 'col1.txt'
inputfile2 = 'col2.txt'
outputfile = 'col_merge.txt'

f = open(inputfile1)
g = open(inputfile2)
h = open(outputfile, "w")

lines1 = f.readlines()
lines2 = g.readlines()
for a, b in zip(lines1, lines2):
    h.write(a.strip() + '\t' + b.strip() + '\n')
f.close()
g.close()
h.close()

# paste col1.txt col2.txt > hightemp_paste.txt
