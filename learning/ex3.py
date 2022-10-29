# -*- coding: utf-8 -*-

import codecs, sys
outf = codecs.getwriter('utf-8')(sys.stdout, errors = 'replace')
sys.stdout = outf

from sys import argv

script, user_name = argv
prompt = '>'

print u"Привет, %s. Мое имя %r Как дела?" % (user_name, script)
answer = raw_input(prompt).decode(sys.stdin.encoding or locale.getpreferrencoding(True))
print u"Ты ответил \"%s\"" % answer