# -*- coding: utf-8 -*-
# TSP 问题

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from lib.GA import GA
import os, time, random, math, thread

class OpenGLWindow():
    rx = 0.0
    ry = 0.0
    rz = 0.0

    def __init__(self, points = [], width = 640, height = 480, title = "TSP问题"):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(width, height)
        self.window = glutCreateWindow(title)
        self.points = points
        glutDisplayFunc(self.Draw)
        glutIdleFunc(self.Draw)
        self.InitGL(width, height)

    def point(self, x, y, z):
        # 在画布上画一个*点
        glBegin(GL_LINES)
        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(x - 0.05, y, z)
        glVertex3f(x + 0.05, y, z)
        glVertex3f(x, y - 0.05, z)
        glVertex3f(x, y + 0.05, z)
        glVertex3f(x, y, z - 0.05)
        glVertex3f(x, y, z + 0.05)
        glEnd()

    def line(self, order):
        # 将画布上的点按指定顺序连线
        glBegin(GL_LINE_STRIP)
        glColor3f(1.0, 1.0, 1.0)
        lst = order + [order[0]]
        for i in range(len(lst) - 1):
            glVertex3f(self.points[lst[i]][0], self.points[lst[i]][1], self.points[lst[i]][2])
            glVertex3f(self.points[lst[i + 1]][0], self.points[lst[i + 1]][1], self.points[lst[i + 1]][2])
        glEnd()

    def info(self, s = ["TSP Question"]):
        # 绘制信息
        glColor3f(1.0, 1.0, 1.0)
        y = 0.0
        for line in s:
            glRasterPos2f(0.0, y)
            y -= 0.2
            for c in line:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))

    def Draw(self):
        global curOrder, g_distance
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(1.5, 0.0, -7.0)
        glRotatef(self.rx, 1.0, 0.0, 0.0)
        glRotatef(self.ry, 0.0, 1.0, 0.0)
        glRotatef(self.rz, 0.0, 0.0, 1.0)
        for p in self.points:
            self.point(p[0], p[1], p[2])
        self.line(curOrder)
        self.info(["distance: %f" % g_distance])
        glutSwapBuffers()
        self.rx += 0.05
        self.ry += 0.05
        self.rz += 0.05

    def InitGL(self, width, height):
        glClearColor(0.25, 0.25, 0.25, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def MainLoop(self, f = lambda: 1):
        thread.start_new_thread(f, ())
        glutMainLoop()

def mkPoints(n):
    # 随机产生若干个点
    ps = []
    for i in range(n):
        ps.append((random.random() * 4 - 3, random.random() * 4 - 1.5, random.random() * 5 - 3))
    return ps

def mkLife():
    # 产生生命的函数
    # lst = ["00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111", "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111", "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111", "11000", "11001", "11010", "11011", "11100", "11101", "11110", "11111"]
    global pointCount
    lst = range(pointCount)
    random.shuffle(lst)
    return lst

def getDistance(lst):
    # 得到一个序列点之间的总距离
    global points
    dst = 0.0
    lst2 = lst + [lst[0]]
    for i in range(0, len(lst2)):
        dst += math.sqrt(
                math.pow(points[lst2[i]][0] - points[lst2[i - 1]][0], 2) +
                math.pow(points[lst2[i]][1] - points[lst2[i - 1]][1], 2) +
                math.pow(points[lst2[i]][2] - points[lst2[i - 1]][2], 2)
            )
    return dst

def judge(lf, av = 100):
    # 评估函数
    global points
    # print(lf.gene)
    dst = getDistance(lf.gene)
    score = 1.0 / dst
    # print("dst: %f, score: %f, av: %f" % (dst, score, av))
    return score

def xFunc(lf1, lf2):
    # 交叉函数
    global pointCount
    p1 = random.randint(0, pointCount - 1)
    p2 = random.randint(pointCount - 1, pointCount)
    g1 = lf2.gene[p1:p2] + lf1.gene
    # g2 = lf1.gene[p1:p2] + lf2.gene
    g11 = []
    for i in g1:
        if i not in g11:
            g11.append(i)
    return g11

def mFunc(gene):
    # 变异函数
    global pointCount
    p1 = random.randint(0, pointCount - 2)
    p2 = random.randint(pointCount - 2, pointCount - 1)
    gene[p1], gene[p2] = gene[p2], gene[p1]
    return gene

def save(lf):
    # 保存值
    global points, curOrder, g_distance
    curOrder = lf.gene
    g_distance = getDistance(curOrder)

def order0():
    # 初始线条
    global pointCount, points, curOrder, g_distance
    curOrder = range(pointCount)
    g_distance = getDistance(curOrder)

def evolve():
    for i in range(1000):
        ga.next()
        # time.sleep(0.1)

def tspq():
    # TSP问题
    global points, ga, curOrder
    ga = GA(lifeCount = 500,
            geneLength = 160,
            judge = judge,
            save = save,
            mkLife = mkLife,
            xFunc = xFunc,
            mFunc = mFunc
        )
    evolve()

if __name__ == "__main__":
    global pointCount, points, curOrder
    pointCount = 32
    points = mkPoints(pointCount)
    order0()
    window = OpenGLWindow(points)
    window.MainLoop(tspq)
