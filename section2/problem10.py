# -*- coding: utf-8 -*-
__author__ = 'todoroki'

f = open('hightemp.txt')
lines = f.readlines()
print len(lines)
f.close()

# cat hightemp.txt | grep -c ""
