# -*- coding: utf-8 -*-

import wx

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,
                id = -1,
                title = "GA Test",
                size = (400, 300),
                style = wx.DEFAULT_FRAME_STYLE,
                name = "frame")
        panel = wx.Panel(frame, -1)
        frame.Show()
        # func()
        return True

    def mainLoop(self, f = lambda: 1):
        f()
        self.MainLoop()

if __name__ == "__main__":
    app = MyApp()
    app.mainLoop()
