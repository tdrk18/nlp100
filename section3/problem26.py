# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import re
import json
import problem25

def remove_emphasis(string):
    emphasis = re.compile(r"''('*)(.+)''\1")
    return emphasis.sub(r"\2", string)

if __name__ == "__main__":
    inputfile = 'jawiki-england.txt'
    outputfile = 'jawiki-england_fundamental-rmEmpha.json'
    f = open(inputfile)
    res = problem25.fundamental_data(f, remove_emphasis)
    with open(outputfile, 'w') as g:
        json.dump(res, g, ensure_ascii=False)
