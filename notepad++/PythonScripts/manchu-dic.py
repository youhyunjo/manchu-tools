from Npp import *
import os
import re
import codecs


if 'MANCHU_ENGLISH_DIC' in globals():
	pass
else:
	#notepad.messageBox('Load Dictionary')
	dicfilename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Manchu-English.txt')
	dicfile = codecs.open(dicfilename, encoding='utf-8')
	MANCHU_ENGLISH_DIC = dicfile.readlines()

class ManchuWord:
	def __init__(self, s):
		# self.voice = r'(bu|mbu)|(n[aeo])|(ji|nji)|(c[aeo])|(nu|ndu)|([td][ae])|([jcx][aeo])'
		self.suffix = ur'((s[aeoi]|t[ae]|ri|i|ni|ng|de|be|ci)|(mbi)|(r[aeo])|([hk][aeo])|(mbihe|mbihebi)|(mahabi)|(rakv)|(h[aeo]kv)|(r[aeo]o)|(ki)|(kini)|(cina)|(k)|(me)|(fi)|(ci)|(h[aeo]i)|(tele|tolo)|(tei|toi)|(nggala|nggele|nggolo)|(cibe)|(ralame|rolame)|(mbime))$'

		self.wordform = self.normalize(s)
		self.stem = self.get_stem()
		
	def normalize(self, s):
		return s.lower().replace('x', 's').replace('v', 'u')
 
	def get_stem(self):
		return re.sub(self.suffix, '', self.wordform)


		
class Search:
	def __init__(self, word, dic):
		self.word = word
		self.dic = dic
		self.exact_entry_match = ''       
		self.exact_body_match = ''
		self.partial_entry_match = ''
		self.partial_body_match = ''
		self.__search()

	def __search(self):
		wordform_found_already = False
		for line in self.dic:
			stem_found = line.find(self.word.stem.upper())
			if stem_found != -1 :
				wordform_found = line.find(self.word.wordform.upper() + ' ')
				if  wordform_found == 0:
					self.exact_entry_match += line
					wordform_found_already = True
				elif wordform_found != -1:
					self.exact_body_match += line
					wordform_found_already = True
				else:
					if wordform_found_already :
						continue
					else:
						if stem_found == 0:
							self.partial_entry_match += line
						else:
							self.partial_body_match += line 
					
	def __str__(self):
		output = ''
		if self.exact_entry_match != '':
			output = self.exact_entry_match
		else:
			output = 'NO ENTRY STARTS WITH: ' + self.word.wordform
			if self.exact_body_match != '':
				output += '\n----\n' + self.exact_body_match
			else:
				output += '\n' + 'NO ENTRY CONTAINS: ' + self.word.wordform
				if self.partial_entry_match != '':
					output += '\n====\nGUESSING CANDIDATES...\n----\n' + self.partial_entry_match
				else:
					output += '\n' + 'NO ENTRY STARTS WITH: ' + self.word.stem
					if self.partial_body_match != '':
						output += '\n----\n' + self.partial_body_match
					else:
						output += '\n' + 'NO ENTRY CONTAINS: ' + self.word.stem
		return output


notepad.messageBox(unicode(Search(ManchuWord(editor.getWord()), MANCHU_ENGLISH_DIC)).encode('utf-8'))

