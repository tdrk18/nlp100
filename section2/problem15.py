# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import sys

if len(sys.argv) == 3:
    N = int(sys.argv[1])
    f = open(sys.argv[2])
    lines = f.readlines()[::-1][0:N][::-1]
    for i in xrange(N):
        print lines[i].strip()
    f.close()
else:
    print "please input \'N\' and \'FILENAME\'"

# tail -n 5 hightemp.txt
