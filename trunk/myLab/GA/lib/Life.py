# -*- coding: utf-8 -*-

import random

class Life:
    env = None
    gene = ""
    score = 0

    def __init__(self, env, gene):
        self.env = env
        self.gene = gene

        if self.gene == "":
            self.__rndGene()

    def __rndGene():
        self.gene = ""
        for i in range(self.env.geneLength):
            self.gene += str(random.randomint(0, 1))

    def setScore(v):
        self.score = v

    def addScore(v):
        self.score += v
