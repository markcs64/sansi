# -*- coding: utf-8 -*-

import os
import cgi
import time

def findNumStr(ns):
	n = 0
	f = open("D:\\wu\\sansi\\wwwroot\\toy\\pi\\pi.txt", "r")
	# f = open("E:\\studio\\sansi\\toy\\pi\\pi_data_32M_2.txt", "r")
	s = f.read(500)
	i = isIn(s, ns)
	firstFindAt = -1
	nss = ""
	if i >= 0:
		nss = nss2(s, ns)
		firstFindAt = n * 250 + i + 1
		return firstFindAt, nss
	while 1:
		s2 = f.read(250)
		if len(s2) == 0:
			i = isIn(s, ns)
			if i >= 0:
				nss = nss2(s, ns)
				firstFindAt = n * 250 + i + 1
				return firstFindAt, nss
			else:
				return firstFindAt, nss
		n += 1
		s = s[250:] + s2
		i = isIn(s[100:400], ns)
		if i >= 0:
			nss = nss2(s, ns)
			firstFindAt = n * 250 + i + 101
			return firstFindAt, nss
	f.close()

def getQs(qs):
	pass

def isIn(s, ns):
	try:
		i = s.index(ns)
		return i
	except:
		return -1

def isValidNs(ns):
	if len(ns) == 0:
		return False
	try:
		iNs = int(ns)
		return True
	except:
		return False
	

def nss2(s, ns):
	#s = s.replace(ns, "<span style=\"color: red\">" + ns + "</span>")
	return s
		
if __name__ == "__main__":
	#print
	t0 = time.time()
	print("Status: 200 OK")
	print("Content-type: text/xml")
	print()
	
	print("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
	print("<piQuery>")
	qs = cgi.parse()
	#print(qs)
	ns = ""
	isValid = "False"
	try:
		ns = qs["ns"][0]
		isValid = "True"
	except:
		pass
	
	ffa = ""
	nss = ""
	if isValidNs(ns) == True:
		ffa, nss = findNumStr(ns)
		isValid = "True"
	else:
		isValid = "False"
	
	print("<isValid>" + isValid + "</isValid>")
	print("<ns>" + ns + "</ns>")
	print("<firstFindAt>" + str(ffa) + "</firstFindAt>")
	print("<query>" + nss + "</query>")
	print("<time>" + str(time.time() - t0) + "</time>")
	print("</piQuery>")
