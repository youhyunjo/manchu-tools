#
# manchu-validate-align.py
#
# Validates line numbers and alignment marks
# for Manch-Chinese parallel texts in physical format.
#
from Npp import *
import os
import re
import codecs


#while editor.getCurrentPos() < editor.getLength():
#	w = editor.wordRight()


#
# startlinenum = editor.lineFromPosition(editor.getCurrentPos())

flag = False
for n in xrange(0, editor.getLineCount()):
	line = editor.getLine(n)
	if not line.startswith("<"):
		continue
	linenumlang = line[line.find("<")+1:line.find(">")]
	linenum = linenumlang[:-1]
	lang = linenumlang[-1]
	if lang == "m" :
		mnc_linenum = linenum
		mnc_line = line[line.find(">")+1:]
	elif lang == "c":
		chn_linenum = linenum
		chn_line = line[line.find(">")+1:]
		if mnc_linenum == chn_linenum:
			if len(mnc_line.split("&")) == len(chn_line.split("&")):
				pass
			else:
				editor.gotoLine(n)
				notepad.messageBox("ERROR: number of align marks does not match!")
				flag = True
				break			
		else:
			editor.gotoLine(n)
			notepad.messageBox("ERROR: line number does not match!")
			flag = True
			break

if flag is False:
	notepad.messageBox("No error found!")
	