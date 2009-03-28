# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageMath
from lib.GA import GA
import os, time

g_xRate = 0.7           # ������
g_mutationRate = 0.005  # ������
g_lifeCount = 50         # ������
g_geneClipLength = 52   # ����Ƭ�γ���
g_geneLength = g_geneClipLength * 100       # ���򳤶�
g_id = str(time.time())


def draw(gene):
    # ���ݻ������ɶ�Ӧ��ͼ��
    global g_geneLength
    # im = Image.new("RGB", (128, 128), (255, 255, 255))
    im = Image.new("L", (128, 128), 255)
    d = ImageDraw.Draw(im)
    for i in range(0, len(gene), g_geneClipLength):
        clip = gene[i:i + g_geneClipLength]
        p1 = int(clip[0:7], 2), int(clip[7:14], 2)
        p2 = int(clip[14:21], 2), int(clip[21:28], 2)
        # rgb = int(clip[28:36], 2), int(clip[36:44], 2), int(clip[44:52], 2)
        # d.line(p1 + p2, rgb)
        clr = int(clip[28:36], 2)
        d.line(p1 + p2, clr)
    del d
    return im

def judge(lf):
    # �ж�һ������ĵ÷�
    global g_im
    score = 0
    im = draw(lf.gene)
    for x in range(0, 128, random.randint(1, 10)):
        for y in range(0, 128, random.randint(1, 10)):
            # print(im.getpixel((x, y)), g_im.getpixel((x, y)))
            if im.getpixel((x, y)) == g_im.getpixel((x, y)):
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
        if steps < 0 or steps > 10000:
            print("���������Ӧ��1 ~ 10000֮�䣡")
            evolve()
            return
    except:
        steps = 1

    global ga
    print("steps: %d" % steps)
    ga.next(steps)
    
    im1 = draw(ga.best.gene)
    im1.show()

    print("\n")
    evolve()

def save(lf):
    # ����
    global g_id
    dir = "sav-" + g_id
    if os.path.isdir(dir) == False:
        os.mkdir(dir)
    im = draw(lf.gene)
    im.save(dir + "\\" + str(lf.env.generation) + ".png")
    print("�ļ��ѱ��浽 %s Ŀ¼" % dir)

def main():
    global ga, g_xRate, g_mutationRate, g_lifeCount, g_geneLength, g_im
    g_im = Image.open("ff.gif")
    print("���ڳ�ʼ��...")
    ga = GA(g_xRate, g_mutationRate, g_lifeCount, g_geneLength, judge, save)

    evolve()

if __name__ == "__main__":
    main()
    # im1 = Image.new("L", (128, 128), 255)
    # im2 = Image.open("ff.gif")
    # print im1.getpixel((50, 50)), im2.getpixel((50, 50))
