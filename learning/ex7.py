# -*- coding: utf-8 -*-

wishlist = [1,2,3,4,5,6,7,8,9,0]

for i in wishlist:
	print(i + 2)
###########################################
print "\v"

i = 0

while i < 8:
	i += 1
	print(i)
###########################################
countries = {
	u"Россия"   : "RU",
	u"Германия" : "DE",
	u"Турция"   : "TR"
}

for country, abbrev in countries.items():
	print u"%s имет аббревиатуру %s" %(country, abbrev)