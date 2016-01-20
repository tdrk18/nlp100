# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import re

inputfile = 'jawiki-england.txt'
outputfile = 'jawiki-england_category-name.txt'

f = open(inputfile)
g = open(outputfile, "w")

category = re.compile('\[\[Category:(.+)\]\]')

for line in f:
    l = category.match(line)
    if l:
        g.write(l.group(1) + "\n")

f.close()
g.close()
