# -*- coding: utf-8 -*-

import wx
import wx.grid
import wx.html

import cStringIO
import os
import thread

import lib.PyAUI as PyAUI
import lib.TianZi as TZ

ID_CreateTree = wx.ID_HIGHEST+1
ID_CreateGrid = ID_CreateTree+2
ID_CreateText = ID_CreateTree+3
ID_CreateHTML = ID_CreateTree+4
ID_CreateSizeReport = ID_CreateTree+5
ID_GridContent = ID_CreateTree+6
ID_TextContent = ID_CreateTree+7
ID_TreeContent = ID_CreateTree+8
ID_HTMLContent = ID_CreateTree+9
ID_SizeReportContent = ID_CreateTree+10
ID_CreatePerspective = ID_CreateTree+11
ID_CopyPerspective = ID_CreateTree+12
ID_AllowFloating = ID_CreateTree+13
ID_AllowActivePane = ID_CreateTree+14
ID_TransparentHint = ID_CreateTree+15
ID_TransparentHintFade = ID_CreateTree+16
ID_TransparentDrag = ID_CreateTree+17
ID_NoGradient = ID_CreateTree+18
ID_VerticalGradient = ID_CreateTree+19
ID_HorizontalGradient = ID_CreateTree+20
ID_Settings = ID_CreateTree+21
ID_About = ID_CreateTree+22
ID_FirstPerspective = ID_CreatePerspective+1000

ID_CreateListBox = ID_CreateTree + 23
ID_ListX = ID_CreateTree + 24
ID_ListY = ID_CreateTree + 25
ID_HintX = ID_CreateTree + 26
ID_HintY = ID_CreateTree + 27
ID_TZSize = ID_CreateTree + 28
ID_UnDo = ID_CreateTree + 29
ID_ReDo = ID_CreateTree + 30
ID_MoveUp = ID_CreateTree + 31
ID_MoveRight = ID_CreateTree + 32
ID_MoveDown = ID_CreateTree + 33
ID_MoveLeft = ID_CreateTree + 34
ID_FileOpen = ID_CreateTree + 35
ID_FileSave = ID_CreateTree + 36
ID_MenuOpen = ID_CreateTree + 37
ID_MenuSave = ID_CreateTree + 38
ID_MenuSaveAs = ID_CreateTree + 39
ID_Clear = ID_CreateTree + 40
ID_MenuClear = ID_CreateTree + 41
ID_Check = ID_CreateTree + 42
ID_Quit = ID_CreateTree + 43
ID_ListWords = ID_CreateTree + 44
ID_ListWords_Box = ID_CreateTree + 45
ID_FileNew = ID_CreateTree + 46
ID_MenuNew = ID_CreateTree + 47

#----------------------------------------------------------------------
def GetMondrianData():
	return \
'\x00\x00\x01\x00\x01\x00\x10\x10\x0005701h\x03\x00\x00\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00\x18\x00\x00\x00\x00\x00@\x03\x00\x00GFleming\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd8\xd8\xd8\xd8\xd8\xd8\xd8\xd8\xd8\xb7\xb7\xb7\x97\x97\x97\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xd8\xd8\xd8\xd8\xd8\xd8\xb7\xb7\xb7\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xd8\xd8\xd8\xd8\xd8\xd8\xb7\xb7\xb7lll\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xf8\xf8\xf8\xd8\xd8\xd8\x9b\x9b\x9b[[[\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd8\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf8\xf8\xf8\xf8\xf8ooo\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00QQ\xff\x00\x00\xd8\x00\x00\x00\xea\xea\xea\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|||\x00\x00\x00\x00\x00\xd8\x00\x00\xd8\x00\x00\x00\x00\x00\x00\x00\x00\x00QQ\xff&&\xff\xff\xff\xff\x00\x00\x00\xcc\xcc\xcc\x00\x00\x00\xb2\xb2\xb2\x00\x00\x00\xac\xac\xac\x00\x00\x00\x00\x00\xd8\x00\x00\xd8\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x83\x83\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd8\x00\x00\xd8\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x83\x83\xff\x83\x83\xff\xff\xff\xff\xff\xff\xffQQ\xff&&\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\xff\xff\xff\xff\xff\xff\x00\x00\x9b\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb1\xb1\xff\x83\x83\xff\x83\x83\xffQQ\xffQQ\xffQQ\xffQQ\xff\xff\xff\xff\xff\xff\xff\x1e\x1e\xff\x00\x00\xf2\x00\x00\xcd\x00\x00\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb1\xb1\xff\xff\xff\xff\x83\x83\xff\xff\xff\xff\x83\x83\xffQQ\xffQQ\xff\x1e\x1e\xff\x00\x00\xf2\x00\x00\xae\x00\x00|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb1\xb1\xffoo\xffoo\xff@@\xff\x17\x17\xff\x17\x17\xff\x00\x00\xcd\x00\x00\xcd\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa5\xa5\xffoo\xff\x10\x10\xff\x00\x00\xe6\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\x1f\xff\xff\xf8\x0f\xff\xff\xf8\x0f\xff\xff\xf8\x0f\xff\xff\xe0\x03\xff\xff\xc0\x01\xff\xff\x80\x00\xff\xff\x80\x00\xff\xff\x80\x00\xff\xff\x80\x00\xff\xff\x80\x00\xff\xff\xc0\x01\xff\xff\xe0\x03\xff\xff\xf0\x07\xff\xff\xfc\x1f\xff\xff\xff\xff\xff\xff'

