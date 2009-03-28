# -*- coding: utf-8 -*-

import random
from Life import Life

class GA:
    xRate = 0.7
    mutationRate = 0.005
    lifeCount = 50
    geneLength = 100
    mutationCount = 0
    generation = 0
    bestHistory = []
    lives = []
    bounds = 0  # 得分总数
    best = None

    def __init__(self, xRate = 0.7, mutationRate = 0.005, lifeCount = 50, geneLength = 100, judge = lambda lf: 1):
        self.xRate = xRate
        self.mutationRate = mutationRate
        self.lifeCount = lifeCount
        self.geneLength = geneLength
        self.__judge = judge

        for i in range(lifeCount):
            self.lives.append(Life(self))

    def __bear(self, p1, p2):
        # 根据父母 p1, p2 生成一个后代
        r = random.random()
        if r < self.xRate:
            # 交叉
            r = random.randint(0, self.geneLength)
            gene = p1.gene[0:r] + p2.gene[r:]
        else:
            gene = p1.gene

        r = random.random()
        if r < self.mutationRate:
            # 突变
            r = random.randint(0, self.geneLength)
            gene = gene[:r] + ("0", "1")[gene[r:r] == "1"] + gene[r + 1:]
            self.mutationCount += 1

        return Life(self, gene)

    def __getOne(self):
        # 根据得分情况，随机取得一个个体，机率正比于个体的score属性
        r = random.uniform(0, self.bounds)
        for lf in self.lives:
            r -= lf.score;
            if r <= 0:
                return lf

    """def __getBounds(self):
        # 取得总分及本代中得分最高的个体
        self.bounds = 0
        self.best = Life(self)
        self.best.setScore(-1)
        for lf in self.lives:
            if lf.score > self.best.score:
                self.best = lf
            self.bounds += lf.score"""

    def __newChild(self):
        # 产生新的后代
        return self.__bear(self.__getOne(), self.__getOne())

    def judge(self, f = lambda lf: 1):
        # 根据传入的方法 f ，计算每个个体的得分
        self.bounds = 0
        self.best = Life(self)
        self.best.setScore(-1)
        for lf in self.lives:
            lf.score = f(lf)
            if lf.score > self.best.score:
                self.best = lf
            self.bounds += lf.score

    def next(self, n = 1):
        # 演化至下一代
        newLives = []
        # self.__getBounds()
        self.judge(self.__judge)
        self.bestHistory.append(self.best)
        while (len(newLives) < self.lifeCount):
            newLives.append(self.__newChild())
        self.lives = newLives
        self.generation += 1
        print("gen: %d" % self.generation)

        if n > 1:
            self.next(n - 1)
