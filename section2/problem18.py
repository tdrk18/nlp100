# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import sys

if len(sys.argv) == 2:
    f = open(sys.argv[1])
    lines = f.readlines()
    sorted_lines = sorted(lines, key=(lambda x:float(x.split()[2])), reverse=True)
    g = open("sorted_hightemp.txt", "w")
    for line in sorted_lines:
        g.write(line.strip() + "\n")
    g.close()
    f.close()
else:
    print "please input \'FILENAME\'"

# sort -r -k 3 hightemp.txt
