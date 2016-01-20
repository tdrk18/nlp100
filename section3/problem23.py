# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import re

inputfile = 'jawiki-england.txt'
outputfile = 'jawiki-england_section.txt'

f = open(inputfile)
g = open(outputfile, "w")

section = re.compile(r'=(=+) (.+) =')

for line in f:
    l = section.match(line)
    if l:
        g.write("sec%s : " % len(l.group(1)))
        g.write(l.group(2) + "\n")

f.close()
g.close()
