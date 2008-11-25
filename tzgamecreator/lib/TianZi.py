# -*- coding: utf-8 -*-

import os
import glob
import copy
from xml.dom.minidom import parse, parseString

class TZ():
	def __init__(self, size = 10, words = []):
		self.size = size
		self.dic = []
		self.words = words
		self.border = []
		self.history = []
		self.curX = 0
		self.curY = 0
		self.step = 0
		self.countX = 0
		self.countY = 0
		self.countC = 0
		self.listX = []
		self.listY = []
		self.hint = {}
		self.length = len(self.words)
		self.dic_list = []
		self.author = ""
		self.clear()

	def clear(self):
		#self.border = [[""] * self.size] * self.size
		self.border = []
		for y in range(self.size):
			self.border.append([])
			for x in range(self.size):
				self.border[y].append("")
		self.log()
		
	def addWord(self, x, y, d, w):
		if len(w) >= 2:
			self.border = self.addWord2(self.border, x, y, d, self.word2list(w))
		else:
			self.border[y][x] = w
		self.log()

	def addWord2(self, bd, x, y, d, wl):
		ii = 0
		if d == 0:	#row
			for i in wl:
				if x + ii < self.size:
					bd[y][x + ii] = i
				ii += 1
		if d == 1:	#col
			for i in wl:
				if y + ii < self.size:
					bd[y + ii][x] = i
				ii += 1
		return bd
	
	def updateSize(self):
		s0 = len(self.border)
		n = self.size
		#尺寸减小
		if s0 > n:
			self.border = self.border[:n]
			for i in range(n):
				self.border[i] = self.border[i][:n]
		#尺寸增加
		elif s0 < n:
			for i in range(s0):
				self.border[i].append([""] * (n - s0))
			self.border.append([[""] * n] * (n - s0))
	
	def word2list(self, w):
		l = []
		for i in range(len(w)/2):
			l.append(w[i*2:i*2+2])
		return l

	def list2word(self, l):
		w = ""
		for i in l:
			w += i
		return w
	
	def importDics(self, dic_list = []):
		if dic_list == []:
			cwd = os.getcwd()
			os.chdir("dic")
			self.dic_list = glob.glob("*.dic")
			for d in self.dic_list:
				self.importDic(d)
			os.chdir(cwd)
		else:
			self.dic_list += dic_list
			for d in dic_list:
				self.importDic(d)
		
		self.dic = []
		for i in self.words:
			self.dic.append(self.list2word(i))
	
	def importDic(self, dic_path):
		if os.path.exists(dic_path):
			lst = []
			f = open(dic_path, "r")
			words = f.read().replace("\r", "").split("\n")
			f.close()
			for w in words:
				if w != "":
					wl = self.word2list(w)
					if wl not in self.words:
						lst.append(wl)
			self.words += lst
			self.words.sort(lambda x, y: cmp(len(y), len(x)))
			self.length = len(self.words)

	def log(self, go = 0):
		self.count2()
		if go == 0:
			self.history = self.history[:self.step]
			self.step += 1
			self.history.append(copy.deepcopy(self.border))
		if go == 1:
			if len(self.history) == self.step:
				return False
			self.step += 1
			self.border = self.history[self.step - 1]
			return True
		if go == -1:
			if self.step == 0:
				return False
			self.step -= 1
			self.border = self.history[self.step - 1]
			return True
	
	def list(self, x, y):
		w = self.border[y][x]
		sx = self.border[y][x:]
		sy = []
		for i in self.border[y:]:
			sy.append(i[x])
		return (self.list2(sx, x, y, 0), self.list2(sy, x, y, 1))
	
	def list2(self, format, x, y, d):
		lst = []
		max_length = len(format)
		for wl in self.words:
			if (len(wl) <= max_length and self.chkFormat(wl, format) and self.isAllInDic(x, y, d, wl)):
				lst.append(self.list2word(wl))
		return lst
	
	def updateHint(self, w, hint = ""):
		if not self.hint.has_key(w):
			self.hint[w] = ""
		self.hint[w] = hint
	
	def chkFormat(self, wl, format):
		for i in range(len(wl)):
			if format[i] != "" and format[i] != wl[i]:
				return False
		return True
	
	def isAllInDic(self, x, y, d, wl):
		return True
		#太耗资源，暂未完成
		bd = self.addWord2(self.border, x, y, d, wl)
		listX, listY = self.getList(bd)
		for wl in listX:
			if wl[1] not in self.words:
				return False
		for wl in listY:
			if wl[1] not in self.words:
				return False
		
		return True
	
	def notInDic(self, bd):
		listX, listY = self.getList(bd)
		notIn = []
		for i in (listX + listY):
			if i[1] not in self.words:
				notIn.append(i)
		return notIn
	
	def count(self, bd):
		listX, listY = self.getList(bd)
		if self.border == bd:
			self.listX = listX
			self.listY = listY
		countX = len(listX)
		countY = len(listY)
		countC = 0
		for y in range(self.size):
			for x in range(self.size):
				if bd[y][x] != "":
					countC += 1
		return countX, countY, countC
	
	def count2(self):
		self.countX, self.countY, self.countC = self.count(self.border)

	def getList(self, bd):
		listX = []
		listY = []
		
		rg = range(self.size)
		size_1 = self.size - 1
		for y in rg:
			isWord = False
			wl = []
			wxy = [0, 0, 0]
			for x in rg:
				if bd[y][x] != "" and isWord == False:
					isWord = True
					wxy = [x, y, 0]
					wl.append(bd[y][x])
				elif bd[y][x] != "" and isWord == True:
					wl.append(bd[y][x])
				if (bd[y][x] == "" or x == size_1) and isWord == True:
					isWord = False
					if len(wl) > 1:
						listX.append((wxy, wl))
					wl = []
		
		for x in rg:
			isWord = False
			wl = []
			wxy = [0, 0, 1]
			for y in rg:
				if bd[y][x] != "" and isWord == False:
					isWord = True
					wxy = [x, y, 1]
					wl.append(bd[y][x])
				elif bd[y][x] != "" and isWord == True:
					wl.append(bd[y][x])
				if (bd[y][x] == "" or y == size_1) and isWord == True:
					isWord = False
					if len(wl) > 1:
						listY.append((wxy, wl))
					wl = []
		
		return listX, listY

	def move(self, dx, dy):
		rg = range(self.size)
		if dx == 1:
			for y in rg:
				self.border[y].pop(self.size - 1)
				self.border[y].insert(0, "")
		if dx == -1:
			for y in rg:
				self.border[y].pop(0)
				self.border[y].append("")
		if dy == 1:
			self.border.pop(self.size - 1)
			self.border.insert(0, [""] * self.size)
		if dy == -1:
			self.border.pop(0)
			self.border.append([""] * self.size)
	
	def toXML(self, author = "oldJ"):
		xml = "<?xml version=\"1.0\" encoding=\"utf-8\" ?>"
		xml += "<tianzi>"
		xml += "<author>" + author + "</author>"
		xml += "<size>" + str(self.size) + "</size>"
		xml += "<content>"
		listX, listY = self.getList(self.border)
		for wl in (listX + listY):
			w = self.list2word(wl[1])
			xml += "<item>"
			xml += "<word x=\"%d\" y=\"%d\" d=\"%d\">%s</word>" % (wl[0][0], wl[0][1], wl[0][2], w)
			xml += "<hint><![CDATA[%s]]></hint>" % self.xmlEncode(self.hint[w])
			xml += "</item>"
		xml += "</content>"
		xml += "</tianzi>"
		return xml.decode("gbk").encode("utf-8")
	
	def loadXML(self, xmlStr):
		xml = parseString(xmlStr)
		self.author = xml.getElementsByTagName("author")[0].firstChild.nodeValue
		items = xml.getElementsByTagName("item")
		words = xml.getElementsByTagName("word")
		self.clear()
		for it in items:
			ob = it.getElementsByTagName("word")[0]
			x = int(ob.getAttribute("x"))
			y = int(ob.getAttribute("y"))
			d = int(ob.getAttribute("d"))
			w = ob.firstChild.nodeValue
			w = w.encode("gbk")
			self.addWord(x, y, d, w)
			h = it.getElementsByTagName("hint")[0]
			if len(h.childNodes) > 0:
				hint = self.xmlDecode(h.firstChild.nodeValue.encode("gbk"))
			else:
				hint = ""
			self.updateHint(w, hint)
	
	def xmlEncode(self, s):
		return s.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;").replace("'", "&apos;").replace("\"", "&quot;")

	def xmlDecode(self, s):
		return s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&apos;", "'").replace("&quot;", "\"")