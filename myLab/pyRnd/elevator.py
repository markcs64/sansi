# -*- coding: utf-8 -*-

"""
电梯（升降机）问题

本程序主要试图模拟大楼乘客高峰期间（如午餐时间）电梯的使用情况，并尝试回答两种不同的乘电梯策略（见电梯就乘及只乘同方向的电梯）哪一种更为高效。
"""

import random, sys

g = {
	"floors": 30,			# 建筑总楼层
	"elevatorCount": 05,	# 总电梯数
	"maxPassagers": 13,		# 每台电梯最多可同时载多少乘客
	"t1": 5.0,				# 电梯启动/停止所需的额外时间（包括开关门）
	"t2": 1.0,				# 电梯正常运行时每经过一层楼所需时间
	"t3": 1.0,				# 每位乘客进入/离开电梯所需的平均时间
	"t4": 09.0,				# 每层楼平均每隔多少时间会新到一位乘客
	"mode": 1,				# 乘客策略，1：见电梯就上；
							# 	2：只坐同方向的电梯；
							# 	0: 随机。
	"time": 0.0,			# 当前相对时间（秒）
	"totalPassagers": 0,	# 当前已运送了多少位乘客到达目的地
	"results": [],			# 记录结果
	"interval": 1.0,		# 系统间隔循环时间
}

class Passager(object):
	waiters = [] # 当前在等待的乘客

	def __init__(self, start = 0, end = 0):
		self.t0 = g["time"] # 开始等待时间
		self.start = start or random.randint(1, g["floors"]) # 起始楼层
		self.end = end
		if self.start != 1:
			# 为简化问题，我们规定所有非一楼的乘客目的都为一楼
			self.end = 1
		else:
			self.end = random.randint(2, g["floors"])	# 用户目的楼层
		self.mode = g["mode"] or random.randint(1, 2)
		self.waiters.append(self)

	def isIn(self, direction):
		# 是否进入电梯
		if self.mode == 1:
			return True
		else:
			d0 = (-1, 1)[self.start - self.end < 0]
			return d0 == direction

	def intoElevator(self, elevator):
		# 进入电梯
		self.waiters.remove(self)
		self.t1 = g["time"]
		self.elevator = elevator
		self.elevator.passagerIn(self)

	def arrival(self):
		# 乘客到达目的地
		g["results"].append((self.start, self.end, g["time"] - self.t0))
		g["totalPassagers"] += 1
		self.elevator.passagerOut(self)

class Elevator(object):
	all = [] # 所有电梯

	def __init__(self, start = 0, step = 1, direction = 0):
		self.floor = start or random.randint(1, g["floors"]) # 电梯起始楼层
		self.passagers = []
		self.step = step
		self.direction = direction # or random.choice((-1, 1)) # 电梯方向
		self.__delay = 0 # 延迟操作
		self.__stopStatus = 0
		self.id = len(self.all) + 1
		self.all.append(self)

	def check(self):
		if self.__delay == 0:
			self.at()
			self.move()
		else:
			self.__delay -= g["interval"]

	def chkStep(self):
		# 检查是否要变化运行方向或停止
		t = self.floor + self.step * self.direction
		if t > g["floors"] or t < 1:
			self.direction *= -1
		if len(self.passagers) == 0:
			self.direction = 0
		if self.direction == 0:
			# 检查最近哪层楼有等待的乘客
			step = self.step
			while self.floor + step <= g["floors"] and \
				self.floor - step >= 1:
				floor = self.floor - step
				if len([p for p in Passager.waiters if p.start == floor]) != 0:
					self.direction = -1
					break
				floor = self.floor + step
				if len([p for p in Passager.waiters if p.start == floor]) != 0:
					self.direction = 1
					break
				step += self.step

	def move(self):
		self.__delay += g["t2"]
		self.chkStep()
		self.floor += self.step * self.direction
		self.__stopStatus = 0

	def at(self):
		# 到达某层楼

		for p in self.passagers:
			if p.end == self.floor:
				p.arrival()
				self.__delay += g["t3"]
				if self.__stopStatus == 0:
					self.__stopStatus = 1

		waiters = Passager.waiters
		for p in waiters:
			if p.start == self.floor and \
				p.isIn(self.direction) and \
				len(self.passagers) < g["maxPassagers"]:
				p.intoElevator(self)
				self.__delay += g["t3"]
				if self.__stopStatus == 0:
					self.__stopStatus = 1

		if self.__stopStatus == 1:
			self.__delay += g["t1"] * 2
			self.__stopStatus = 2

	def passagerIn(self, passager):
		self.passagers.append(passager)

	def passagerOut(self, passager):
		self.passagers.remove(passager)

def showState():
	for ele in Elevator.all:
		waiters = len([p for p in Passager.waiters if p.start == ele.floor])
		print "#%d, floor: %2d, waiters: %3d/%4d, passagers: %2d" % \
			(ele.id, ele.floor, waiters, len(Passager.waiters), len(ele.passagers))
	stat()
	print

def stat():
	totalTime = 0
	for a in g["results"]:
		totalTime += a[-1]
	if g["totalPassagers"] != 0:
		avgTime = totalTime / g["totalPassagers"]
	else:
		avgTime = -1
	print "Passagers: %d, Total time: %.3f, AVG Time: %.3f" % \
		(g["totalPassagers"], totalTime, avgTime)

if __name__ == "__main__":
	for i in range(g["elevatorCount"]):
		Elevator()
	while g["totalPassagers"] < 10000:
		if random.random() < g["interval"] / g["t4"]:
			p = Passager()
		for ele in Elevator.all:
			ele.check()
		if g["time"] % 3600 == 0:
			showState()
		g["time"] += g["interval"]

	stat()

