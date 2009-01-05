# -*- coding: iso-8859-15 -*-

def findNumStr(ns):
	n = 0
	f = open("pi_data_32M_2.txt", "r")
	s = f.read(500)
	i = isIn(s, ns)
	if i >= 0:
		print nss(s, ns)
		print "第一次出现于：", n * 250 + i + 1
		return
	while 1:
		n += 1
		s2 = f.read(250)
		if len(s2) == 0:
			print "没有找到..."
			break
		s = s[250:] + s2
		i = isIn(s[100:400], ns)
		if i >= 0:
			print nss(s, ns)
			print "第一次出现于：", n * 250 + i + 101
			break
	f.close()

def isIn(s, ns):
	try:
		i = s.index(ns)
		return i
	except:
		return -1

def nss(s, ns):
	s = s.replace(ns, ".." + ns + "..")
	return s
		
if __name__ == "__main__":
	while 1:
		print "请输入一个数字：",
		s = raw_input().strip()
		findNumStr(s)
		print