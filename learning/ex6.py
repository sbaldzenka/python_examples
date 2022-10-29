# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

read_data = open(from_file)
data = read_data.read()

print u"Исходный файл имеет размер %d байт." % len(data)

write_data = open(to_file, 'w')
write_data.write(data)

read_data.close()
write_data.close()

print u"Данные скопированы."