# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import re

inputfile = 'hightemp.txt'
outputfile = 'hightemp_tab2space.txt'

f = open(inputfile)
lines = f.readlines()
g = open(outputfile, 'w')
for line in lines:
    line = re.sub('\t', ' ', line)
    g.write(line)
    print line
f.close()
g.close()

# cat hightemp.txt | tr "\t" " " > hightemp_tr.txt
