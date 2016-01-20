# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import re

if __name__ == "__main__":
    f = open('nlp.txt', 'r')
    for line in f:
        l = line.strip()
        for word in l.split():
            print re.sub(r"\W", "", word)
        print ""
    f.close()
