# -*- coding: utf-8 -*-

import mystuff

mystuff.apple()

print "%d" % mystuff.tangerine

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		
		for line in self.lyrics:
			print line

happy_bday = Song(["happy b-day to you","happy b-day to you"])	

happy_bday.sing_me_a_song()		