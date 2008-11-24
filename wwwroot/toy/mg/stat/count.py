#coding=utf-8

import os, time
#path = os.path.abspath(os.path.join(os.getcwd(), __file__))

def getPath(fn):
    return os.path.abspath(os.path.join(os.getcwd(), fn))

def isLock():
    f = open(getPath("isLock.ini"), "r")
    c = f.read()
    r = False
    if c == "1":
        r = True
    f.close()
    return r

def lock(v):
    while (isLock() and v == 1):
        time.sleep(1)
    f = open(getPath("isLock.ini"), "w+")
    f.write(str(v))
    f.close()

def count():
    lock(1)
    f = open(getPath("data.ini"), "r")
    d = f.read()
    f.close()
    if d != "":
        d = int(d) + 1
    else:
        d = 1
    lock(0)
    f = open(getPath("data.ini"), "w+")
    f.write(str(d))
    f.close()
    return d

if __name__ == "__main__":
    print "Status: 200 OK"
    print "Content-type: text/plain"
    print
    print "%d" % count()
