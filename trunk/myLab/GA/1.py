# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageMath
from lib.GA import GA
import os, time, random

g_xRate = 0.7           # ������
g_mutationRate = 0.005  # ������
g_lifeCount = 50         # ������
g_geneClipLength = 36   # ����Ƭ�γ���
g_geneLength = g_geneClipLength * 1000       # ���򳤶�
g_id = time.strftime("%y%m%d_%H%M%S", time.localtime(time.time()))


def draw(gene):
    # ���ݻ������ɶ�Ӧ��ͼ��
    global g_geneLength
    # im = Image.new("RGB", (128, 128), (255, 255, 255))
    im = Image.new("L", (128, 128), 255)
    d = ImageDraw.Draw(im)
    points = []
    for i in range(0, len(gene), g_geneClipLength):
        clip = gene[i:i + g_geneClipLength]
        p1 = int(clip[0:7], 2), int(clip[7:14], 2)
        p2 = int(clip[14:21], 2), int(clip[21:28], 2)
        # rgb = int(clip[28:36], 2), int(clip[36:44], 2), int(clip[44:52], 2)
        rgb = int(clip[28:36], 2)
        # d.line(p1 + p2, rgb)
        d.point(p1, rgb)
        d.point(p2, rgb)
        points.append(p1)
        points.append(p2)
    del d
    return im, points

def judge(lf):
    # �ж�һ������ĵ÷�
    global g_im, g_pix
    score = 0
    im, points = draw(lf.gene)
    pix = im.load()
    for point in points:
        # if pix[x, y] == g_pix[x, y]:
        if pix[point] == g_pix[point]:
            score += 1
    # print score
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
    
    # im1 = draw(ga.best.gene)
    # im1.show()

    print("\n")
    evolve()

def save(lf):
    # ����
    global g_id
    dir = "sav-" + g_id
    im, points = draw(lf.gene)
    im.save(dir + "\\" + str(lf.env.generation) + ".png")
    print("�ļ��ѱ��浽 %s Ŀ¼" % dir)

def main():
    global ga, g_xRate, g_mutationRate, g_lifeCount, g_geneLength, g_im, g_pix
    # g_im = Image.open("ff.gif").convert("RGB")
    g_im = Image.open("ff.gif").convert("L")
    dir = "sav-" + g_id
    if os.path.isdir(dir) == False:
        os.mkdir(dir)
    g_im.save(dir + "\\_.png")
    g_pix = g_im.load()
    print("���ڳ�ʼ��...")
    ga = GA(g_xRate, g_mutationRate, g_lifeCount, g_geneLength, judge, save)

    evolve()

if __name__ == "__main__":
    main()
    # im1 = Image.new("RGB", (128, 128), (255, 255, 255))
    # im2 = Image.open("ff.gif").convert("RGB")
    # print im1.getpixel((50, 50)), im2.getpixel((50, 50))
    # pix1 = im1.load()
    # pix2 = im2.load()
    # print pix1[50, 50], pix2[50, 50]
    # for x in range(128):
        # for y in range(128):
            # pix1[x, y] = pix2[x, y]
    # im1.show()
