# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import problem56

class TreeParser():
    def __init__(self):
        self.root = None
        self._stack = [[]]

    def parse(self, tree_string):
        read = []
        for character in tree_string.strip():
            if character == "(":
                self._stack.append([])
            elif character == " ":
                if read:
                    self._stack[-1].append("".join(read))
                    read = []
            elif character == ")":
                if read:
                    self._stack[-1].append("".join(read))
                    read = []
                self._stack[-2].append(self._stack.pop())
            else:
                read.append(character)
        self.root = self._stack.pop()

    def get_phrase(self, tag):
        s = self.root[0][1]
        return self._recursive_finder(s, tag)

    def _recursive_finder(self, lst, tag):
        res = []
        if lst[0] == tag:
            res.append(lst)
        for l in lst[1:]:
            if isinstance(l, list):
                res.extend(self._recursive_finder(l, tag))
        return res

def main(file, tag):
    doc = problem56.StanfordDocument(file)
    sentences = doc.sentences.findall('sentence')
    tag_phases = []

    for sentence in sentences:
        parser = TreeParser()
        tree_string = sentence.find('parse').text
        parser.parse(tree_string)
        tag_phases.append(parser.get_phrase(tag))

    return tag_phases

def str_phrase(phrase):
    res = []
    for p in phrase:
        if isinstance(p, list):
            if isinstance(p[1], list):
                res += str_phrase(p)
            else:
                res.append(p[1])
    return res

if __name__ == "__main__":
    np_phases = main("nlp.txt.xml", "NP")
    for np_phase in np_phases:
        for np in np_phase:
            phase_list = str_phrase(np)
            np_string = problem56.prettifySentence(phase_list)
            print np_string
