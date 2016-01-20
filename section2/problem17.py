# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import sys

if len(sys.argv) == 2:
    f = open(sys.argv[1])
    str_set = set()
    for line in f.readlines():
        str_set.add(line.split()[0])
    f.close()
    for s in str_set:
        print s
else:
    print "please input \'FILENAME\'"

# cat col1.txt | sort | uniq
