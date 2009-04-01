# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageMath
from lib.GA import GA
import os, time, random, math

g_xRate = 0.7           # ������
g_mutationRate = 0.005  # ������
g_lifeCount = 500        # ������
g_geneClipLength = 3    # ����Ƭ�γ���
g_geneLength = g_geneClipLength * 1024       # ���򳤶�
g_id = time.strftime("%y%m%d_%H%M%S", time.localtime(time.time()))


def draw(gene):
    # ���ݻ������ɶ�Ӧ��ͼ��
    global g_geneLength
    # im = Image.new("RGB", (128, 128), (255, 255, 255))
    im = Image.new("L", (32, 32), 255)
    d = ImageDraw.Draw(im)
    for y in range(32):
        for x in range(32):
            p = y * 32 + x
            v = int(gene[p:p + g_geneClipLength], 2) * 32
            d.point((x, y), v)
    del d
    return im

def judge(lf, av):
    # �ж�һ������ĵ÷�
    # avΪ��һ�ֵ�����ƽ���÷�
    global g_pix
    j = 0
    match = 0
    for i in range(0, len(lf.gene), g_geneClipLength):
        if g_pix[j] == int(lf.gene[i:i + g_geneClipLength], 2) * 32:
            match += 1
        j += 1

    score = match - 0.9 * av
    if score > av:
        print("\tmatch: %d / %d" % (match, j))
    if score < 1:
        score = 1
    return score

def evolve():
    # �ݻ�
    try:
        steps = int(input("������Ҫ�����Ĵ���(Ĭ��Ϊ1��0�˳�)��"))
        if steps == 0:
            print("�˳�...")
            return
        if steps < 0 or steps > 1000000:
            print("���������Ӧ��1 ~ 1000000֮�䣡")
            evolve()
            return
    except:
        steps = 1

    global ga
    print("steps: %d" % steps)
    ga.next(steps)
    
    print("\n")
    evolve()

def filter(t, step = 32):
    l2 = []
    if type(t) in (type(()), type([])):
        for k in t:
            l2.append(int(k / step) * step)
    elif type(t) == type(1):
        l2 = [int(t / step) * step]
    return tuple(l2)

def save(lf):
    # ����
    global g_id
    dir = "sav-" + g_id
    im = draw(lf.gene)
    im.save(dir + "\\" + str(lf.env.generation) + ".png")
    # print("�ļ��ѱ��浽 %s Ŀ¼" % dir)

def main():
    global ga, g_xRate, g_mutationRate, g_lifeCount, g_geneLength, g_im, g_pix
    # g_im = Image.open("ff.gif").convert("RGB")
    g_im = Image.open("ff.gif").convert("L")
    imn = Image.new("L", (32, 32), 255)
    d = ImageDraw.Draw(imn)
    pix = g_im.load()
    g_pix = []
    for y in range(0, 32):
        for x in range(0, 32):
            p = filter(pix[x * 4, y * 4])[0]
            g_pix.append(p)
            d.point((x, y), p)
    dir = "sav-" + g_id
    if os.path.isdir(dir) == False:
        os.mkdir(dir)
    imn.save(dir + "\\_.png")
    print("���ڳ�ʼ��...")
    ga = GA(g_xRate, g_mutationRate, g_lifeCount, g_geneLength, judge, save)

    evolve()

if __name__ == "__main__":
    main()
