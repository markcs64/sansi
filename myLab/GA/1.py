# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageMath
from lib.GA import GA
import os, time, random, math

g_xRate = 0.7           # 交叉率
g_mutationRate = 0.005  # 变异率
g_lifeCount = 500        # 个体数
g_geneClipLength = 3    # 基因片段长度
g_geneLength = g_geneClipLength * 1024       # 基因长度
g_id = time.strftime("%y%m%d_%H%M%S", time.localtime(time.time()))


def draw(gene):
    # 根据基因生成对应的图形
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
    # 判断一个个体的得分
    # av为上一轮迭代的平均得分
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
    # 演化
    try:
        steps = int(input("请输入要迭代的次数(默认为1，0退出)："))
        if steps == 0:
            print("退出...")
            return
        if steps < 0 or steps > 1000000:
            print("输入的数字应在1 ~ 1000000之间！")
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
    # 保存
    global g_id
    dir = "sav-" + g_id
    im = draw(lf.gene)
    im.save(dir + "\\" + str(lf.env.generation) + ".png")
    # print("文件已保存到 %s 目录" % dir)

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
    print("正在初始化...")
    ga = GA(g_xRate, g_mutationRate, g_lifeCount, g_geneLength, judge, save)

    evolve()

if __name__ == "__main__":
    main()