def GetMondrianBitmap():
	return wx.BitmapFromImage(GetMondrianImage())

def GetMondrianImage():
	stream = cStringIO.StringIO(GetMondrianData())
	return wx.ImageFromStream(stream)

def GetMondrianIcon():
	icon = wx.EmptyIcon()
	icon.CopyFromBitmap(GetMondrianBitmap())
	return icon

tz = TZ.TZ()
	
class PyAUIFrame(wx.Frame):
	def __init__(self, parent, id=-1, title="", pos=wx.DefaultPosition,
				 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE |
											wx.SUNKEN_BORDER |
											wx.CLIP_CHILDREN):

		wx.Frame.__init__(self, parent, id, title, pos, size, style)
		
		# tell FrameManager to manage this frame		
		self._mgr = PyAUI.FrameManager()
		self._mgr.SetFrame(self)
		
		self._perspectives = []
		self.n = 0
		self.x = 0
		self.file = ""
		
		self.SetIcon(GetMondrianIcon())
		
		# create menu
		mb = wx.MenuBar()

		file_menu = wx.Menu()
		file_menu.Append(ID_MenuNew, "新建(&N)")
		file_menu.Append(ID_MenuOpen, "打开(&O)")
		file_menu.Append(ID_MenuSave, "保存(&S)")
		file_menu.Append(ID_MenuSaveAs, "另存为(&V)")
		file_menu.Append(ID_MenuClear, "清空(&C)")
		file_menu.Append(ID_TZSize, "设置尺寸(&R)")
		file_menu.AppendSeparator()
		file_menu.Append(wx.ID_EXIT, "退出(&E)")

		view_menu = wx.Menu()
		view_menu.Append(ID_ListWords, "词汇表(&D)")
		view_menu.AppendSeparator()
		view_menu.Append(ID_FirstPerspective, "恢复初始面版(&D)")

		options_menu = wx.Menu()
		options_menu.AppendCheckItem(ID_AllowFloating, "允许浮动")
		options_menu.AppendCheckItem(ID_TransparentHint, "Transparent Hint")
		options_menu.AppendCheckItem(ID_TransparentHintFade, "Transparent Hint Fade-in")
		options_menu.AppendCheckItem(ID_TransparentDrag, "Transparent Drag")
		options_menu.AppendCheckItem(ID_AllowActivePane, "Allow Active Pane")
		options_menu.AppendSeparator()
		options_menu.AppendRadioItem(ID_NoGradient, "No Caption Gradient")
		options_menu.AppendRadioItem(ID_VerticalGradient, "Vertical Caption Gradient")
		options_menu.AppendRadioItem(ID_HorizontalGradient, "Horizontal Caption Gradient")
		#options_menu.AppendSeparator()
		#options_menu.Append(ID_Settings, "Settings Pane")

		help_menu = wx.Menu()
		help_menu.Append(ID_About, "About...")
		
		mb.Append(file_menu, "文件(&F)")
		mb.Append(view_menu, "查看(&V)")
		mb.Append(options_menu, "选项(&O)")
		mb.Append(help_menu, "帮助(&H)")
		
		self.SetMenuBar(mb)

		self.statusbar = self.CreateStatusBar(4, wx.ST_SIZEGRIP)
		self.statusbar.SetStatusWidths([-5, -2, -2, -4])
		self.statusbar.SetStatusText("Welcome To Sansi TZ!", 0)
		self.statusbar.SetStatusText("", 1)
		self.statusbar.SetStatusText("行：%d　　列：%d" % (tz.curY, tz.curX), 2)
		self.statusbar.SetStatusText("横向 %d 词，纵向 %d 词，共 %d 字" % (tz.countX, tz.countY, tz.countC), 3)

		# min size for the frame itself isn't completely done.
		# see the end up FrameManager::Update() for the test
		# code. For now, just hard code a frame minimum size
		self.SetMinSize(wx.Size(400, 300))

		# create some toolbars
		tb4 = wx.ToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
						 wx.TB_FLAT | wx.TB_NODIVIDER | wx.TB_HORZ_TEXT)
		tb4.SetToolBitmapSize(wx.Size(16,16))
		tb4_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_NEW, wx.ART_OTHER, wx.Size(16, 16))
		tb4.AddLabelTool(ID_FileNew, "新建", tb4_bmp1)
		tb4_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, wx.Size(16, 16))
		tb4.AddLabelTool(ID_FileOpen, "打开", tb4_bmp1)
		tb4_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_FILE_SAVE, wx.ART_OTHER, wx.Size(16, 16))
		tb4.AddLabelTool(ID_FileSave, "保存", tb4_bmp1)
		tb4_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_QUIT, wx.ART_OTHER, wx.Size(16, 16))
		tb4.AddLabelTool(ID_Quit, "退出", tb4_bmp1)
		tb4.AddSeparator()
		tb4_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_UNDO, wx.ART_OTHER, wx.Size(16, 16))
		tb4.AddLabelTool(ID_UnDo, "撤销", tb4_bmp1)
		tb4_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_REDO, wx.ART_OTHER, wx.Size(16, 16))
		tb4.AddLabelTool(ID_ReDo, "重做", tb4_bmp1)
		tb4_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_TICK_MARK, wx.ART_OTHER, wx.Size(16, 16))
		tb4.AddLabelTool(ID_Check, "检测", tb4_bmp1)
		tb4_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_CROSS_MARK, wx.ART_OTHER, wx.Size(16, 16))
		tb4.AddLabelTool(ID_Clear, "清空", tb4_bmp1)
		tb4.Realize()
		
		tb3 = wx.ToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
						 wx.TB_FLAT | wx.TB_NODIVIDER | wx.TB_HORZ_TEXT)
		tb3.SetToolBitmapSize(wx.Size(16,16))
		tb3_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_GO_BACK, wx.ART_OTHER, wx.Size(16, 16))
		tb3.AddLabelTool(ID_MoveLeft, "左移", tb3_bmp1)
		tb3_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_GO_DOWN, wx.ART_OTHER, wx.Size(16, 16))
		tb3.AddLabelTool(ID_MoveDown, "下移", tb3_bmp1)
		tb3_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_GO_UP, wx.ART_OTHER, wx.Size(16, 16))
		tb3.AddLabelTool(ID_MoveUp, "上移", tb3_bmp1)
		tb3_bmp1 = wx.ArtProvider_GetBitmap(wx.ART_GO_FORWARD, wx.ART_OTHER, wx.Size(16, 16))
		tb3.AddLabelTool(ID_MoveRight, "右移", tb3_bmp1)
		tb3.Realize()

		tb5 = wx.ToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
						 wx.TB_FLAT | wx.TB_NODIVIDER | wx.TB_VERTICAL)
		tb5.SetToolBitmapSize(wx.Size(48, 48))
		tb5.AddLabelTool(101, "Test", wx.ArtProvider_GetBitmap(wx.ART_ERROR)) 
		tb5.AddSeparator()
		tb5.AddLabelTool(102, "Test", wx.ArtProvider_GetBitmap(wx.ART_QUESTION))
		tb5.AddLabelTool(103, "Test", wx.ArtProvider_GetBitmap(wx.ART_INFORMATION))
		tb5.AddLabelTool(103, "Test", wx.ArtProvider_GetBitmap(wx.ART_WARNING))
		tb5.AddLabelTool(103, "Test", wx.ArtProvider_GetBitmap(wx.ART_MISSING_IMAGE))
		tb5.Realize()
		
		self._mgr.AddPane(self.CreateListBox(ID_ListX), PyAUI.PaneInfo().
						  Name("listX").Caption("横向词表").
						  Bottom().Layer(1).Position(1))
		
		self._mgr.AddPane(self.CreateListBox(ID_ListY), PyAUI.PaneInfo().
						  Name("listY").Caption("纵向词表").
						  Bottom().Layer(1).Position(1))
		
		self._mgr.AddPane(self.CreateHintGrid(ID_HintX), PyAUI.PaneInfo().
                          Name("hintX").Caption("横向提示").
                          Bottom().Layer(1).Position(1))
		
		self._mgr.AddPane(self.CreateHintGrid(ID_HintY), PyAUI.PaneInfo().
                          Name("hintY").Caption("纵向提示").
                          Bottom().Layer(1).Position(1))


		# create some center panes
		self._mgr.AddPane(self.CreateGrid(ID_GridContent, tz.size), PyAUI.PaneInfo().Name("grid_content").
						  CenterPane().Hide())

		# add the toolbars to the manager

		self._mgr.AddPane(tb4, PyAUI.PaneInfo().
						  Name("tb4").Caption("操作").
						  ToolbarPane().Top().Row(2).
						  LeftDockable(False).RightDockable(False))
		
		self._mgr.AddPane(tb3, PyAUI.PaneInfo().
						  Name("tb3").Caption("移动").
						  ToolbarPane().Top().Row(2).
						  LeftDockable(False).RightDockable(False))

		self._mgr.AddPane(tb5, PyAUI.PaneInfo().
						  Name("tbvert").Caption("垂直工具条").
						  ToolbarPane().Left().GripperTop().
						  TopDockable(False).BottomDockable(False))

		# make some default perspectives

		self._mgr.GetPane("tbvert").Hide()		
		all_panes = self._mgr.GetAllPanes()
		
		for ii in xrange(len(all_panes)):
			if not all_panes[ii].IsToolbar():
				all_panes[ii].Hide()

		self._mgr.GetPane("tb1").Hide()
		self._mgr.GetPane("tb5").Hide()
		self._mgr.GetPane("tbvert").Show()
		self._mgr.GetPane("grid_content").Show()
		self._mgr.GetPane("listX").Show().Left().Layer(0).Row(0).Position(0)
		self._mgr.GetPane("listY").Show().Left().Layer(0).Row(0).Position(0)
		self._mgr.GetPane("hintX").Show().Bottom().Layer(0).Row(0).Position(0)
		self._mgr.GetPane("hintY").Show().Bottom().Layer(0).Row(0).Position(0)

		self._mgr.Update()
		
		perspective_default = self._mgr.SavePerspective()
		self._perspectives.append(perspective_default)

		self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
		self.Bind(wx.EVT_SIZE, self.OnSize)
		self.Bind(wx.EVT_CLOSE, self.OnClose)

		# Show How To Use The Closing Panes Event
		
		self.Bind(wx.EVT_MENU, self.OnChangeTZSize, id=ID_TZSize)
		self.Bind(wx.EVT_MENU, self.OnCreateListBox, id=ID_CreateListBox)
		self.Bind(wx.EVT_MENU, self.OnCreateListBox, id=ID_ListWords)
		self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_AllowFloating)
		self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_TransparentHint)
		self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_TransparentHintFade)
		self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_TransparentDrag)
		self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_AllowActivePane)
		self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_NoGradient)
		self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_VerticalGradient)
		self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_HorizontalGradient)
		self.Bind(wx.EVT_MENU, self.OnClose, id=wx.ID_EXIT)
		self.Bind(wx.EVT_MENU, self.OnAbout, id=ID_About)
		self.Bind(wx.EVT_MENU_RANGE, self.OnRestorePerspective, id=ID_FirstPerspective,
                  id2=ID_FirstPerspective+1000)

		self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AllowFloating)
		self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentHint)
		self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentHintFade)
		self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentDrag)
		self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoGradient)
		self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VerticalGradient)
		self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_HorizontalGradient)
		
		self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListXDClick, id=ID_ListX)
		self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListYDClick, id=ID_ListY)
		self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.OnGridClick, id=ID_GridContent)
		self.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.OnCellChange, id=ID_GridContent)
		self.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.OnHintChange, id=ID_HintX)
		self.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.OnHintChange, id=ID_HintY)
		self.Bind(wx.EVT_MENU, self.OnUnDo, id=ID_UnDo)
		self.Bind(wx.EVT_MENU, self.OnReDo, id=ID_ReDo)
		self.Bind(wx.EVT_MENU, self.OnMoveUp, id=ID_MoveUp)
		self.Bind(wx.EVT_MENU, self.OnMoveRight, id=ID_MoveRight)
		self.Bind(wx.EVT_MENU, self.OnMoveDown, id=ID_MoveDown)
		self.Bind(wx.EVT_MENU, self.OnMoveLeft, id=ID_MoveLeft)
		self.Bind(wx.EVT_MENU, self.OnNew, id=ID_FileNew)
		self.Bind(wx.EVT_MENU, self.OnNew, id=ID_MenuNew)
		self.Bind(wx.EVT_MENU, self.OnFileOpen, id=ID_FileOpen)
		self.Bind(wx.EVT_MENU, self.OnFileOpen, id=ID_MenuOpen)
		self.Bind(wx.EVT_MENU, self.OnFileSave, id=ID_FileSave)
		self.Bind(wx.EVT_MENU, self.OnFileSave, id=ID_MenuSave)
		self.Bind(wx.EVT_MENU, self.OnFileSaveAs, id=ID_MenuSaveAs)
		self.Bind(wx.EVT_MENU, self.OnClear, id=ID_MenuClear)
		self.Bind(wx.EVT_MENU, self.OnClear, id=ID_Clear)
		self.Bind(wx.EVT_MENU, self.OnCheck, id=ID_Check)
		self.Bind(wx.EVT_MENU, self.OnClose, id=ID_Quit)
		self.Bind(wx.EVT_MENU, self.OnListShow, id=ID_ListWords)

		#初始化词库
		thread.start_new_thread(self.initDic, ())

	def initDic(self):
		self.statusbar.SetStatusText("正在初始化词库...", 1)
		tz.importDics()
		self.statusbar.SetStatusText("共有词条 %d" % tz.length, 1)
	
	def OnClear(self, event):
		tz.clear()
		self.gridUpdate()
	
	def OnListShow(self, event):
		if not wx.FindWindowById(ID_ListWords_Box):
			self.OnCreateListBox(event, ID_ListWords_Box, "词汇表")
		else:
			self._mgr.GetPane("list").Show().Left().Layer(0).Row(0).Position(0)
			self._mgr.Update()
		wx.FindWindowById(ID_ListWords_Box).Set(tz.dic)
	
	def OnCheck(self, event):
		notIn = tz.notInDic(tz.border)
		grid = wx.FindWindowById(ID_GridContent)
		for w in notIn:
			x = w[0][0]
			y = w[0][1]
			for i in range(len(w[1])):
				if w[0][2] == 0:
					grid.SetCellTextColour(y, x + i, wx.RED)
				else:
					grid.SetCellTextColour(y + i, x, wx.RED)
		if event != None:
			msg = "共有 %d 处不能组成词语！" % len(notIn)
			dlg = wx.MessageDialog(self, msg, "Sansi TZ", wx.OK | wx.ICON_INFORMATION)
			dlg.ShowModal()
			dlg.Destroy()
	
	def OnNew(self, event):
		if (tz.countC != 0 or self.file != "") and wx.MessageBox("是否要先保存正在编辑的文件？", 
				"文件保存提示", wx.YES_NO) == wx.YES:
			self.OnFileSaveAs(event)

		self.file = ""
		self.OnClear(event)
		self.SetTitle("Sansi-TZ - New*")
	
	def OnFileOpen(self, event):
		if self.file != "" and wx.MessageBox("是否要先保存正在编辑的文件？", 
				"文件保存提示", wx.YES_NO) == wx.YES:
			self.OnFileSaveAs(event)
		cwd = os.getcwd()
		if os.path.exists("save") == False:
			os.mkdir("save")
		os.chdir("save")
		dialog = wx.FileDialog(None, message = "打开", defaultDir = os.getcwd(), wildcard = "填字游戏文件 (*.xml)|*.xml|所有文件 (*.*)|*.*",  style = wx.OPEN)
		if dialog.ShowModal() == wx.ID_OK:
			self.file = dialog.GetPath()
			f = open(self.file)
			tz.loadXML(f.read())
			f.close()
		dialog.Destroy()
		self.gridUpdate()
		os.chdir(cwd)
		self.statusbar.SetStatusText("当前文件：%s" % self.file, 0)
		self.SetTitle("Sansi-TZ - %s" % self.file)
	
	def OnFileSave(self, event):
		if self.file == "":
			self.OnFileSaveAs(event)
		else:
			f = open(self.file, "w+")
			f.write(tz.toXML())
			f.close()
		self.statusbar.SetStatusText("文件已保存至：%s" % self.file, 0)
		self.SetTitle("Sansi-TZ - %s" % self.file)
	
	def OnFileSaveAs(self, event):
		cwd = os.getcwd()
		if os.path.exists("save") == False:
			os.mkdir("save")
		os.chdir("save")
		dialog = wx.FileDialog(None, message = "保存为", defaultDir = os.getcwd(), wildcard = "填字游戏文件 (*.xml)|*.xml|所有文件 (*.*)|*.*", style = wx.SAVE)
		if dialog.ShowModal() == wx.ID_OK:
			self.file = dialog.GetPath()
			f = open(self.file, "w+")
			f.write(tz.toXML())
			f.close()
		dialog.Destroy()
		os.chdir(cwd)
		self.statusbar.SetStatusText("文件已保存至：%s" % self.file, 0)
	
	def OnCellChange(self, event):
		tz.curX = event.GetCol()
		tz.curY = event.GetRow()
		w = wx.FindWindowById(ID_GridContent).GetCellValue(tz.curY, tz.curX)
		tz.addWord(tz.curX, tz.curY, 0, w)
		self.gridUpdate()
	
	def OnHintChange(self, event):
		gx = wx.FindWindowById(ID_HintX)
		gy = wx.FindWindowById(ID_HintY)
		for i in range(gx.GetNumberRows()):
			w = gx.GetCellValue(i, 0)
			h = gx.GetCellValue(i, 1)
			tz.updateHint(w, h)
		for i in range(gy.GetNumberRows()):
			w = gy.GetCellValue(i, 0)
			h = gy.GetCellValue(i, 1)
			tz.updateHint(w, h)
	
	def OnGridClick(self, event):
		tz.curX = event.GetCol()
		tz.curY = event.GetRow()
		self.statusbar.SetStatusText("当前位置：X: %d, Y: %d" % (tz.curX + 1, tz.curY + 1), 2)
		wx.FindWindowById(ID_GridContent).SetGridCursor(tz.curY, tz.curX)
		listX, listY = tz.list(tz.curX, tz.curY)
		wx.FindWindowById(ID_ListX).Set(listX)
		self._mgr.GetPane("listX").Caption("横向词表(%d)" % len(listX))
		wx.FindWindowById(ID_ListY).Set(listY)
		self._mgr.GetPane("listY").Caption("纵向词表(%d)" % len(listY))
		self._mgr.Update()

	def OnChangeTZSize(self, event):
		n = wx.GetNumberFromUser("请选择尺寸", "", "Sansi TZ", 10, min = 3, max = 20)
		grid = wx.FindWindowById(ID_GridContent)
		if n != -1 and tz.size != n:
			if tz.size < n:
				grid.AppendCols(n - tz.size)
				grid.AppendRows(n - tz.size)
			else:
				grid.DeleteCols(n, tz.size - n)
				grid.DeleteRows(n, tz.size - n)
			tz.size = n
			tz.updateSize()
			self.formatGrid()

	def OnUnDo(self, event):
		if tz.log(-1) == True:
			tz.count2()
			self.gridUpdate(-1)
		else:
			msg = "已经不能后退了！"
			dlg = wx.MessageDialog(self, msg, "Sansi TZ", wx.OK | wx.ICON_INFORMATION)
			dlg.ShowModal()
			dlg.Destroy()
	
	def OnReDo(self, event):
		if tz.log(1) == True:
			tz.count2()
			self.gridUpdate(-1)
		else:
			msg = "已经不能前进了！"
			dlg = wx.MessageDialog(self, msg, "Sansi TZ", wx.OK | wx.ICON_INFORMATION)
			dlg.ShowModal()
			dlg.Destroy()

	def OnMoveUp(self, event):
		tz.move(0, -1)
		self.gridUpdate()
	
	def OnMoveRight(self, event):
		tz.move(1, 0)
		self.gridUpdate()
	
	def OnMoveDown(self, event):
		tz.move(0, 1)
		self.gridUpdate()
	
	def OnMoveLeft(self, event):
		tz.move(-1, 0)
		self.gridUpdate()
	
	def hintUpdate(self):
		gx = wx.FindWindowById(ID_HintX)
		gy = wx.FindWindowById(ID_HintY)
		i = 0
		while gx.GetNumberRows():
			gx.DeleteRows(0, gx.GetNumberRows())
		for w in tz.listX:
			if gx.GetNumberRows() <= i:
				gx.AppendRows(1)
				gx.SetCellAlignment(i, 0, wx.ALIGN_LEFT, wx.ALIGN_CENTRE)
				gx.SetCellAlignment(i, 1, wx.ALIGN_LEFT, wx.ALIGN_CENTRE)
				gx.SetReadOnly(i, 0, True)
			w = tz.list2word(w[1])
			gx.SetCellValue(i, 0, w)
			if tz.hint.has_key(w):
				gx.SetCellValue(i, 1, tz.hint[w])
			else:
				tz.updateHint(w)
			i += 1
		i = 0
		while gy.GetNumberRows():
			gy.DeleteRows(0, gy.GetNumberRows())
		for w in tz.listY:
			if gy.GetNumberRows() <= i:
				gy.AppendRows(1)
				gy.SetCellAlignment(i, 0, wx.ALIGN_LEFT, wx.ALIGN_CENTRE)
				gy.SetCellAlignment(i, 1, wx.ALIGN_LEFT, wx.ALIGN_CENTRE)
				gy.SetReadOnly(i, 0, True)
			w = tz.list2word(w[1])
			gy.SetCellValue(i, 0, w)
			if tz.hint.has_key(w):
				gy.SetCellValue(i, 1, tz.hint[w])
			else:
				tz.updateHint(w)
			i += 1
	
	def gridUpdate(self, type = 1):
		grid = wx.FindWindowById(ID_GridContent)
		for y in range(tz.size):
			for x in range(tz.size):
				grid.SetCellValue(y, x, tz.border[y][x])
				grid.SetCellTextColour(y, x, wx.BLACK)
		#if type != -1:
		#	tz.log()	#如果不是redo或undo，则记录历史
		self.statusbar.SetStatusText("横向 %d 词，纵向 %d 词，共 %d 字" % (tz.countX, tz.countY, tz.countC), 3)
		self.OnCheck(None)
		self.hintUpdate()
	
	def OnListXDClick(self, event):
		w = event.GetString()
		tz.addWord(tz.curX, tz.curY, 0, w)
		self.gridUpdate()

	def OnListYDClick(self, event):
		w = event.GetString()
		tz.addWord(tz.curX, tz.curY, 1, w)
		self.gridUpdate()

	def OnClose(self, event):
		self._mgr.UnInit()
		self.Destroy()

		event.Skip()

	def OnAbout(self, event):
		msg = "三思填字制作程序(Ver 7.12.31)\n\n" + \
			  "作者： oldJ\n\n" + \
			  "有问题或反馈请发送邮件至以下地址：\n\n" + \
			  "oldj.wu@gmail.com\n\n" + \
			  "Based On Kirix C++ Implementation (wxAUI).\n\n" + \
			  ";-)"
			  
		dlg = wx.MessageDialog(self, msg, "Sansi TZ",
							   wx.OK | wx.ICON_INFORMATION)
		dlg.ShowModal()
		dlg.Destroy()


	def GetDockArt(self):
		return self._mgr.GetArtProvider()


	def DoUpdate(self):
		self._mgr.Update()


	def OnEraseBackground(self, event):
		event.Skip()


	def OnSize(self, event):
		event.Skip()


	def OnGradient(self, event):
		gradient = 0

		if event.GetId() == ID_NoGradient:
			gradient = PyAUI.AUI_GRADIENT_NONE
		elif event.GetId() == ID_VerticalGradient:
			gradient = PyAUI.AUI_GRADIENT_VERTICAL
		elif event.GetId() == ID_HorizontalGradient:
			gradient = PyAUI.AUI_GRADIENT_HORIZONTAL

		self._mgr.GetArtProvider().SetMetric(PyAUI.AUI_ART_GRADIENT_TYPE, gradient)
		self._mgr.Update()


	def OnManagerFlag(self, event):
		flag = 0
		
		if wx.Platform != "__WXMSW__":
			if event.GetId() == ID_TransparentDrag or \
			   event.GetId() == ID_TransparentHint or \
			   event.GetId() == ID_TransparentHintFade:
			
				wx.MessageBox("This option is presently only available on wxMSW")
				return

		if event.GetId() == ID_AllowFloating:
			flag = PyAUI.AUI_MGR_ALLOW_FLOATING

		elif event.GetId() == ID_TransparentDrag:
			flag = PyAUI.AUI_MGR_TRANSPARENT_DRAG

		elif event.GetId() == ID_TransparentHint:
			flag = PyAUI.AUI_MGR_TRANSPARENT_HINT

		elif event.GetId() == ID_TransparentHintFade:
			flag = PyAUI.AUI_MGR_TRANSPARENT_HINT_FADE

		elif event.GetId() == ID_AllowActivePane:
			flag = PyAUI.AUI_MGR_ALLOW_ACTIVE_PANE
			
		self._mgr.SetFlags(self._mgr.GetFlags() ^ flag)


	def OnUpdateUI(self, event):
		flags = self._mgr.GetFlags()

		if event.GetId() == ID_NoGradient:
			event.Check(((self._mgr.GetArtProvider().GetMetric(PyAUI.AUI_ART_GRADIENT_TYPE) == PyAUI.AUI_GRADIENT_NONE) and \
						[True] or [False])[0])

		elif event.GetId() == ID_VerticalGradient:
			event.Check(((self._mgr.GetArtProvider().GetMetric(PyAUI.AUI_ART_GRADIENT_TYPE) == PyAUI.AUI_GRADIENT_VERTICAL) and \
						[True] or [False])[0])

		elif event.GetId() == ID_HorizontalGradient:
			event.Check(((self._mgr.GetArtProvider().GetMetric(PyAUI.AUI_ART_GRADIENT_TYPE) == PyAUI.AUI_GRADIENT_HORIZONTAL) and \
						[True] or [False])[0])

		elif event.GetId() == ID_AllowFloating:
			event.Check(((flags & PyAUI.AUI_MGR_ALLOW_FLOATING) and [True] or [False])[0])

		elif event.GetId() == ID_TransparentDrag:
			event.Check(((flags & PyAUI.AUI_MGR_TRANSPARENT_DRAG) and [True] or [False])[0])

		elif event.GetId() == ID_TransparentHint:
			event.Check(((flags & PyAUI.AUI_MGR_TRANSPARENT_HINT) and [True] or [False])[0])

		elif event.GetId() == ID_TransparentHintFade:
			event.Check(((flags & PyAUI.AUI_MGR_TRANSPARENT_HINT_FADE) and [True] or [False])[0])


	def OnRestorePerspective(self, event):
		self._mgr.LoadPerspective(self._perspectives[0])


	def GetStartPosition(self):
		self.x = self.x + 20
		x = self.x
		pt = self.ClientToScreen(wx.Point(0, 0))
		
		return wx.Point(pt.x + x, pt.y + x)


	def OnCreateTree(self, event):
		self._mgr.AddPane(self.CreateTreeCtrl(), PyAUI.PaneInfo().
						  Name("Test").Caption("Tree Control").
						  Float().FloatingPosition(self.GetStartPosition()).
						  FloatingSize(wx.Size(150, 300)))
		self._mgr.Update()


	def OnCreateText(self, event):
		self._mgr.AddPane(self.CreateTextCtrl(), PyAUI.PaneInfo().
						  Name("text").Caption("文本").
						  Float().FloatingPosition(self.GetStartPosition()))
		self._mgr.Update()


	def OnCreateListBox(self, event, id = -1, caption = "列表"):
		self._mgr.AddPane(self.CreateListBox(id), PyAUI.PaneInfo().
						  Name("list").Caption(caption).
						  Float().FloatingPosition(self.GetStartPosition()))
		self._mgr.Update()


	def CreateTextCtrl(self, text = ""):
		return wx.TextCtrl(self,-1, text, wx.Point(0, 0), wx.Size(150, 90),
						   wx.NO_BORDER | wx.TE_MULTILINE)

	def formatGrid(self, gridSize = tz.size):
		editor = wx.grid.GridCellTextEditor()
		editor.SetParameters("1")
		grid = wx.FindWindowById(ID_GridContent)
		for y in range(gridSize):
			grid.SetColLabelValue(y, str(y + 1))
			#grid.SetColSize(y, 40)
			#grid.SetRowSize(y, 40)
			for x in range(gridSize):
				grid.SetCellAlignment(y, x, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
				grid.SetCellEditor(y, x, editor)
				#grid.SetCellValue(y, x, "")
				grid.SetCellFont(y, x, wx.Font(12, wx.NORMAL, wx.NORMAL, wx.NORMAL))
	
	def CreateGrid(self, id = -1, gridSize = tz.size):
		grid = wx.grid.Grid(self, id, wx.Point(0, 0), wx.Size(150, 250),
							wx.NO_BORDER | wx.WANTS_CHARS)
		
		grid.SetDefaultColSize(40, resizeExistingCols = True) 
		grid.SetDefaultRowSize(40, resizeExistingRows = True)
		grid.CreateGrid(gridSize, gridSize)
		grid.SetColMinimalAcceptableWidth(40)
		grid.SetRowMinimalAcceptableHeight(40)
		grid.SetRowLabelSize(30)
		grid.SetColLabelSize(25)
		grid.EnableDragColSize(enable = False)
		grid.EnableDragRowSize(enable = False)
		grid.EnableDragGridSize(enable = False)
		self.formatGrid()

		return grid

	def CreateHintGrid(self, id = -1):
		grid = wx.grid.Grid(self, id, wx.Point(0, 0), wx.Size(150, 250),
							wx.NO_BORDER | wx.WANTS_CHARS)
		
		grid.CreateGrid(0, 2)
		grid.SetColLabelValue(0, "词")
		grid.SetColLabelValue(1, "提示")
		grid.SetColSize(0, 100)
		grid.SetColSize(1, 180)
		grid.SetDefaultRowSize(25, resizeExistingRows = True)
		grid.SetRowMinimalAcceptableHeight(25)
		grid.SetRowLabelSize(30)
		grid.SetColLabelSize(25)
		return grid

	def CreateListBox(self, id = -1):
		listbox = wx.ListBox(self, id, wx.Point(0, 0), wx.Size(150, 250),
								choices=[], style = wx.NO_BORDER)
		return listbox


	def CreateTreeCtrl(self):
		tree = wx.TreeCtrl(self, -1, wx.Point(0, 0), wx.Size(160, 250),
						   wx.TR_DEFAULT_STYLE | wx.NO_BORDER)
		
		root = tree.AddRoot("PyAUI Project")
		items = []

		imglist = wx.ImageList(16, 16, True, 2)
		imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16,16)))
		imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16,16)))
		tree.AssignImageList(imglist)

		items.append(tree.AppendItem(root, "Item 1", 0))
		items.append(tree.AppendItem(root, "Item 2", 0))
		items.append(tree.AppendItem(root, "Item 3", 0))
		items.append(tree.AppendItem(root, "Item 4", 0))
		items.append(tree.AppendItem(root, "Item 5", 0))

		for ii in xrange(len(items)):
			id = items[ii]
			tree.AppendItem(id, "Subitem 1", 1)
			tree.AppendItem(id, "Subitem 2", 1)
			tree.AppendItem(id, "Subitem 3", 1)
			tree.AppendItem(id, "Subitem 4", 1)
			tree.AppendItem(id, "Subitem 5", 1)
		
		tree.Expand(root)

		return tree
	
def main():
	#显示窗口
	app = wx.PySimpleApp()
	frame = PyAUIFrame(None, wx.ID_ANY, "Sansi-TZ ;-)",
					   wx.DefaultPosition, wx.Size(750, 590))

	frame.CenterOnScreen()	
	app.SetTopWindow(frame)
	frame.Show()

	app.MainLoop()

if __name__ == "__main__":
	main()

