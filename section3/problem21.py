# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import re

inputfile = 'jawiki-england.txt'
outputfile = 'jawiki-england_category.txt'

f = open(inputfile)
g = open(outputfile, "w")

category = re.compile('\[\[Category:.+\]\]')

for line in f:
    if category.match(line):
        g.write(line.strip() + "\n")

f.close()
g.close()
