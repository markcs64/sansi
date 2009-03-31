# -*- coding: utf-8 -*-

import random, math
from Life import Life

class GA:
    xRate = 0.7
    mutationRate = 0.005
    lifeCount = 50
    geneLength = 100
    mutationCount = 0
    generation = 0
    # bestHistory = []
    lives = []
    bounds = 0  # �÷�����
    best = None
    saveEvery = 1

    def __init__(self, xRate = 0.7, mutationRate = 0.005, lifeCount = 50, geneLength = 100, judge = lambda lf: 1, save = lambda: 1):
        self.xRate = xRate
        self.mutationRate = mutationRate
        self.lifeCount = lifeCount
        self.geneLength = geneLength
        self.__judge = judge
        self.save = save

        for i in range(lifeCount):
            self.lives.append(Life(self))

    def __bear(self, p1, p2):
        # ���ݸ�ĸ p1, p2 ����һ�����
        r = random.random()
        if r < self.xRate:
            # ����
            r = random.randint(0, self.geneLength)
            gene = p1.gene[0:r] + p2.gene[r:]
        else:
            gene = p1.gene

        r = random.random()
        if r < self.mutationRate:
            # ͻ��
            r = random.randint(0, self.geneLength - 1)
            gene = gene[:r] + ("0", "1")[gene[r:r] == "1"] + gene[r + 1:]
            self.mutationCount += 1

        return Life(self, gene)

    def __getOne(self):
        # ���ݵ÷���������ȡ��һ�����壬���������ڸ����score����
        r = random.uniform(0, self.bounds)
        for lf in self.lives:
            r -= lf.score;
            if r <= 0:
                return lf

    def __newChild(self):
        # �����µĺ��
        return self.__bear(self.__getOne(), self.__getOne())

    def judge(self, f = lambda lf: 1):
        # ���ݴ���ķ��� f ������ÿ������ĵ÷�
        self.bounds = 0
        self.best = Life(self)
        self.best.setScore(-1)
        for lf in self.lives:
            lf.score = f(lf)
            if lf.score > self.best.score:
                self.best = lf
            self.bounds += lf.score

    def next(self, n = 1):
        # �ݻ�����n��
        while n > 0:
            newLives = []
            # self.__getBounds()
            self.judge(self.__judge)
            # self.bestHistory.append(self.best)
            while (len(newLives) < self.lifeCount):
                newLives.append(self.__newChild())
            self.lives = newLives
            self.generation += 1
            print("gen: %d, mutation: %d, best: %d, p: %d" % (self.generation, self.mutationCount, self.best.score, math.sqrt(self.best.score) + 130))
            if (100 < self.generation <= 1000):
                self.saveEvery = 10
            elif (1000 < self.generation <= 10000):
                self.saveEvery = 100
            elif (10000 < self.generation <= 100000):
                self.saveEvery = 1000
            elif (100000 < self.generation):
                self.saveEvery = 10000

            if self.generation % self.saveEvery == 0:
                self.save(self.best)

            n -= 1
