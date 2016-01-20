# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import sys

if len(sys.argv) == 3:
    N = int(sys.argv[1])
    f = open(sys.argv[2])
    rows = f.readlines()
    n, mod = divmod(len(rows), N)
    if mod != 0:
        n += 1
    idx = 0
    for i in xrange(N):
        filename = "split_%s.txt" % (i + 1)
        g = open(filename, "w")
        for j in xrange(n):
            try:
                g.write(rows[idx + j])
            except:
                break
        idx += n
        g.close()
    f.close()

else:
    print "please input \'N\' and \'FILENAME\'"

# split -l 5 hightemp.txt out.
