# -*- code: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk, gtk.glade
import glib, math, time, random
from lib.GA import GA

class CairoDraw(gtk.DrawingArea):
	def __init__(self):
		super(self.__class__, self).__init__()

class TSP_GTK:
	ps = []

	def __init__(self):
		self.gladefile = "win.glade"
		self.wTree = gtk.glade.XML(self.gladefile)
		self.window = self.wTree.get_widget("winMain")
		self.window.connect("destroy", gtk.main_quit)
		self.cr = CairoDraw()
		self.area = self.wTree.get_widget("alignment1")
		self.area.set_size_request(320, 320)
		self.area.add(self.cr)
		self.cr.connect("expose-event", self.on_expose)
		signal = {"on_btnAct_clicked": self.act}
		self.wTree.signal_autoconnect(signal)
		self.txtMsg = self.wTree.get_widget("txtMsg")
		self.txtMsg.set_text = "123"
		self.__mkTree()

	def on_expose(self, widget, event):
		self.gc = widget.window.cairo_create()
		self.gc.rectangle(event.area.x, event.area.y, event.area.width, event.area.height)
		self.gc.clip()
		self.draw()

	def draw(self):
		print 2
		rect = self.area.get_allocation()
		#print rect.x, rect.y, rect.width, rect.height
		self.gc.rectangle(0, 0, rect.width, rect.height)
		self.gc.set_source_rgb(1, 1, 1)
		self.gc.fill_preserve()
		self.gc.set_source_rgb(0, 0, 0)
		self.gc.stroke()

		self.__drawPoints()

	def act(self, widget):
		self.__mkPoints(32)

	def __mkTree(self):
		self.treePoints = self.wTree.get_widget("treePoints")
		self.colPointNum = gtk.TreeViewColumn("ID")
		self.treePoints.append_column(self.colPointNum)
		self.cell = gtk.CellRendererText()
		self.colPointNum.pack_start(self.cell, True)
		self.colPointNum.add_attribute(self.cell, "text", 0)

	def __mkPoints(self, n):
		#make some points randomly
		self.ps = []
		for i in range(n):
			p = (int(random.random() * 320), int(random.random() * 320))
			self.ps.append(p)

	def __drawPoints(self):
		self.gc.set_source_rgb(1, 0, 0)
		for p in self.ps:
			self.gc.move_to(p[0], p[1])
			self.gc.line_to(p[1], p[0])
		self.gc.stroke()
		print 1

	def main(self):
		self.window.show_all()
		gtk.main()

if __name__ == "__main__":
	tsp = TSP_GTK()
	tsp.main()
