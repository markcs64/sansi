# -*- coding: utf-8 -*-

import random
import os
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

PLACE_COUNT = 5
ANT_COUNT = 5000
PERIOD = 300

g_colors = (
		"#82A970", "#DC9EA6", "#546350", "#CED3AB", "#75A494",
		"#A72D00", "#446000", "#F4C610", "#CF5A00", "#A9B432",
		"#C3C2A6", "#A18C87", "#FEFEFE", "#C7AA80",
	)

class Place(object):
	items = []

	def __init__(self, name):
		self.name = name
		self.clear()
		Place.items.append(self)

	def clear(self):
		self.counts = [0] * PERIOD

	def beVisited(self, period = 0):
		self.counts[period] += 1

class Ant(object):
	items = []

	def __init__(self):
		self.clear()
		Ant.items.append(self)

	def clear(self):
		self.preference = {}
		self.history = []
		for place in Place.items:
			self.preference[place] = random.random()

	def visit(self, period = 0):
		place = max(self.preference.items(), key = lambda x: x[1])[0]
		self.history.append(place)
		place.beVisited(period)
		if place.counts[period] > ANT_COUNT / PLACE_COUNT:
			self.preference[place] *= 0.95
		else:
			self.preference[place] *= 1.05
#			if self.preference[place] > 1.0:
#				self.preference[place] = 1.0

	def communicate(self):
		another = random.choice(Ant.items)
		if another == self:
			return
		for k in self.preference:
			another.preference[k] = (self.preference[k] + another.preference[k]) * 0.5

def plot(vals, aid):
	fig = plt.figure(figsize = (8, 4), facecolor = "w", dpi = 100)
	fig.subplots_adjust(top = 0.93, right = 0.96, bottom = 0.2, left = 0.09)
	plt.grid(True)
	plt.xlabel(u"Period")
	plt.ylabel(u"Count")

	for i, v in enumerate(vals):
		plt.plot(v, "k", color = g_colors[i])

#	plt.show()
	plt.savefig(os.path.join("ant", "ant_%d.%d.png" % (PLACE_COUNT, aid)))

def act(aid):
	for pid in range(PERIOD):
		for ant in Ant.items:
			ant.visit(pid)
			ant.communicate()

	vals = []
	for p in Place.items:
		vals.append(p.counts)
	plot(vals, aid)

def clear():
	for p in Place.items:
		p.clear()
	for a in Ant.items:
		a.clear()

def init():
	for i in range(PLACE_COUNT):
		Place(str(i + 1))
	for i in range(ANT_COUNT):
		ant = Ant()

def main():
	init()
	if os.path.isdir("ant") == False:
		os.mkdir("ant")
	n = 50
	for i in range(n):
		act(i)
		clear()
		print "%d / %d done!" % (i, n)

if __name__ == "__main__":
	main()
