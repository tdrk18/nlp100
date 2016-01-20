# -*- coding: utf-8 -*-
__author__ = 'todoroki'

inputfile = 'hightemp.txt'
outputfile1 = 'col1.txt'
outputfile2 = 'col2.txt'
f = open(inputfile)
lines = f.readlines()
g = open(outputfile1, "w")
h = open(outputfile2, "w")
for line in lines:
    line = line.split('\t')
    g.write(line[0].strip('\n') + '\n')
    h.write(line[1].strip('\n') + '\n')
f.close()
g.close()
h.close()

# cut -f 1 hightemp.txt > hightemp_cut1.txt
# cut -f 2 hightemp.txt > hightemp_cut2.txt
