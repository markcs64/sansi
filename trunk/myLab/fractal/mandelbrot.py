# -*- coding: utf-8 -*-

# z<n+1> = z<n> ^ 2 + c

import time, random
import Image, ImageDraw

g_size = (800, 600)
g_zoom = 0.003
g_offsetX = -200
g_offsetY = 0
g_maxRepeat = 100
g_bailout = 1000

def draw():
	img = Image.new("RGB", g_size, 0xffffff)
	dr = ImageDraw.Draw(img)

	print "painting Mandelbrot .."
	for iy in xrange(g_size[1]):
		print ("%s%d%%..." % ("\b" * 10, iy * 100 / g_size[1])),
		for ix in xrange(g_size[0]):
			y = (iy - g_size[1] / 2 + g_offsetY) * g_zoom
			x = (ix - g_size[0] / 2 + g_offsetX) * g_zoom
			c = complex(x, y)
			r = getRepeats(c)
			dr.point((ix, iy), fill = getColor(r))
	print "%s100%%" % ("\b" * 10)

	del dr
	img.show()
	img.save("mandelbrot.png")

def getRepeats(c):
	z = c
	repeats = 0
	while abs(z) < g_bailout and repeats < g_maxRepeat:
		z = z ** 2 + c
		repeats += 1
	return repeats

def getColor(r):
	color = 0x000000
	if r < g_maxRepeat:
		color = 0xffffff * r / g_maxRepeat
	return color

def main():
	t0 = time.time()
	draw()
	t = time.time() - t0
	print "%dm%.3fs" % (t / 60, t % 60)

if __name__ == "__main__":
	main()
