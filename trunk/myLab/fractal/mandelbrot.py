# -*- coding: utf-8 -*-

# z<n+1> = z<n> ^ 2 + c

import time, random
import Image, ImageDraw

g_size = (600, 480)
g_maxIteration = 4096
g_bailout = 4
g_zoom = 2.5 / g_size[0]
g_offset = (-g_size[0] * 0.25, 0)

def draw(antialias = True):
	zi = 1
	if antialias: # 抗锯齿
		zi = 2
	size = [i * zi for i in g_size]
	zoom = g_zoom / zi
	offset = [i * zi  for i in g_offset]
	bailout = g_bailout * zi
	img = Image.new("RGB", size, 0xffffff)
	dr = ImageDraw.Draw(img)

	print "painting Mandelbrot .."
	for p in getPoints(size, offset, zoom):
		dr.point(p[0], fill = p[1])
	print "%s100%%" % ("\b" * 10)

	del dr
	if antialias:
		img = img.resize(g_size, Image.ANTIALIAS)
#	img.show()
	img.save("mandelbrot.png")

def getPoints(size, offset, zoom, ti = 0, tstep = 1):
	"生成需要绘制的点的坐标及颜色"

	def getRepeats(c):
		z = c
		repeats = 0
		while abs(z) < g_bailout and repeats < g_maxIteration:
			z = z ** 2 + c
			repeats += 1
		return repeats

	def getColor(r):
		color = 0
		if r < g_maxIteration:
			color = int(0xffffff * r / g_maxIteration)
		return color

	xs, ys = size
	for iy in xrange(ys):
		print ("%s%d%%..." % ("\b" * 10, iy * 100 / ys)),
		for ix in xrange(ti, xs, tstep):
			y = (iy - ys / 2 + offset[1]) * zoom
			x = (ix - xs / 2 + offset[0]) * zoom
			c = complex(x, y)
			r = getRepeats(c)
			yield (ix, iy), getColor(r)

def main():
	t0 = time.time()
	draw()
	t = time.time() - t0
	print "%dm%.3fs" % (t / 60, t % 60)

if __name__ == "__main__":
	main()
