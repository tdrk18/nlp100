# -*- coding: utf-8 -*-
__author__ = 'todoroki'

def func(x, y, z):
    return u"%s時の%sは%s" % (x, y, z)

x = 12
y = u"気温"
z = 22.4
print func(x, y, z)
