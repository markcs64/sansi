#coding=utf-8

import time
#path = "D:\\wu\\sansi\\wwwroot\\toy\\mg\\stat\\"
path = "E:\\studio\\sansi\\wwwroot\\toy\\mg\\stat\\"

def isLock():
    f = open(path + "isLock.ini", "r")
    c = f.read()
    r = False
    if c == "1":
        r = True
    f.close()
    return r

def lock(v):
    while (isLock() and v == 1):
        time.sleep(1)
    f = open(path + "isLock.ini", "w+")
    f.write(str(v))
    f.close()

def count():
    lock(1)
    f = open(path + "data.ini", "r")
    d = f.read()
    f.close()
    if d != "":
        d = int(d) + 1
    else:
        d = 1
    lock(0)
    f = open(path + "data.ini", "w+")
    f.write(str(d))
    f.close()
    return d

if __name__ == "__main__":
    print "Status: 200 OK"
    print "Content-type: text/plain"
    print
    print "%d" % count()
