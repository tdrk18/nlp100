# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import re
import json
import problem25
import problem26
import problem27

def remove_markup(string):
    markups = [
        re.compile(r"\[https?://[a-zA-Z0-9\./]+\s(.+)?\]"),
        re.compile(r"#REDIRECT\s?(.+)"),
        re.compile(r"<!--\s?(.+)\s?-->"),
        re.compile(r"\{\{.*[Ll]ang\|[a-zA-Z\-]+\|(.+)\}\}"),
        re.compile(r"(.*)<ref.+(</ref>)?>"),
        re.compile(r"(.*?)<br\s?/?>"),
        re.compile(r"<[a-z]+.*>(.*?)</[a-z]+>")
    ]
    removed_string = problem27.remove_internalLink(string)
    for m in markups:
        removed_string = m.sub(r"\1", removed_string)
    return removed_string

if __name__ == "__main__":
    inputfile = 'jawiki-england.txt'
    outputfile = 'jawiki-england_fundamental-rmMUs.json'
    f = open(inputfile)
    res = problem25.fundamental_data(f, remove_markup)
    with open(outputfile, 'w') as g:
        json.dump(res, g, ensure_ascii=False)
