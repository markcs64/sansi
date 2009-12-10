# -*- coding: utf-8 -*-

# z<n+1> = z<n> ^ 2 + c

import time, random
import Image, ImageDraw

g_size = (800, 600)
g_zoom = 0.003
g_offset = (-200, 0)
g_maxRepeat = 100
g_bailout = 1000

def draw(antialias = True):
	zi = 1
	if antialias:
		zi = 2
	size = [i * zi for i in g_size]
	zoom = g_zoom / zi
	offset = [i * zi  for i in g_offset]
	bailout = g_bailout * zi
	img = Image.new("RGB", size, 0xffffff)
	dr = ImageDraw.Draw(img)

	print "painting Mandelbrot .."
	for iy in xrange(size[1]):
		print ("%s%d%%..." % ("\b" * 10, iy * 100 / size[1])),
		for ix in xrange(size[0]):
			y = (iy - size[1] / 2 + offset[1]) * zoom
			x = (ix - size[0] / 2 + offset[0]) * zoom
			c = complex(x, y)
			r = getRepeats(c)
			dr.point((ix, iy), fill = getColor(r))
	print "%s100%%" % ("\b" * 10)

	del dr
	if antialias:
		img = img.resize(g_size, Image.ANTIALIAS)
#	img.show()
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
