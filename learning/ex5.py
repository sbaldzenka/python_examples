# -*- coding: utf-8 -*-

import codecs, sys
outf = codecs.getwriter('utf-8')(sys.stdout, errors = 'replace')
sys.stdout = outf

from sys import argv
script, filename = argv

print u"Файл %s" % filename
print u"Нажмите Enter чтобы стереть файл, нажмите CTRL+C для отмены."
raw_input(">")

print u"Открытие файла..."
target = open(filename, 'w')

print u"Очистка файла."
target.truncate()

print u"Введите 3 строки:"
line1 = raw_input(u"Строка 1> ")
line2 = raw_input(u"Строка 2> ")
line3 = raw_input(u"Строка 3> ")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.close()
print u"Сохранено в файл."