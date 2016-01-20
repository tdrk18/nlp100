# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import sys

if len(sys.argv) == 2:
    f = open(sys.argv[1])
    lines = f.readlines()
    count = {}
    for line in lines:
        l = line.split()[0]
        if count.has_key(l):
            count[l] += 1
        else:
            count[l] = 1
    for k, v in sorted(count.items(), key=(lambda x:x[1]), reverse=True):
        print k
else:
    print "please input \'FILENAME\'"

# cut -f 1 hightemp.txt | sort  | uniq -c | sort -n -r | less
