# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import re
import json
import problem25
import problem26

def remove_internalLink(string):
    internallink = re.compile(r"\[\[((.+?)\|)?(.+?)\]\]")
    emphasis_removed = problem26.remove_emphasis(string)
    return internallink.sub(r"\3", emphasis_removed)

if __name__ == "__main__":
    inputfile = 'jawiki-england.txt'
    outputfile = 'jawiki-england_fundamental-rmEmpha-rmLink.json'
    f = open(inputfile)
    res = problem25.fundamental_data(f, remove_internalLink)
    with open(outputfile, 'w') as g:
        json.dump(res, g, ensure_ascii=False)
