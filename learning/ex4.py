# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

txt = open(filename)

print u"Содержимое файла %r:" % filename
print txt.read()