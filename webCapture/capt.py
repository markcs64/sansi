# -*- coding: utf-8 -*-

import os, random, datetime
import threading, time
import urllib, socket

def getList():
	# 得到url列表
	urlList = []
	f = open("list.csv", "r")
	lines = f.readlines()
	f.close()
	for l in lines:
		l = l.replace("\n", "").replace("\r", "")
		if len(l) > 1 and l[0] != "#":
			a = l.split("\t")
			if len(a) == 2:
				a[1] = int(a[1])
				if random.randint(1, 100) <= a[1]:
					urlList.append(a)
	return urlList

def mkFn(url):
	# 根据URL及当前日期生成文件名
	fn = url.replace("http://", "").replace("/", "_")
	dt = datetime.datetime.now()
	fn += "__" + str(dt).replace(":", "_").replace(" ", "_")
	return fn.replace("___", "__")

def saveHTML(url, fn):
	# 保存指定url的HTML源代码
	u = urllib.urlopen(url)
	c = u.read()
	u.close()
	f = open(os.path.join("storage_html", fn + ".html"), "w+")
	f.write(c)
	f.close()

def captOne():
	# 截图
	global g_idx
	global g_urls
	if g_idx >= len(g_urls):
		return
	u = g_urls[g_idx]
	g_idx += 1
	idx = g_idx
	count = len(g_urls)
	print("> (%d/%d) capturing %s ..." % (idx, count, u[0]))
	fn = mkFn(u[0])
	cmd = "iecapt --url=%s --out=storage/%s.png --min-width=1024 --delay=5000 --silent" % (u[0], fn)
	os.system(cmd)
	saveHTML(u[0], fn)
	time.sleep(1)
	#cmd2 = "iecapt --url=%s --out=storage/%s.jpeg --min-width=1024 --delay=5000 --silent" % (u[0], mkFn(u[0]))
	#os.system(cmd2)
	print("] (%d/%d) %s captured!" % (idx, count, u[0]))
	time.sleep(1)
	captOne()

def captUrls():
	threads = []
	n = 10 # 10个线程
	for i in range(n):
		t = threading.Thread(target=captOne)
		threads.append(t)
		t.start()
		time.sleep(1)

if __name__ == "__main__":
	print("web capture!")
	socket.setdefaulttimeout(30)	# 默认超时时间为30秒
	g_idx = 0
	g_urls = getList()
	captUrls()
