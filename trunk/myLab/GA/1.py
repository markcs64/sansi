# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageMath
from lib.GA import GA

g_xRate = 0.7           # ������
g_mutationRate = 0.005  # ������
g_lifeCount = 10       # ������
g_geneLength = 40 * 100       # ���򳤶�


def draw(gene):
    # ���ݻ������ɶ�Ӧ��ͼ��
    global g_geneLength
    im = Image.new("RGB", (128, 128), (255, 255, 255))
    d = ImageDraw.Draw(im)
    for i in range(0, len(gene), g_geneLength):
        clip = gene[i:g_geneLength]
        p1 = int(clip[0:7], 2), int(clip[7:14], 2)
        p2 = int(clip[14:21], 2), int(clip[21:28], 2)
        rgb = int(clip[28:32], 2), int(clip[32:36], 2), int(clip[36:40], 2)
        d.line(p1 + p2, rgb)
    del d
    return im

def judge(lf):
    # �ж�һ������ĵ÷�
    global g_im
    score = 0
    im = draw(lf.gene)
    im.show()
    return score

def main():
    try:
        steps = int(input("������Ҫ�����Ĵ���(Ĭ��Ϊ1)��"))
        if steps < 0 or steps > 10000:
            print("���������Ӧ��1 ~ 10000֮�䣡")
            main()
            return
    except:
        steps = 1

    print("steps: %d" % steps)
    global g_xRate, g_mutationRate, g_lifeCount, g_geneLength, g_im
    g_im = Image.open("ff.gif")
    ga = GA(g_xRate, g_mutationRate, g_lifeCount, g_geneLength, judge)
    ga.next(steps)

if __name__ == "__main__":
    main()
    im2 = Image.open("ff.gif")
    #im.rotate(45).show()
    #print im.getpixel((50, 60))
    #print im.getdata()
    #im.show()
    #out = ImageMath.eval("convert(min(a, b), 'L')", a = im1, b = im2)
    #out.show()
