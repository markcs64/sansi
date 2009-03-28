# -*- coding: utf-8 -*-

import random

class Life:
    env = None
    gene = ""
    score = 0

    def __init__(self, env, gene = ""):
        self.env = env
        self.gene = gene

        if self.gene == "":
            self.__rndGene()

    def __rndGene(self):
        self.gene = ""
        for i in range(self.env.geneLength):
            self.gene += str(random.randint(0, 1))

    def setScore(self, v):
        self.score = v

    def addScore(self, v):
        self.score += v
