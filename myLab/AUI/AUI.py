import wx
import wx.html
import wx.grid

import os
import sys

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

sys.path.append(os.path.split(dirName)[0])

import aui

import random
import images

ArtIDs = [ "wx.ART_ADD_BOOKMARK",
           "wx.ART_DEL_BOOKMARK",
           "wx.ART_HELP_SIDE_PANEL",
           "wx.ART_HELP_SETTINGS",
           "wx.ART_HELP_BOOK",
           "wx.ART_HELP_FOLDER",
           "wx.ART_HELP_PAGE",
           "wx.ART_GO_BACK",
           "wx.ART_GO_FORWARD",
           "wx.ART_GO_UP",
           "wx.ART_GO_DOWN",
           "wx.ART_GO_TO_PARENT",
           "wx.ART_GO_HOME",
           "wx.ART_FILE_OPEN",
           "wx.ART_PRINT",
           "wx.ART_HELP",
           "wx.ART_TIP",
           "wx.ART_REPORT_VIEW",
           "wx.ART_LIST_VIEW",
           "wx.ART_NEW_DIR",
           "wx.ART_HARDDISK",
           "wx.ART_FLOPPY",
           "wx.ART_CDROM",
           "wx.ART_REMOVABLE",
           "wx.ART_FOLDER",
           "wx.ART_FOLDER_OPEN",
           "wx.ART_GO_DIR_UP",
           "wx.ART_EXECUTABLE_FILE",
           "wx.ART_NORMAL_FILE",
           "wx.ART_TICK_MARK",
           "wx.ART_CROSS_MARK",
           "wx.ART_ERROR",
           "wx.ART_QUESTION",
           "wx.ART_WARNING",
           "wx.ART_INFORMATION",
           "wx.ART_MISSING_IMAGE",
           ]

ID_CreateTree = wx.ID_HIGHEST + 1
ID_CreateGrid = ID_CreateTree + 1
ID_CreateText = ID_CreateTree + 2
ID_CreateHTML = ID_CreateTree + 3
ID_CreateNotebook = ID_CreateTree + 4
ID_CreateSizeReport = ID_CreateTree + 5
ID_GridContent = ID_CreateTree + 6
ID_TextContent = ID_CreateTree + 7
ID_TreeContent = ID_CreateTree + 8
ID_HTMLContent = ID_CreateTree + 9
ID_NotebookContent = ID_CreateTree + 10
ID_SizeReportContent = ID_CreateTree + 11
ID_CreatePerspective = ID_CreateTree + 12
ID_CopyPerspectiveCode = ID_CreateTree + 13
ID_AllowFloating = ID_CreateTree + 14
ID_AllowActivePane = ID_CreateTree + 15
ID_TransparentHint = ID_CreateTree + 16
ID_VenetianBlindsHint = ID_CreateTree + 17
ID_RectangleHint = ID_CreateTree + 18
ID_NoHint = ID_CreateTree + 19
ID_HintFade = ID_CreateTree + 20
ID_NoVenetianFade = ID_CreateTree + 21
ID_TransparentDrag = ID_CreateTree + 22
ID_NoGradient = ID_CreateTree + 23
ID_VerticalGradient = ID_CreateTree + 24
ID_HorizontalGradient = ID_CreateTree + 25
ID_LiveUpdate = ID_CreateTree + 26
ID_PaneIcons = ID_CreateTree + 27
ID_TransparentPane = ID_CreateTree + 28
ID_DefaultDockArt = ID_CreateTree + 29
ID_ModernDockArt = ID_CreateTree + 30
ID_SnapToScreen = ID_CreateTree + 31
ID_SnapPanes = ID_CreateTree + 32
ID_Settings = ID_CreateTree + 33
ID_CustomizeToolbar = ID_CreateTree + 34
ID_DropDownToolbarItem = ID_CreateTree + 35
ID_NotebookNoCloseButton = ID_CreateTree + 36
ID_NotebookCloseButton = ID_CreateTree + 37
ID_NotebookCloseButtonAll = ID_CreateTree + 38
ID_NotebookCloseButtonActive = ID_CreateTree + 39
ID_NotebookAllowTabMove = ID_CreateTree + 40
ID_NotebookAllowTabExternalMove = ID_CreateTree + 41
ID_NotebookAllowTabSplit = ID_CreateTree + 42
ID_NotebookWindowList = ID_CreateTree + 43
ID_NotebookScrollButtons = ID_CreateTree + 44
ID_NotebookTabFixedWidth = ID_CreateTree + 45
ID_NotebookArtGloss = ID_CreateTree + 46
ID_NotebookArtSimple = ID_CreateTree + 47
ID_NotebookArtVC71 = ID_CreateTree + 48
ID_NotebookArtFF2 = ID_CreateTree + 49
ID_NotebookArtVC8 = ID_CreateTree + 50
ID_NotebookArtChrome = ID_CreateTree + 51
ID_NotebookAlignTop = ID_CreateTree + 52
ID_NotebookAlignBottom = ID_CreateTree + 53
ID_NotebookHideSingle = ID_CreateTree + 54
ID_NotebookSmartTab = ID_CreateTree + 55
ID_NotebookUseImagesDropDown = ID_CreateTree + 56

ID_SampleItem = ID_CreateTree + 57

ID_FirstPerspective = ID_CreatePerspective + 1000

ID_PaneBorderSize = ID_SampleItem + 100
ID_SashSize = ID_PaneBorderSize + 2
ID_CaptionSize = ID_PaneBorderSize + 3
ID_BackgroundColor = ID_PaneBorderSize + 4
ID_SashColor = ID_PaneBorderSize + 5
ID_InactiveCaptionColor = ID_PaneBorderSize + 6
ID_InactiveCaptionGradientColor = ID_PaneBorderSize + 7
ID_InactiveCaptionTextColor = ID_PaneBorderSize + 8
ID_ActiveCaptionColor = ID_PaneBorderSize + 9
ID_ActiveCaptionGradientColor = ID_PaneBorderSize + 10
ID_ActiveCaptionTextColor = ID_PaneBorderSize + 11
ID_BorderColor = ID_PaneBorderSize + 12
ID_GripperColor = ID_PaneBorderSize + 13
ID_SashGrip = ID_PaneBorderSize + 14


# -- SizeReportCtrl --
# (a utility control that always reports it's client size)

class SizeReportCtrl(wx.PyControl):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                size=wx.DefaultSize, mgr=None):

        wx.PyControl.__init__(self, parent, id, pos, size, style=wx.NO_BORDER)
        self._mgr = mgr

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)


    def OnPaint(self, event):
    
        dc = wx.PaintDC(self)
        size = self.GetClientSize()

        s = "Size: %d x %d"%(size.x, size.y)

        dc.SetFont(wx.NORMAL_FONT)
        w, height = dc.GetTextExtent(s)
        height += 3
        dc.SetBrush(wx.WHITE_BRUSH)
        dc.SetPen(wx.WHITE_PEN)
        dc.DrawRectangle(0, 0, size.x, size.y)
        dc.SetPen(wx.LIGHT_GREY_PEN)
        dc.DrawLine(0, 0, size.x, size.y)
        dc.DrawLine(0, size.y, size.x, 0)
        dc.DrawText(s, (size.x-w)/2, (size.y-height*5)/2)

        if self._mgr:
        
            pi = self._mgr.GetPane(self)

            s = "Layer: %d"%pi.dock_layer
            w, h = dc.GetTextExtent(s)
            dc.DrawText(s, (size.x-w)/2, ((size.y-(height*5))/2)+(height*1))

            s = "Dock: %d Row: %d"%(pi.dock_direction, pi.dock_row)
            w, h = dc.GetTextExtent(s)
            dc.DrawText(s, (size.x-w)/2, ((size.y-(height*5))/2)+(height*2))

            s = "Position: %d"%pi.dock_pos
            w, h = dc.GetTextExtent(s)
            dc.DrawText(s, (size.x-w)/2, ((size.y-(height*5))/2)+(height*3))

            s = "Proportion: %d"%pi.dock_proportion
            w, h = dc.GetTextExtent(s)
            dc.DrawText(s, (size.x-w)/2, ((size.y-(height*5))/2)+(height*4))

        
    def OnEraseBackground(self, event):

        pass
    

    def OnSize(self, event):
    
        self.Refresh()
    

class SettingsPanel(wx.Panel):

    def __init__(self, parent, frame):

        wx.Panel.__init__(self, parent)
        self._frame = frame
    
        s1 = wx.BoxSizer(wx.HORIZONTAL)
        self._border_size = wx.SpinCtrl(self, ID_PaneBorderSize, "%d"%frame.GetDockArt().GetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE),
                                        wx.DefaultPosition, wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100,
                                        frame.GetDockArt().GetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE))
        s1.Add((1, 1), 1, wx.EXPAND)
        s1.Add(wx.StaticText(self, -1, "Pane Border Size:"))
        s1.Add(self._border_size)
        s1.Add((1, 1), 1, wx.EXPAND)
        s1.SetItemMinSize(1, (180, 20))

        s2 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_size = wx.SpinCtrl(self, ID_SashSize, "%d"%frame.GetDockArt().GetMetric(aui.AUI_DOCKART_SASH_SIZE), wx.DefaultPosition,
                                      wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100, frame.GetDockArt().GetMetric(aui.AUI_DOCKART_SASH_SIZE))
        s2.Add((1, 1), 1, wx.EXPAND)
        s2.Add(wx.StaticText(self, -1, "Sash Size:"))
        s2.Add(self._sash_size)
        s2.Add((1, 1), 1, wx.EXPAND)
        s2.SetItemMinSize(1, (180, 20))

        s3 = wx.BoxSizer(wx.HORIZONTAL)
        self._caption_size = wx.SpinCtrl(self, ID_CaptionSize, "%d"%frame.GetDockArt().GetMetric(aui.AUI_DOCKART_CAPTION_SIZE),
                                         wx.DefaultPosition, wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100, frame.GetDockArt().GetMetric(aui.AUI_DOCKART_CAPTION_SIZE))
        s3.Add((1, 1), 1, wx.EXPAND)
        s3.Add(wx.StaticText(self, -1, "Caption Size:"))
        s3.Add(self._caption_size)
        s3.Add((1, 1), 1, wx.EXPAND)
        s3.SetItemMinSize(1, (180, 20))

        b = self.CreateColorBitmap(wx.BLACK)

        s4 = wx.BoxSizer(wx.HORIZONTAL)
        self._background_color = wx.BitmapButton(self, ID_BackgroundColor, b, wx.DefaultPosition, wx.Size(50, 25))
        s4.Add((1, 1), 1, wx.EXPAND)
        s4.Add(wx.StaticText(self, -1, "Background Color:"))
        s4.Add(self._background_color)
        s4.Add((1, 1), 1, wx.EXPAND)
        s4.SetItemMinSize(1, (180, 20))

        s5 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_color = wx.BitmapButton(self, ID_SashColor, b, wx.DefaultPosition, wx.Size(50, 25))
        s5.Add((1, 1), 1, wx.EXPAND)
        s5.Add(wx.StaticText(self, -1, "Sash Color:"))
        s5.Add(self._sash_color)
        s5.Add((1, 1), 1, wx.EXPAND)
        s5.SetItemMinSize(1, (180, 20))

        s6 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_color = wx.BitmapButton(self, ID_InactiveCaptionColor, b, wx.DefaultPosition, wx.Size(50, 25))
        s6.Add((1, 1), 1, wx.EXPAND)
        s6.Add(wx.StaticText(self, -1, "Normal Caption:"))
        s6.Add(self._inactive_caption_color)
        s6.Add((1, 1), 1, wx.EXPAND)
        s6.SetItemMinSize(1, (180, 20))

        s7 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_gradient_color = wx.BitmapButton(self, ID_InactiveCaptionGradientColor, b, wx.DefaultPosition, wx.Size(50, 25))
        s7.Add((1, 1), 1, wx.EXPAND)
        s7.Add(wx.StaticText(self, -1, "Normal Caption Gradient:"))
        s7.Add(self._inactive_caption_gradient_color)
        s7.Add((1, 1), 1, wx.EXPAND)
        s7.SetItemMinSize(1, (180, 20))

        s8 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_text_color = wx.BitmapButton(self, ID_InactiveCaptionTextColor, b, wx.DefaultPosition, wx.Size(50, 25))
        s8.Add((1, 1), 1, wx.EXPAND)
        s8.Add(wx.StaticText(self, -1, "Normal Caption Text:"))
        s8.Add(self._inactive_caption_text_color)
        s8.Add((1, 1), 1, wx.EXPAND)
        s8.SetItemMinSize(1, (180, 20))

        s9 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_color = wx.BitmapButton(self, ID_ActiveCaptionColor, b, wx.DefaultPosition, wx.Size(50, 25))
        s9.Add((1, 1), 1, wx.EXPAND)
        s9.Add(wx.StaticText(self, -1, "Active Caption:"))
        s9.Add(self._active_caption_color)
        s9.Add((1, 1), 1, wx.EXPAND)
        s9.SetItemMinSize(1, (180, 20))

        s10 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_gradient_color = wx.BitmapButton(self, ID_ActiveCaptionGradientColor, b, wx.DefaultPosition, wx.Size(50, 25))
        s10.Add((1, 1), 1, wx.EXPAND)
        s10.Add(wx.StaticText(self, -1, "Active Caption Gradient:"))
        s10.Add(self._active_caption_gradient_color)
        s10.Add((1, 1), 1, wx.EXPAND)
        s10.SetItemMinSize(1, (180, 20))

        s11 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_text_color = wx.BitmapButton(self, ID_ActiveCaptionTextColor, b, wx.DefaultPosition, wx.Size(50, 25))
        s11.Add((1, 1), 1, wx.EXPAND)
        s11.Add(wx.StaticText(self, -1, "Active Caption Text:"))
        s11.Add(self._active_caption_text_color)
        s11.Add((1, 1), 1, wx.EXPAND)
        s11.SetItemMinSize(1, (180, 20))

        s12 = wx.BoxSizer(wx.HORIZONTAL)
        self._border_color = wx.BitmapButton(self, ID_BorderColor, b, wx.DefaultPosition, wx.Size(50, 25))
        s12.Add((1, 1), 1, wx.EXPAND)
        s12.Add(wx.StaticText(self, -1, "Border Color:"))
        s12.Add(self._border_color)
        s12.Add((1, 1), 1, wx.EXPAND)
        s12.SetItemMinSize(1, (180, 20))

        s13 = wx.BoxSizer(wx.HORIZONTAL)
        self._gripper_color = wx.BitmapButton(self, ID_GripperColor, b, wx.DefaultPosition, wx.Size(50,25))
        s13.Add((1, 1), 1, wx.EXPAND)
        s13.Add(wx.StaticText(self, -1, "Gripper Color:"))
        s13.Add(self._gripper_color)
        s13.Add((1, 1), 1, wx.EXPAND)
        s13.SetItemMinSize(1, (180, 20))
        
        s14 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_grip = wx.CheckBox(self, ID_SashGrip, "", wx.DefaultPosition, wx.Size(50,20))
        s14.Add((1, 1), 1, wx.EXPAND)
        s14.Add(wx.StaticText(self, -1, "Draw Sash Grip:"))
        s14.Add(self._sash_grip)
        s14.Add((1, 1), 1, wx.EXPAND)
        s14.SetItemMinSize(1, (180, 20))

        grid_sizer = wx.GridSizer(0, 2)
        grid_sizer.SetHGap(5)
        grid_sizer.Add(s1)
        grid_sizer.Add(s4)
        grid_sizer.Add(s2)
        grid_sizer.Add(s5)
        grid_sizer.Add(s3)
        grid_sizer.Add(s13)
        grid_sizer.Add(s14)
        grid_sizer.Add((1, 1))
        grid_sizer.Add(s12)
        grid_sizer.Add(s6)
        grid_sizer.Add(s9)
        grid_sizer.Add(s7)
        grid_sizer.Add(s10)
        grid_sizer.Add(s8)
        grid_sizer.Add(s11)

        cont_sizer = wx.BoxSizer(wx.VERTICAL)
        cont_sizer.Add(grid_sizer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(cont_sizer)
        self.GetSizer().SetSizeHints(self)

        self._border_size.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE))
        self._sash_size.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_SASH_SIZE))
        self._caption_size.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_CAPTION_SIZE))
        self._sash_grip.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_DRAW_SASH_GRIP))

        self.UpdateColors()

        self.Bind(wx.EVT_SPINCTRL, self.OnPaneBorderSize, id=ID_PaneBorderSize)
        self.Bind(wx.EVT_SPINCTRL, self.OnSashSize, id=ID_SashSize)
        self.Bind(wx.EVT_SPINCTRL, self.OnCaptionSize, id=ID_CaptionSize)
        self.Bind(wx.EVT_CHECKBOX, self.OnDrawSashGrip, id=ID_SashGrip)
        self.Bind(wx.EVT_BUTTON, self.OnSetColor, id=ID_BackgroundColor)
        self.Bind(wx.EVT_BUTTON, self.OnSetColor, id=ID_SashColor)
        self.Bind(wx.EVT_BUTTON, self.OnSetColor, id=ID_InactiveCaptionColor)
        self.Bind(wx.EVT_BUTTON, self.OnSetColor, id=ID_InactiveCaptionGradientColor)
        self.Bind(wx.EVT_BUTTON, self.OnSetColor, id=ID_InactiveCaptionTextColor)
        self.Bind(wx.EVT_BUTTON, self.OnSetColor, id=ID_ActiveCaptionColor)
        self.Bind(wx.EVT_BUTTON, self.OnSetColor, id=ID_ActiveCaptionGradientColor)
        self.Bind(wx.EVT_BUTTON, self.OnSetColor, id=ID_ActiveCaptionTextColor)
        self.Bind(wx.EVT_BUTTON, self.OnSetColor, id=ID_BorderColor)
        self.Bind(wx.EVT_BUTTON, self.OnSetColor, id=ID_GripperColor)
        

    def CreateColorBitmap(self, c):
    
        image = wx.EmptyImage(25, 14)
        for x in xrange(25):
            for y in xrange(14):
                pixcol = c
                if x == 0 or x == 24 or y == 0 or y == 13:
                    pixcol = wx.BLACK
                    
                image.SetRGB(x, y, pixcol.Red(), pixcol.Green(), pixcol.Blue())
            
        return image.ConvertToBitmap()
    

    def UpdateColors(self):
    
        bk = self._frame.GetDockArt().GetColor(aui.AUI_DOCKART_BACKGROUND_COLOUR)
        self._background_color.SetBitmapLabel(self.CreateColorBitmap(bk))

        cap = self._frame.GetDockArt().GetColor(aui.AUI_DOCKART_INACTIVE_CAPTION_COLOUR)
        self._inactive_caption_color.SetBitmapLabel(self.CreateColorBitmap(cap))

        capgrad = self._frame.GetDockArt().GetColor(aui.AUI_DOCKART_INACTIVE_CAPTION_GRADIENT_COLOUR)
        self._inactive_caption_gradient_color.SetBitmapLabel(self.CreateColorBitmap(capgrad))

        captxt = self._frame.GetDockArt().GetColor(aui.AUI_DOCKART_INACTIVE_CAPTION_TEXT_COLOUR)
        self._inactive_caption_text_color.SetBitmapLabel(self.CreateColorBitmap(captxt))

        acap = self._frame.GetDockArt().GetColor(aui.AUI_DOCKART_ACTIVE_CAPTION_COLOUR)
        self._active_caption_color.SetBitmapLabel(self.CreateColorBitmap(acap))

        acapgrad = self._frame.GetDockArt().GetColor(aui.AUI_DOCKART_ACTIVE_CAPTION_GRADIENT_COLOUR)
        self._active_caption_gradient_color.SetBitmapLabel(self.CreateColorBitmap(acapgrad))

        acaptxt = self._frame.GetDockArt().GetColor(aui.AUI_DOCKART_ACTIVE_CAPTION_TEXT_COLOUR)
        self._active_caption_text_color.SetBitmapLabel(self.CreateColorBitmap(acaptxt))

        sash = self._frame.GetDockArt().GetColor(aui.AUI_DOCKART_SASH_COLOUR)
        self._sash_color.SetBitmapLabel(self.CreateColorBitmap(sash))

        border = self._frame.GetDockArt().GetColor(aui.AUI_DOCKART_BORDER_COLOUR)
        self._border_color.SetBitmapLabel(self.CreateColorBitmap(border))

        gripper = self._frame.GetDockArt().GetColor(aui.AUI_DOCKART_GRIPPER_COLOUR)
        self._gripper_color.SetBitmapLabel(self.CreateColorBitmap(gripper))
    

    def OnPaneBorderSize(self, event):
    
        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE,
                                           event.GetInt())
        self._frame.DoUpdate()
    

    def OnSashSize(self, event):
    
        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_SASH_SIZE,
                                           event.GetInt())
        self._frame.DoUpdate()
    

    def OnCaptionSize(self, event):
    
        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_CAPTION_SIZE,
                                           event.GetInt())
        self._frame.DoUpdate()
    

    def OnDrawSashGrip(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_DRAW_SASH_GRIP,
                                           event.GetInt())
        self._frame.DoUpdate()

        
    def OnSetColor(self, event):
    
        dlg = wx.ColourDialog(self._frame)
        dlg.SetTitle("Color Picker")
        
        if dlg.ShowModal() != wx.ID_OK:
            return

        evId = event.GetId()
        if evId == ID_BackgroundColor:
            var = aui.AUI_DOCKART_BACKGROUND_COLOUR
        elif evId == ID_SashColor:
            var = aui.AUI_DOCKART_SASH_COLOUR 
        elif evId == ID_InactiveCaptionColor:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_COLOUR 
        elif evId == ID_InactiveCaptionGradientColor:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_GRADIENT_COLOUR 
        elif evId == ID_InactiveCaptionTextColor:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_TEXT_COLOUR 
        elif evId == ID_ActiveCaptionColor:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_COLOUR 
        elif evId == ID_ActiveCaptionGradientColor:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_GRADIENT_COLOUR 
        elif evId == ID_ActiveCaptionTextColor:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_TEXT_COLOUR 
        elif evId == ID_BorderColor:
            var = aui.AUI_DOCKART_BORDER_COLOUR 
        elif evId == ID_GripperColor:
            var = aui.AUI_DOCKART_GRIPPER_COLOUR
        else:
            return
        
        self._frame.GetDockArt().SetColor(var, dlg.GetColourData().GetColour())
        self._frame.DoUpdate()
        self.UpdateColors()
    

class AuiFrame(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title="", pos= wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE|wx.SUNKEN_BORDER):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        self._mgr = aui.AuiManager()
        
        # tell AuiManager to manage self frame
        self._mgr.SetManagedWindow(self)

        # set frame icon
        self.SetIcon(images.Mondrian.GetIcon())

        # set up default notebook style
        self._notebook_style = aui.AUI_NB_DEFAULT_STYLE | aui.AUI_NB_TAB_EXTERNAL_MOVE | wx.NO_BORDER
        self._notebook_theme = 0
        self._textCount = 1
        self._transparency = 255
        self._snapped = False

        self.CreateStatusBar()
        self.GetStatusBar().SetStatusText("Ready")

        self.CreateMenuBar()
        self.BuildPanes()
        self.BindEvents()


    def CreateMenuBar(self):
        
        # create menu
        mb = wx.MenuBar()

        file_menu = wx.Menu()
        file_menu.Append(wx.ID_EXIT, "Exit")

        view_menu = wx.Menu()
        view_menu.Append(ID_CreateText, "Create Text Control")
        view_menu.Append(ID_CreateHTML, "Create HTML Control")
        view_menu.Append(ID_CreateTree, "Create Tree")
        view_menu.Append(ID_CreateGrid, "Create Grid")
        view_menu.Append(ID_CreateNotebook, "Create Notebook")
        view_menu.Append(ID_CreateSizeReport, "Create Size Reporter")
        view_menu.AppendSeparator()
        view_menu.Append(ID_GridContent, "Use a Grid for the Content Pane")
        view_menu.Append(ID_TextContent, "Use a Text Control for the Content Pane")
        view_menu.Append(ID_HTMLContent, "Use an HTML Control for the Content Pane")
        view_menu.Append(ID_TreeContent, "Use a Tree Control for the Content Pane")
        view_menu.Append(ID_NotebookContent, "Use a AuiNotebook control for the Content Pane")
        view_menu.Append(ID_SizeReportContent, "Use a Size Reporter for the Content Pane")

        options_menu = wx.Menu()
        options_menu.AppendRadioItem(ID_TransparentHint, "Transparent Hint")
        options_menu.AppendRadioItem(ID_VenetianBlindsHint, "Venetian Blinds Hint")
        options_menu.AppendRadioItem(ID_RectangleHint, "Rectangle Hint")
        options_menu.AppendRadioItem(ID_NoHint, "No Hint")
        options_menu.AppendSeparator()
        options_menu.AppendCheckItem(ID_HintFade, "Hint Fade-in")
        options_menu.AppendCheckItem(ID_AllowFloating, "Allow Floating")
        options_menu.AppendCheckItem(ID_NoVenetianFade, "Disable Venetian Blinds Hint Fade-in")
        options_menu.AppendCheckItem(ID_TransparentDrag, "Transparent Drag")
        options_menu.AppendCheckItem(ID_AllowActivePane, "Allow Active Pane")
        options_menu.AppendCheckItem(ID_LiveUpdate, "Live Resize Update")
        options_menu.AppendCheckItem(ID_PaneIcons, "Set Icons On Panes")
        options_menu.AppendSeparator()
        options_menu.Append(ID_TransparentPane, "Set Floating Panes Transparency")
        options_menu.AppendSeparator()
        options_menu.AppendRadioItem(ID_DefaultDockArt, "Default DockArt")
        options_menu.AppendRadioItem(ID_ModernDockArt, "Modern Dock Art")
        options_menu.AppendSeparator()
        options_menu.Append(ID_SnapToScreen, "Snap To Screen")
        options_menu.AppendCheckItem(ID_SnapPanes, "Snap Panes To Managed Window")
        options_menu.AppendSeparator()
        options_menu.AppendRadioItem(ID_NoGradient, "No Caption Gradient")
        options_menu.AppendRadioItem(ID_VerticalGradient, "Vertical Caption Gradient")
        options_menu.AppendRadioItem(ID_HorizontalGradient, "Horizontal Caption Gradient")
        options_menu.AppendSeparator()
        options_menu.Append(ID_Settings, "Settings Pane")

        notebook_menu = wx.Menu()
        notebook_menu.AppendRadioItem(ID_NotebookArtGloss, "Glossy Theme (Default)")
        notebook_menu.AppendRadioItem(ID_NotebookArtSimple, "Simple Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtVC71, "VC71 Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtFF2, "Firefox 2 Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtVC8, "VC8 Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtChrome, "Chrome Theme")
        notebook_menu.AppendSeparator()        
        notebook_menu.AppendRadioItem(ID_NotebookNoCloseButton, "No Close Button")
        notebook_menu.AppendRadioItem(ID_NotebookCloseButton, "Close Button at Right")
        notebook_menu.AppendRadioItem(ID_NotebookCloseButtonAll, "Close Button on All Tabs")
        notebook_menu.AppendRadioItem(ID_NotebookCloseButtonActive, "Close Button on Active Tab")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendRadioItem(ID_NotebookAlignTop, "Tab Top Alignment")
        notebook_menu.AppendRadioItem(ID_NotebookAlignBottom, "Tab Bottom Alignment")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(ID_NotebookAllowTabMove, "Allow Tab Move")
        notebook_menu.AppendCheckItem(ID_NotebookAllowTabExternalMove, "Allow External Tab Move")
        notebook_menu.AppendCheckItem(ID_NotebookAllowTabSplit, "Allow Notebook Split")
        notebook_menu.AppendCheckItem(ID_NotebookScrollButtons, "Scroll Buttons Visible")
        notebook_menu.AppendCheckItem(ID_NotebookWindowList, "Window List Button Visible")
        notebook_menu.AppendCheckItem(ID_NotebookTabFixedWidth, "Fixed-width Tabs")
        notebook_menu.AppendCheckItem(ID_NotebookHideSingle, "Hide On Single Tab")
        notebook_menu.AppendCheckItem(ID_NotebookSmartTab, "Use Smart Tabbing")
        notebook_menu.AppendCheckItem(ID_NotebookUseImagesDropDown, "Use Tab Images In Dropdown Menu")

        self._perspectives_menu = wx.Menu()
        self._perspectives_menu.Append(ID_CreatePerspective, "Create Perspective")
        self._perspectives_menu.Append(ID_CopyPerspectiveCode, "Copy Perspective Data To Clipboard")
        self._perspectives_menu.AppendSeparator()
        self._perspectives_menu.Append(ID_FirstPerspective+0, "Default Startup")
        self._perspectives_menu.Append(ID_FirstPerspective+1, "All Panes")

        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, "About...")

        mb.Append(file_menu, "&File")
        mb.Append(view_menu, "&View")
        mb.Append(self._perspectives_menu, "&Perspectives")
        mb.Append(options_menu, "&Options")
        mb.Append(notebook_menu, "&Notebook")
        mb.Append(help_menu, "&Help")

        self.SetMenuBar(mb)


    def BuildPanes(self):
        
        # min size for the frame itself isn't completely done.
        # see the end up AuiManager.Update() for the test
        # code. For now, just hard code a frame minimum size
        self.SetMinSize(wx.Size(400, 300))

        # prepare a few custom overflow elements for the toolbars' overflow buttons

        prepend_items, append_items = [], []
        item = aui.AuiToolBarItem()
        
        item.SetKind(wx.ITEM_SEPARATOR)
        append_items.append(item)

        item = aui.AuiToolBarItem()        
        item.SetKind(wx.ITEM_NORMAL)
        item.SetId(ID_CustomizeToolbar)
        item.SetLabel("Customize...")
        append_items.append(item)


        # create some toolbars
        tb1 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                            aui.AUI_TB_DEFAULT_STYLE | aui.AUI_TB_OVERFLOW)
        tb1.SetToolBitmapSize(wx.Size(48, 48))
        tb1.AddSimpleTool(ID_SampleItem+1, "Test", wx.ArtProvider.GetBitmap(wx.ART_ERROR))
        tb1.AddSeparator()
        tb1.AddSimpleTool(ID_SampleItem+2, "Test", wx.ArtProvider.GetBitmap(wx.ART_QUESTION))
        tb1.AddSimpleTool(ID_SampleItem+3, "Test", wx.ArtProvider.GetBitmap(wx.ART_INFORMATION))
        tb1.AddSimpleTool(ID_SampleItem+4, "Test", wx.ArtProvider.GetBitmap(wx.ART_WARNING))
        tb1.AddSimpleTool(ID_SampleItem+5, "Test", wx.ArtProvider.GetBitmap(wx.ART_MISSING_IMAGE))
        tb1.SetCustomOverflowItems(prepend_items, append_items)
        tb1.Realize()

        tb2 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                            aui.AUI_TB_DEFAULT_STYLE | aui.AUI_TB_OVERFLOW)
        tb2.SetToolBitmapSize(wx.Size(16, 16))

        tb2_bmp1 = wx.ArtProvider.GetBitmap(wx.ART_QUESTION, wx.ART_OTHER, wx.Size(16, 16))
        tb2.AddSimpleTool(ID_SampleItem+6, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+7, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+8, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+9, "Test", tb2_bmp1)
        tb2.AddSeparator()
        tb2.AddSimpleTool(ID_SampleItem+10, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+11, "Test", tb2_bmp1)
        tb2.AddSeparator()
        tb2.AddSimpleTool(ID_SampleItem+12, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+13, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+14, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+15, "Test", tb2_bmp1)
        tb2.SetCustomOverflowItems(prepend_items, append_items)
        tb2.Realize()

        tb3 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                            aui.AUI_TB_DEFAULT_STYLE | aui.AUI_TB_OVERFLOW)
        tb3.SetToolBitmapSize(wx.Size(16, 16))
        tb3_bmp1 = wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16))
        tb3.AddSimpleTool(ID_SampleItem+16, "Check 1", tb3_bmp1, "Check 1", aui.ITEM_CHECK)
        tb3.AddSimpleTool(ID_SampleItem+17, "Check 2", tb3_bmp1, "Check 2", aui.ITEM_CHECK)
        tb3.AddSimpleTool(ID_SampleItem+18, "Check 3", tb3_bmp1, "Check 3", aui.ITEM_CHECK)
        tb3.AddSimpleTool(ID_SampleItem+19, "Check 4", tb3_bmp1, "Check 4", aui.ITEM_CHECK)
        tb3.AddSeparator()
        tb3.AddSimpleTool(ID_SampleItem+20, "Radio 1", tb3_bmp1, "Radio 1", aui.ITEM_RADIO)
        tb3.AddSimpleTool(ID_SampleItem+21, "Radio 2", tb3_bmp1, "Radio 2", aui.ITEM_RADIO)
        tb3.AddSimpleTool(ID_SampleItem+22, "Radio 3", tb3_bmp1, "Radio 3", aui.ITEM_RADIO)
        tb3.AddSeparator()
        tb3.AddSimpleTool(ID_SampleItem+23, "Radio 1 (Group 2)", tb3_bmp1, "Radio 1 (Group 2)", aui.ITEM_RADIO)
        tb3.AddSimpleTool(ID_SampleItem+24, "Radio 2 (Group 2)", tb3_bmp1, "Radio 2 (Group 2)", aui.ITEM_RADIO)
        tb3.AddSimpleTool(ID_SampleItem+25, "Radio 3 (Group 2)", tb3_bmp1, "Radio 3 (Group 2)", aui.ITEM_RADIO);

        tb3.SetCustomOverflowItems(prepend_items, append_items)
        tb3.Realize()

        tb4 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                            aui.AUI_TB_DEFAULT_STYLE | aui.AUI_TB_OVERFLOW |
                            aui.AUI_TB_TEXT | aui.AUI_TB_HORZ_TEXT)
        tb4.SetToolBitmapSize(wx.Size(16, 16))
        tb4_bmp1 = wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16))
        tb4.AddSimpleTool(ID_DropDownToolbarItem, "Item 1", tb4_bmp1)
        tb4.AddSimpleTool(ID_SampleItem+23, "Item 2", tb4_bmp1)
        tb4.AddSimpleTool(ID_SampleItem+24, "Item 3", tb4_bmp1)
        tb4.AddSimpleTool(ID_SampleItem+25, "Item 4", tb4_bmp1)
        tb4.AddSeparator()
        tb4.AddSimpleTool(ID_SampleItem+26, "Item 5", tb4_bmp1)
        tb4.AddSimpleTool(ID_SampleItem+27, "Item 6", tb4_bmp1)
        tb4.AddSimpleTool(ID_SampleItem+28, "Item 7", tb4_bmp1)
        tb4.AddSimpleTool(ID_SampleItem+29, "Item 8", tb4_bmp1)
        tb4.SetToolDropDown(ID_DropDownToolbarItem, True)
        tb4.SetCustomOverflowItems(prepend_items, append_items)
        tb4.Realize()

        tb5 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                            aui.AUI_TB_DEFAULT_STYLE | aui.AUI_TB_OVERFLOW | aui.AUI_TB_VERTICAL)
        tb5.SetToolBitmapSize(wx.Size(48, 48))
        tb5.AddSimpleTool(ID_SampleItem+30, "Test", wx.ArtProvider.GetBitmap(wx.ART_ERROR))
        tb5.AddSeparator()
        tb5.AddSimpleTool(ID_SampleItem+31, "Test", wx.ArtProvider.GetBitmap(wx.ART_QUESTION))
        tb5.AddSimpleTool(ID_SampleItem+32, "Test", wx.ArtProvider.GetBitmap(wx.ART_INFORMATION))
        tb5.AddSimpleTool(ID_SampleItem+33, "Test", wx.ArtProvider.GetBitmap(wx.ART_WARNING))
        tb5.AddSimpleTool(ID_SampleItem+34, "Test", wx.ArtProvider.GetBitmap(wx.ART_MISSING_IMAGE))
        tb5.SetCustomOverflowItems(prepend_items, append_items)
        tb5.Realize()

        # add a bunch of panes
        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test1").Caption("Pane Caption").Top())

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test2").Caption("Client Size Reporter").
                          Bottom().Position(1).CloseButton(True).MaximizeButton(True).
                          MinimizeButton(True))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test3").Caption("Client Size Reporter").
                          Bottom().CloseButton(True).MaximizeButton(True).MinimizeButton(True))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test4").Caption("Pane Caption").Left())

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test5").Caption("No Close Button").Right().CloseButton(False))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test6").Caption("Client Size Reporter").Right().Row(1).
                          CloseButton(True).MaximizeButton(True).MinimizeButton(True))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test7").Caption("Client Size Reporter").Left().Layer(1).
                          CloseButton(True).MaximizeButton(True).MinimizeButton(True))

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().Name("test8").Caption("Tree Pane").
                          Left().Layer(1).Position(1).CloseButton(True).MaximizeButton(True).
                          MinimizeButton(True).MinimizeButton(True))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test9").Caption("Min Size 200x100").
                          BestSize(wx.Size(200,100)).MinSize(wx.Size(200,100)).Bottom().Layer(1).
                          CloseButton(True).MaximizeButton(True).MinimizeButton(True))

        wnd10 = self.CreateTextCtrl("This pane will prompt the user before hiding.")
        self._mgr.AddPane(wnd10, aui.AuiPaneInfo().
                          Name("test10").Caption("Text Pane with Hide Prompt").
                          Bottom().Layer(1).Position(1).MinimizeButton(True))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test11").Caption("Fixed Pane").
                          Bottom().Layer(1).Position(2).Fixed().MinimizeButton(True))

        self._mgr.AddPane(SettingsPanel(self,self), aui.AuiPaneInfo().
                          Name("settings").Caption("Dock Manager Settings").
                          Dockable(False).Float().Hide().MinimizeButton(True))

        # create some center panes

        self._mgr.AddPane(self.CreateGrid(), aui.AuiPaneInfo().Name("grid_content").
                          CenterPane().Hide().MinimizeButton(True))

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().Name("tree_content").
                          CenterPane().Hide().MinimizeButton(True))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().Name("sizereport_content").
                          CenterPane().Hide().MinimizeButton(True))

        self._mgr.AddPane(self.CreateTextCtrl(), aui.AuiPaneInfo().Name("text_content").
                          CenterPane().Hide().MinimizeButton(True))

        self._mgr.AddPane(self.CreateHTMLCtrl(), aui.AuiPaneInfo().Name("html_content").
                          CenterPane().Hide().MinimizeButton(True))

        self._mgr.AddPane(self.CreateNotebook(), aui.AuiPaneInfo().Name("notebook_content").
                          CenterPane().PaneBorder(False))

        # add the toolbars to the manager
        self._mgr.AddPane(tb1, aui.AuiPaneInfo().Name("tb1").Caption("Big Toolbar").
                          ToolbarPane().Top())

        self._mgr.AddPane(tb2, aui.AuiPaneInfo().Name("tb2").Caption("Toolbar 2").
                          ToolbarPane().Top().Row(1))

        self._mgr.AddPane(tb3, aui.AuiPaneInfo().Name("tb3").Caption("Toolbar 3").
                          ToolbarPane().Top().Row(1).Position(1))

        self._mgr.AddPane(tb4, aui.AuiPaneInfo().Name("tb4").Caption("Sample Bookmark Toolbar").
                          ToolbarPane().Top().Row(2))

        self._mgr.AddPane(tb5, aui.AuiPaneInfo().Name("tb5").Caption("Sample Vertical Toolbar").
                          ToolbarPane().Left().GripperTop())

        self._mgr.AddPane(wx.Button(self, -1, "Test Button"),
                          aui.AuiPaneInfo().Name("tb6").ToolbarPane().Top().Row(2).Position(1))

        # make some default perspectives

        perspective_all = self._mgr.SavePerspective()

        all_panes = self._mgr.GetAllPanes()
        for pane in all_panes:
            if not pane.IsToolbar():
                pane.Hide()
                
        self._mgr.GetPane("tb1").Hide()
        self._mgr.GetPane("tb6").Hide()
        self._mgr.GetPane("test8").Show().Left().Layer(0).Row(0).Position(0)
        self._mgr.GetPane("test10").Show().Bottom().Layer(0).Row(0).Position(0)
        self._mgr.GetPane("notebook_content").Show()
        perspective_default = self._mgr.SavePerspective()

        self._perspectives = []
        self._perspectives.append(perspective_default)
        self._perspectives.append(perspective_all)

        self._mgr.LoadPerspective(perspective_default)
    
        # "commit" all changes made to AuiManager
        self._mgr.Update()


    def BindEvents(self):

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_MENU, self.OnCreateTree, id=ID_CreateTree)
        self.Bind(wx.EVT_MENU, self.OnCreateGrid, id=ID_CreateGrid)
        self.Bind(wx.EVT_MENU, self.OnCreateText, id=ID_CreateText)
        self.Bind(wx.EVT_MENU, self.OnCreateHTML, id=ID_CreateHTML)
        self.Bind(wx.EVT_MENU, self.OnCreateSizeReport, id=ID_CreateSizeReport)
        self.Bind(wx.EVT_MENU, self.OnCreateNotebook, id=ID_CreateNotebook)
        self.Bind(wx.EVT_MENU, self.OnCreatePerspective, id=ID_CreatePerspective)
        self.Bind(wx.EVT_MENU, self.OnCopyPerspectiveCode, id=ID_CopyPerspectiveCode)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_AllowFloating)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_TransparentHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_VenetianBlindsHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_RectangleHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_NoHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_HintFade)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_NoVenetianFade)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_TransparentDrag)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_LiveUpdate)
        self.Bind(wx.EVT_MENU, self.OnSetIconsOnPanes, id=ID_PaneIcons)
        self.Bind(wx.EVT_MENU, self.OnTransparentPane, id=ID_TransparentPane)
        self.Bind(wx.EVT_MENU, self.OnDockArt, id=ID_DefaultDockArt)
        self.Bind(wx.EVT_MENU, self.OnDockArt, id=ID_ModernDockArt)
        self.Bind(wx.EVT_MENU, self.OnSnapToScreen, id=ID_SnapToScreen)
        self.Bind(wx.EVT_MENU, self.OnSnapPanes, id=ID_SnapPanes)        
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_AllowActivePane)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookTabFixedWidth)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookNoCloseButton)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseButton)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseButtonAll)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseButtonActive)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookAllowTabMove)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookAllowTabExternalMove)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookAllowTabSplit)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookScrollButtons)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookWindowList)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtGloss)                  
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtSimple)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtVC71)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtFF2)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtVC8)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtChrome)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookHideSingle)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookSmartTab)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookUseImagesDropDown)
        self.Bind(wx.EVT_MENU, self.OnTabAlignment, id=ID_NotebookAlignTop)
        self.Bind(wx.EVT_MENU, self.OnTabAlignment, id=ID_NotebookAlignBottom)
        
        self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_NoGradient)
        self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_VerticalGradient)
        self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_HorizontalGradient)
        self.Bind(wx.EVT_MENU, self.OnSettings, id=ID_Settings)
        self.Bind(wx.EVT_MENU, self.OnCustomizeToolbar, id=ID_CustomizeToolbar)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_GridContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_TreeContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_TextContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_SizeReportContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_HTMLContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_NotebookContent)
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)

        self.Bind(wx.EVT_MENU_RANGE, self.OnRestorePerspective, id=ID_FirstPerspective,
                  id2=ID_FirstPerspective+1000)

        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AllowFloating)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_HintFade)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentDrag)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VerticalGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_HorizontalGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VenetianBlindsHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_RectangleHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoVenetianFade)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_LiveUpdate)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_DefaultDockArt)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_ModernDockArt)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_SnapPanes)
        
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookTabFixedWidth)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookNoCloseButton)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCloseButton)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCloseButtonAll)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCloseButtonActive)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookAllowTabMove)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookAllowTabExternalMove)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookAllowTabSplit)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookScrollButtons)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookWindowList)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookHideSingle)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookSmartTab)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookUseImagesDropDown)

        self.Bind(aui.EVT_AUITOOLBAR_TOOL_DROPDOWN, self.OnDropDownToolbarItem, id=ID_DropDownToolbarItem)
        self.Bind(aui.EVT_AUI_PANE_CLOSE, self.OnPaneClose)
        self.Bind(aui.EVT_AUINOTEBOOK_ALLOW_DND, self.OnAllowNotebookDnD)
        self.Bind(aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnNotebookPageClose)
        

    def GetDockArt(self):

        return self._mgr.GetArtProvider()


    def DoUpdate(self):

        self._mgr.Update()
        self.Refresh()


    def OnEraseBackground(self, event):

        event.Skip()


    def OnSize(self, event):

        event.Skip()


    def OnSettings(self, event):

        # show the settings pane, and float it
        floating_pane = self._mgr.GetPane("settings").Float().Show()

        if floating_pane.floating_pos == wx.DefaultPosition:
            floating_pane.FloatingPosition(self.GetStartPosition())

        self._mgr.Update()


    def OnSetIconsOnPanes(self, event):

        panes = self._mgr.GetAllPanes()
        checked = event.IsChecked()
        
        for pane in panes:
            if checked:
                randimage = random.randint(0, len(ArtIDs) - 1)
                bmp = wx.ArtProvider_GetBitmap(eval(ArtIDs[randimage]), wx.ART_OTHER, (16, 16))
            else:
                bmp = None
                
            pane.Icon(bmp)

        self.SendSizeEvent()
        self._mgr.Update()     


    def OnTransparentPane(self, event):

        dlg = wx.TextEntryDialog(self, "Enter a transparency value (0-255):", "Pane transparency")

        dlg.SetValue("%d"%self._transparency)
        if dlg.ShowModal() != wx.ID_OK:
            return

        transparency = int(dlg.GetValue())
        dlg.Destroy()
        try:
            transparency = int(transparency)
        except:
            dlg = wx.MessageDialog(self, 'Invalid transparency value. Transparency' \
                                   ' should be an integer between 0 and 255.',
                                   'Error',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        if transparency < 0 or transparency > 255:
            dlg = wx.MessageDialog(self, 'Invalid transparency value. Transparency' \
                                   ' should be an integer between 0 and 255.',
                                   'Error',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        self._transparency = transparency
        panes = self._mgr.GetAllPanes()
        for pane in panes:
            pane.Transparent(self._transparency)

        self._mgr.Update()
        

    def OnDockArt(self, event):

        if event.GetId() == ID_DefaultDockArt:
            self._mgr.SetArtProvider(aui.AuiDefaultDockArt())
        else:
            if self._mgr.CanUseModernDockArt():
                self._mgr.SetArtProvider(aui.ModernDockArt(self))

        self._mgr.Update()
        self.Refresh()


    def OnSnapToScreen(self, event):

        self._mgr.SnapToScreen(True, monitor=0, hAlign=wx.RIGHT, vAlign=wx.TOP)


    def OnSnapPanes(self, event):

        allPanes = self._mgr.GetAllPanes()
        
        if not self._snapped:
            self._captions = {}
            for pane in allPanes:
                self._captions[pane.name] = pane.caption
            
        toSnap = not self._snapped

        if toSnap:
            for pane in allPanes:
                if pane.IsToolbar() or isinstance(pane.window, aui.AuiNotebook):
                    continue

                snap = random.randint(0, 4)
                if snap == 0:
                    # Snap everywhere
                    pane.Caption(pane.caption + " (Snap Everywhere)")
                    pane.Snappable(True)
                elif snap == 1:
                    # Snap left
                    pane.Caption(pane.caption + " (Snap Left)")
                    pane.LeftSnappable(True)
                elif snap == 2:
                    # Snap right
                    pane.Caption(pane.caption + " (Snap Right)")
                    pane.RightSnappable(True)
                elif snap == 3:
                    # Snap top
                    pane.Caption(pane.caption + " (Snap Top)")
                    pane.TopSnappable(True)
                elif snap == 4:
                    # Snap bottom
                    pane.Caption(pane.caption + " (Snap Bottom)")
                    pane.BottomSnappable(True)
                    
        else:

            for pane in allPanes:
                if pane.IsToolbar() or isinstance(pane.window, aui.AuiNotebook):
                    continue

                pane.Caption(self._captions[pane.name])
                pane.Snappable(False)

        self._snapped = toSnap
        self._mgr.Update()
        self.Refresh()
        

    def OnCustomizeToolbar(self, event):

        wx.MessageBox("Customize Toolbar clicked")


    def OnGradient(self, event):

        evId = event.GetId()
        if evId == ID_NoGradient:
            gradient = aui.AUI_GRADIENT_NONE
        elif evId == ID_VerticalGradient:
            gradient = aui.AUI_GRADIENT_VERTICAL
        elif evId == ID_HorizontalGradient:
            gradient = aui.AUI_GRADIENT_HORIZONTAL 

        self._mgr.GetArtProvider().SetMetric(aui.AUI_DOCKART_GRADIENT_TYPE, gradient)
        self.SendSizeEvent()
        self._mgr.Update()


    def OnManagerFlag(self, event):

        flag = 0
        evId = event.GetId()

        if evId in [ID_TransparentHint, ID_VenetianBlindsHint, ID_RectangleHint, ID_NoHint]:
        
            flags = self._mgr.GetFlags()
            flags &= ~aui.AUI_MGR_TRANSPARENT_HINT
            flags &= ~aui.AUI_MGR_VENETIAN_BLINDS_HINT
            flags &= ~aui.AUI_MGR_RECTANGLE_HINT
            self._mgr.SetFlags(flags)
        
        if evId == ID_AllowFloating:
            flag = aui.AUI_MGR_ALLOW_FLOATING 
        elif evId == ID_TransparentDrag:
            flag = aui.AUI_MGR_TRANSPARENT_DRAG 
        elif evId == ID_HintFade:
            flag = aui.AUI_MGR_HINT_FADE 
        elif evId == ID_NoVenetianFade:
            flag = aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE 
        elif evId == ID_AllowActivePane:
            flag = aui.AUI_MGR_ALLOW_ACTIVE_PANE 
        elif evId == ID_TransparentHint:
            flag = aui.AUI_MGR_TRANSPARENT_HINT 
        elif evId == ID_VenetianBlindsHint:
            flag = aui.AUI_MGR_VENETIAN_BLINDS_HINT 
        elif evId == ID_RectangleHint:
            flag = aui.AUI_MGR_RECTANGLE_HINT 
        elif evId == ID_LiveUpdate:
            flag = aui.AUI_MGR_LIVE_RESIZE 
        
        if flag:
            self._mgr.SetFlags(self._mgr.GetFlags() ^ flag)
        
        self._mgr.Update()


    def OnNotebookFlag(self, event):

        evId = event.GetId()
        
        if evId in [ID_NotebookNoCloseButton, ID_NotebookCloseButton, ID_NotebookCloseButtonAll, \
                    ID_NotebookCloseButtonActive]:
        
            self._notebook_style &= ~(aui.AUI_NB_CLOSE_BUTTON |
                                      aui.AUI_NB_CLOSE_ON_ACTIVE_TAB |
                                      aui.AUI_NB_CLOSE_ON_ALL_TABS)

            if evId == ID_NotebookCloseButton:
                self._notebook_style ^= aui.AUI_NB_CLOSE_BUTTON 
            elif evId == ID_NotebookCloseButtonAll:
                self._notebook_style ^= aui.AUI_NB_CLOSE_ON_ALL_TABS 
            elif evId == ID_NotebookCloseButtonActive:
                self._notebook_style ^= aui.AUI_NB_CLOSE_ON_ACTIVE_TAB 

        if evId == ID_NotebookAllowTabMove:
            self._notebook_style ^= aui.AUI_NB_TAB_MOVE
        
        if evId == ID_NotebookAllowTabExternalMove:
            self._notebook_style ^= aui.AUI_NB_TAB_EXTERNAL_MOVE
        
        elif evId == ID_NotebookAllowTabSplit:
            self._notebook_style ^= aui.AUI_NB_TAB_SPLIT
        
        elif evId == ID_NotebookWindowList:
            self._notebook_style ^= aui.AUI_NB_WINDOWLIST_BUTTON
        
        elif evId == ID_NotebookScrollButtons:
            self._notebook_style ^= aui.AUI_NB_SCROLL_BUTTONS
        
        elif evId == ID_NotebookTabFixedWidth:
            self._notebook_style ^= aui.AUI_NB_TAB_FIXED_WIDTH

        elif evId == ID_NotebookHideSingle:
            self._notebook_style ^= aui.AUI_NB_HIDE_ON_SINGLE_TAB

        elif evId == ID_NotebookSmartTab:
            self._notebook_style ^= aui.AUI_NB_SMART_TABS

        elif evId == ID_NotebookUseImagesDropDown:
            self._notebook_style ^= aui.AUI_NB_USE_IMAGES_DROPDOWN
        
        all_panes = self._mgr.GetAllPanes()
        
        for pane in all_panes:

            if isinstance(pane.window, aui.AuiNotebook):            
                nb = pane.window

                if evId == ID_NotebookArtGloss:
                
                    nb.SetArtProvider(aui.AuiDefaultTabArt())
                    self._notebook_theme = 0
                
                elif evId == ID_NotebookArtSimple:
                    nb.SetArtProvider(aui.AuiSimpleTabArt())
                    self._notebook_theme = 1
                
                elif evId == ID_NotebookArtVC71:
                    nb.SetArtProvider(aui.VC71TabArt())
                    self._notebook_theme = 2
                    
                elif evId == ID_NotebookArtFF2:
                    nb.SetArtProvider(aui.FF2TabArt())
                    self._notebook_theme = 3

                elif evId == ID_NotebookArtVC8:
                    nb.SetArtProvider(aui.VC8TabArt())
                    self._notebook_theme = 4

                elif evId == ID_NotebookArtChrome:
                    nb.SetArtProvider(aui.ChromeTabArt())
                    self._notebook_theme = 5

                nb.SetWindowStyleFlag(self._notebook_style)
                nb.Refresh()
                nb.Update()
            

    def OnUpdateUI(self, event):

        flags = self._mgr.GetFlags()
        evId = event.GetId()

        if evId == ID_NoGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_NONE)
                
        elif evId == ID_VerticalGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_VERTICAL)
                
        elif evId == ID_HorizontalGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_HORIZONTAL)
                
        elif evId == ID_AllowFloating:
            event.Check((flags & aui.AUI_MGR_ALLOW_FLOATING) != 0)
                
        elif evId == ID_TransparentDrag:
            event.Check((flags & aui.AUI_MGR_TRANSPARENT_DRAG) != 0)
                
        elif evId == ID_TransparentHint:
            event.Check((flags & aui.AUI_MGR_TRANSPARENT_HINT) != 0)
                
        elif evId == ID_LiveUpdate:
            event.Check((flags & aui.AUI_MGR_LIVE_RESIZE) != 0)
                
        elif evId == ID_VenetianBlindsHint:
            event.Check((flags & aui.AUI_MGR_VENETIAN_BLINDS_HINT) != 0)
                
        elif evId == ID_RectangleHint:
            event.Check((flags & aui.AUI_MGR_RECTANGLE_HINT) != 0)
                
        elif evId == ID_NoHint:
            event.Check(((aui.AUI_MGR_TRANSPARENT_HINT |
                              aui.AUI_MGR_VENETIAN_BLINDS_HINT |
                              aui.AUI_MGR_RECTANGLE_HINT) & flags) == 0)
                
        elif evId == ID_HintFade:
            event.Check((flags & aui.AUI_MGR_HINT_FADE) != 0)
                
        elif evId == ID_NoVenetianFade:
            event.Check((flags & aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE) != 0)
                
        elif evId == ID_DefaultDockArt:
            event.Check(isinstance(self._mgr.GetArtProvider(), aui.AuiDefaultDockArt))

        elif evId == ID_ModernDockArt:
            event.Check(isinstance(self._mgr.GetArtProvider(), aui.ModernDockArt))

        elif evId == ID_SnapPanes:
            event.Check(self._snapped)
            
        elif evId == ID_NotebookNoCloseButton:
            event.Check((self._notebook_style & (aui.AUI_NB_CLOSE_BUTTON|aui.AUI_NB_CLOSE_ON_ALL_TABS|aui.AUI_NB_CLOSE_ON_ACTIVE_TAB)) != 0)
                
        elif evId == ID_NotebookCloseButton:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_BUTTON) != 0)
                
        elif evId == ID_NotebookCloseButtonAll:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_ON_ALL_TABS) != 0)
                
        elif evId == ID_NotebookCloseButtonActive:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_ON_ACTIVE_TAB) != 0)
                
        elif evId == ID_NotebookAllowTabSplit:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_SPLIT) != 0)
                
        elif evId == ID_NotebookAllowTabMove:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_MOVE) != 0)
                
        elif evId == ID_NotebookAllowTabExternalMove:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_EXTERNAL_MOVE) != 0)
                
        elif evId == ID_NotebookScrollButtons:
            event.Check((self._notebook_style & aui.AUI_NB_SCROLL_BUTTONS) != 0)
                
        elif evId == ID_NotebookWindowList:
            event.Check((self._notebook_style & aui.AUI_NB_WINDOWLIST_BUTTON) != 0)
                
        elif evId == ID_NotebookTabFixedWidth:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_FIXED_WIDTH) != 0)

        elif evId == ID_NotebookHideSingle:
            event.Check((self._notebook_style & aui.AUI_NB_HIDE_ON_SINGLE_TAB) != 0)

        elif evId == ID_NotebookSmartTab:
            event.Check((self._notebook_style & aui.AUI_NB_SMART_TABS) != 0)

        elif evId == ID_NotebookUseImagesDropDown:
            event.Check((self._notebook_style & aui.AUI_NB_USE_IMAGES_DROPDOWN) != 0)
            
        elif evId == ID_NotebookArtGloss:
            event.Check(self._notebook_theme == 0)
                
        elif evId == ID_NotebookArtSimple:
            event.Check(self._notebook_theme == 1)
                
        elif evId == ID_NotebookArtVC71:
            event.Check(self._notebook_theme == 2)
                
        elif evId == ID_NotebookArtFF2:
            event.Check(self._notebook_theme == 3)

        elif evId == ID_NotebookArtVC8:
            event.Check(self._notebook_theme == 4)
                
        elif evId == ID_NotebookArtChrome:
            event.Check(self._notebook_theme == 5)


    def OnPaneClose(self, event):

        if event.pane.name == "test10":
        
            res = wx.MessageBox("Are you sure you want to close/hide self pane?",
                                "AUI", wx.YES_NO, self)
            if res != wx.YES:
                event.Veto()
        

    def OnCreatePerspective(self, event):

        dlg = wx.TextEntryDialog(self, "Enter a name for the new perspective:", "AUI Test")

        dlg.SetValue("Perspective %u"%(len(self._perspectives) + 1))
        if dlg.ShowModal() != wx.ID_OK:
            return

        if len(self._perspectives) == 0:
            self._perspectives_menu.AppendSeparator()
        
        self._perspectives_menu.Append(ID_FirstPerspective + len(self._perspectives), dlg.GetValue())
        self._perspectives.append(self._mgr.SavePerspective())


    def OnCopyPerspectiveCode(self, event):

        s = self._mgr.SavePerspective()

        if wx.TheClipboard.Open():
        
            wx.TheClipboard.SetData(wx.TextDataObject(s))
            wx.TheClipboard.Close()
        

    def OnRestorePerspective(self, event):

        self._mgr.LoadPerspective(self._perspectives[event.GetId() - ID_FirstPerspective])


    def OnNotebookPageClose(self, event):

        ctrl = event.GetEventObject()
        if isinstance(ctrl.GetPage(event.GetSelection()), wx.html.HtmlWindow):
        
            res = wx.MessageBox("Are you sure you want to close/hide this notebook page?",
                                "AUI", wx.YES_NO, self)
            if res != wx.YES:
                event.Veto()


    def OnAllowNotebookDnD(self, event):

        # for the purpose of this test application, explicitly
        # allow all noteboko drag and drop events
        event.Allow()


    def GetStartPosition(self):

        x = 20
        pt = self.ClientToScreen(wx.Point(0, 0))
        return wx.Point(pt.x + x, pt.y + x)


    def OnCreateTree(self, event):

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Caption("Tree Control").
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(150, 300)).MinimizeButton(True))
        self._mgr.Update()


    def OnCreateGrid(self, event):

        self._mgr.AddPane(self.CreateGrid(), aui.AuiPaneInfo().
                          Caption("Grid").
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(300, 200)).MinimizeButton(True))
        self._mgr.Update()


    def OnCreateHTML(self, event):

        self._mgr.AddPane(self.CreateHTMLCtrl(), aui.AuiPaneInfo().
                          Caption("HTML Control").
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(300, 200)).MinimizeButton(True))
        self._mgr.Update()


    def OnCreateNotebook(self, event):

        self._mgr.AddPane(self.CreateNotebook(), aui.AuiPaneInfo().
                          Caption("Notebook").
                          Float().FloatingPosition(self.GetStartPosition()).
                          CloseButton(True).MaximizeButton(True).MinimizeButton(True))
        self._mgr.Update()


    def OnCreateText(self, event):

        self._mgr.AddPane(self.CreateTextCtrl(), aui.AuiPaneInfo().
                          Caption("Text Control").
                          Float().FloatingPosition(self.GetStartPosition()).
                          MinimizeButton(True))
        self._mgr.Update()


    def OnCreateSizeReport(self, event):

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Caption("Client Size Reporter").
                          Float().FloatingPosition(self.GetStartPosition()).
                          CloseButton(True).MaximizeButton(True).MinimizeButton(True))
        self._mgr.Update()


    def OnChangeContentPane(self, event):

        self._mgr.GetPane("grid_content").Show(event.GetId() == ID_GridContent)
        self._mgr.GetPane("text_content").Show(event.GetId() == ID_TextContent)
        self._mgr.GetPane("tree_content").Show(event.GetId() == ID_TreeContent)
        self._mgr.GetPane("sizereport_content").Show(event.GetId() == ID_SizeReportContent)
        self._mgr.GetPane("html_content").Show(event.GetId() == ID_HTMLContent)
        self._mgr.GetPane("notebook_content").Show(event.GetId() == ID_NotebookContent)
        self._mgr.Update()


    def OnDropDownToolbarItem(self, event):

        if event.IsDropDownClicked():
        
            tb = event.GetEventObject()
            tb.SetToolSticky(event.GetId(), True)

            # create the popup menu
            menuPopup = wx.Menu()
            bmp = wx.ArtProvider.GetBitmap(wx.ART_QUESTION, wx.ART_OTHER, wx.Size(16, 16))

            m1 =  wx.MenuItem(menuPopup, 10001, "Drop Down Item 1")
            m1.SetBitmap(bmp)
            menuPopup.AppendItem(m1)

            m2 =  wx.MenuItem(menuPopup, 10002, "Drop Down Item 2")
            m2.SetBitmap(bmp)
            menuPopup.AppendItem(m2)

            m3 =  wx.MenuItem(menuPopup, 10003, "Drop Down Item 3")
            m3.SetBitmap(bmp)
            menuPopup.AppendItem(m3)

            m4 =  wx.MenuItem(menuPopup, 10004, "Drop Down Item 4")
            m4.SetBitmap(bmp)
            menuPopup.AppendItem(m4)

            # line up our menu with the button
            rect = tb.GetToolRect(event.GetId())
            pt = tb.ClientToScreen(rect.GetBottomLeft())
            pt = self.ScreenToClient(pt)

            self.PopupMenu(menuPopup, pt)

            # make sure the button is "un-stuck"
            tb.SetToolSticky(event.GetId(), False)
        

    def OnTabAlignment(self, event):

        for pane in self._mgr.GetAllPanes():
        
            if isinstance(pane.window, aui.AuiNotebook):
            
                nb = pane.window
                style = nb.GetWindowStyleFlag()

                if event.GetId() == ID_NotebookAlignTop:
                    style &= ~aui.AUI_NB_BOTTOM
                    style ^= aui.AUI_NB_TOP
                    nb.SetWindowStyleFlag(style)
                elif event.GetId() == ID_NotebookAlignBottom:
                    style &= ~aui.AUI_NB_TOP
                    style ^= aui.AUI_NB_BOTTOM
                    nb.SetWindowStyleFlag(style)

                self._notebook_style = style
                nb.Update()
                nb.Refresh()
            

    def OnExit(self, event):

        self.Close(True)


    def OnAbout(self, event):

        wx.MessageBox("AUI Demo\nAn advanced window management library for wxPython",
                      "About AUI Demo", wx.OK, self)


    def CreateTextCtrl(self, ctrl_text=""):

        if ctrl_text.strip():
            text = ctrl_text
        else:
            text = "This is text box %d"%self._textCount
            self._textCount += 1

        return wx.TextCtrl(self,-1, text, wx.Point(0, 0), wx.Size(150, 90),
                           wx.NO_BORDER | wx.TE_MULTILINE)


    def CreateGrid(self):

        grid = wx.grid.Grid(self, -1, wx.Point(0, 0), wx.Size(150, 250),
                            wx.NO_BORDER | wx.WANTS_CHARS)
        grid.CreateGrid(50, 20)
        return grid


    def CreateTreeCtrl(self):

        tree = wx.TreeCtrl(self, -1, wx.Point(0, 0), wx.Size(160, 250),
                           wx.TR_DEFAULT_STYLE | wx.NO_BORDER)

        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16)))
        tree.AssignImageList(imglist)

        root = tree.AddRoot("AUI Project", 0)
        items = []
        
        items.append(tree.AppendItem(root, "Item 1", 0))
        items.append(tree.AppendItem(root, "Item 2", 0))
        items.append(tree.AppendItem(root, "Item 3", 0))
        items.append(tree.AppendItem(root, "Item 4", 0))
        items.append(tree.AppendItem(root, "Item 5", 0))

        for item in items:
            tree.AppendItem(item, "Subitem 1", 1)
            tree.AppendItem(item, "Subitem 2", 1)
            tree.AppendItem(item, "Subitem 3", 1)
            tree.AppendItem(item, "Subitem 4", 1)
            tree.AppendItem(item, "Subitem 5", 1)
        
        tree.Expand(root)

        return tree


    def CreateSizeReportCtrl(self, width=80, height=80):

        ctrl = SizeReportCtrl(self, -1, wx.DefaultPosition, wx.Size(width, height), self._mgr)
        return ctrl


    def CreateHTMLCtrl(self, parent=None):

        if not parent:
            parent = self

        ctrl = wx.html.HtmlWindow(parent, -1, wx.DefaultPosition, wx.Size(400, 300))
        ctrl.SetPage(self.GetIntroText())
        return ctrl


    def CreateNotebook(self):

        # create the notebook off-window to avoid flicker
        client_size = self.GetClientSize()
        ctrl = aui.AuiNotebook(self, -1, wx.Point(client_size.x, client_size.y),
                              wx.Size(430, 200), self._notebook_style)

        arts = [aui.AuiDefaultTabArt, aui.AuiSimpleTabArt, aui.VC71TabArt, aui.FF2TabArt,
                aui.VC8TabArt, aui.ChromeTabArt]

        art = arts[self._notebook_theme]()
        ctrl.SetArtProvider(art)

        page_bmp = wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16))
        ctrl.AddPage(self.CreateHTMLCtrl(ctrl), "Welcome to AUI", False, page_bmp)

        panel = wx.Panel(ctrl, -1)
        flex = wx.FlexGridSizer(0, 2)
        flex.Add((5, 5))
        flex.Add((5, 5))
        flex.Add(wx.StaticText(panel, -1, "wxTextCtrl:"), 0, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add(wx.TextCtrl(panel, -1, "", wx.DefaultPosition, wx.Size(100, -1)),
                 1, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add(wx.StaticText(panel, -1, "wxSpinCtrl:"), 0, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add(wx.SpinCtrl(panel, -1, "5", wx.DefaultPosition, wx.Size(100, -1),
                             wx.SP_ARROW_KEYS, 5, 50, 5), 0, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add((5, 5))
        flex.Add((5, 5))
        flex.AddGrowableRow(0)
        flex.AddGrowableRow(3)
        flex.AddGrowableCol(1)
        panel.SetSizer(flex)
        ctrl.AddPage(panel, "wxPanel", False, page_bmp)
 
        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 1", False, page_bmp)

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 2")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 3")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 4")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 5")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 6")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 7 (longer title)")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 8")

        ctrl.EnableTab(1, False)
        ctrl.SetPageTextColour(2, wx.RED)
        ctrl.SetPageTextColour(3, wx.BLUE)
        return ctrl


    def GetIntroText(self):

        text = \
        "<html><body>" \
        "<h3>Welcome to AUI</h3>" \
        "<br/><b>Overview</b><br/>" \
        "<p>AUI is an Advanced User Interface library for the wxPython toolkit " \
        "that allows developers to create high-quality, cross-platform user " \
        "interfaces quickly and easily.</p>" \
        "<p><b>Features</b></p>" \
        "<p>With AUI, developers can create application frameworks with:</p>" \
        "<ul>" \
        "<li>Native, dockable floating frames</li>" \
        "<li>Perspective saving and loading</li>" \
        "<li>Native toolbars incorporating real-time, &quotspring-loaded&quot dragging</li>" \
        "<li>Customizable floating/docking behavior</li>" \
        "<li>Completely customizable look-and-feel</li>" \
        "<li>Optional transparent window effects (while dragging or docking)</li>" \
        "<li>Splittable notebook control</li>" \
        "</ul>" \
        "<p><b>What's new in AUI?</b></p>" \
        "<p>Current wxAUI Version Tracked: wxWidgets 2.9.0 (SVN HEAD)" \
        "<p>The wxPython AUI version fixes the following bugs or implement the following" \
        " missing features (the list is not exhaustive): " \
        "<p><ul>" \
        "<li>Visual Studio 2005 style docking: <a href='http://www.kirix.com/forums/viewtopic.php?f=16&t=596'>" \
        "http://www.kirix.com/forums/viewtopic.php?f=16&t=596</a></li>" \
        "<li>Dock and Pane Resizing: <a href='http://www.kirix.com/forums/viewtopic.php?f=16&t=582'>" \
        "http://www.kirix.com/forums/viewtopic.php?f=16&t=582</a></li> " \
        "<li>Patch concerning dock resizing: <a href='http://www.kirix.com/forums/viewtopic.php?f=16&t=610'>" \
        "http://www.kirix.com/forums/viewtopic.php?f=16&t=610</a></li> " \
        "<li>Patch to effect wxAuiToolBar orientation switch: <a href='http://www.kirix.com/forums/viewtopic.php?f=16&t=641'>" \
        "http://www.kirix.com/forums/viewtopic.php?f=16&t=641</a></li> " \
        "<li>AUI: Core dump when loading a perspective in wxGTK (MSW OK): <a href='http://www.kirix.com/forums/viewtopic.php?f=15&t=627</li>'>" \
        "http://www.kirix.com/forums/viewtopic.php?f=15&t=627</li></a>" \
        "<li>wxAuiNotebook reordered AdvanceSelection(): <a href='http://www.kirix.com/forums/viewtopic.php?f=16&t=617'>"\
        "http://www.kirix.com/forums/viewtopic.php?f=16&t=617</a></li> " \
        "<li>Vertical Toolbar Docking Issue: <a href='http://www.kirix.com/forums/viewtopic.php?f=16&t=181'>" \
        "http://www.kirix.com/forums/viewtopic.php?f=16&t=181</a></li> " \
        "<li>Patch to show the resize hint on mouse-down in aui: <a href='http://trac.wxwidgets.org/ticket/9612'>" \
        "http://trac.wxwidgets.org/ticket/9612</a></li> " \
        "<li>The Left/Right and Top/Bottom Docks over draw each other: <a href='http://trac.wxwidgets.org/ticket/3516'>" \
        "<http://trac.wxwidgets.org/ticket/3516</a>/li>" \
        "<li>MinSize() not honoured: <a href='http://trac.wxwidgets.org/ticket/3562'>" \
        "http://trac.wxwidgets.org/ticket/3562</a></li> " \
        "<li>Layout problem with wxAUI: <a href='http://trac.wxwidgets.org/ticket/3597'>" \
        "http://trac.wxwidgets.org/ticket/3597</a></li>" \
        "<li>Resizing children ignores current window size: <a href='http://trac.wxwidgets.org/ticket/3908'>" \
        "http://trac.wxwidgets.org/ticket/3908</a></li> " \
        "<li>Resizing panes under Vista does not repaint background: <a href='http://trac.wxwidgets.org/ticket/4325'>" \
        "http://trac.wxwidgets.org/ticket/4325</a></li> " \
        "<li>Resize sash resizes in response to click: <a href='http://trac.wxwidgets.org/ticket/4547'>" \
        "http://trac.wxwidgets.org/ticket/4547</a></li> " \
        "<li>'Illegal' resizing of the AuiPane? (wxPython): <a href='http://trac.wxwidgets.org/ticket/4599'>" \
        "http://trac.wxwidgets.org/ticket/4599</a></li> " \
        "<li>Floating wxAUIPane Resize Event doesn't update its position: <a href='http://trac.wxwidgets.org/ticket/9773'>" \
        "http://trac.wxwidgets.org/ticket/9773</a></li>" \
        "<li>Don't hide floating panels when we maximize some other panel: <a href='http://trac.wxwidgets.org/ticket/4066'>"\
        "http://trac.wxwidgets.org/ticket/4066</a></li>" \
        "<li>wxAUINotebook incorrect ALLOW_ACTIVE_PANE handling: <a href='http://trac.wxwidgets.org/ticket/4361'>" \
        "http://trac.wxwidgets.org/ticket/4361</a></li> " \
        "<li>Page changing veto doesn't work, (patch supplied): <a href='http://trac.wxwidgets.org/ticket/4518'>" \
        "http://trac.wxwidgets.org/ticket/4518</a></li> " \
        "<li>Show and DoShow are mixed around in wxAuiMDIChildFrame: <a href='http://trac.wxwidgets.org/ticket/4567'>"\
        "http://trac.wxwidgets.org/ticket/4567</a></li> " \
        "<li>wxAuiManager & wxToolBar - ToolBar Of Size Zero: <a href='http://trac.wxwidgets.org/ticket/9724'>" \
        "http://trac.wxwidgets.org/ticket/9724</a></li> " \
        "<li>wxAuiNotebook doesn't behave properly like a container as far as...: <a href='http://trac.wxwidgets.org/ticket/9911'>" \
        "http://trac.wxwidgets.org/ticket/9911</a></li>" \
        "<li>Serious layout bugs in wxAUI: <a href='http://trac.wxwidgets.org/ticket/10620'>" \
        "http://trac.wxwidgets.org/ticket/10620</a></li>" \
        "</ul>" \
        "<p>Plus the following features:" \
        "<p><ul>" \
        "<li><b>AuiManager:</b></li>" \
        "<ul>" \
        "<li>Implementation of a simple minimize pane system: Clicking on this minimize button causes a new " \
        "<i>AuiToolBar</i> to be created and added to the frame manager, (currently the implementation is such " \
        "that panes at West will have a toolbar at the right, panes at South will have toolbars at the " \
        "bottom etc...) and the pane is hidden in the manager. " \
        "Clicking on the restore button on the newly created toolbar will result in the toolbar being " \
        "removed and the original pane being restored;</li>" \
        "<li>Panes can be docked on top of each other to form <i>AuiNotebooks</i>; <i>AuiNotebooks</i> tabs can be torn " \
        "off to create floating panes;</li>" \
        "<li>On Windows XP, use the nice sash drawing provided by XP while dragging the sash;</li>" \
        "<li>Possibility to set an icon on docked panes;</li>" \
        "<li>Possibility to draw a sash visual grip, for enhanced visualization of sashes;</li>" \
        "<li>Implementation of a native docking art (<i>ModernDockArt</i>). Windows XP only, <b>requires</b> Mark Hammond's " \
        "pywin32 package (winxptheme);</li>" \
        "<li>Possibility to set a transparency for floating panes (a la Paint .NET);</li>" \
        "<li>Snapping the main frame to the screen in any positin specified by horizontal and vertical " \
        "alignments;</li>" \
        "<li>Snapping floating panes on left/right/top/bottom or any combination of directions, a la Winamp.</li>" \
        "</ul><p>" \
        "<li><b>AuiNotebook:</b></li>" \
        "<ul>" \
        "<li>Implementation of the style <tt>AUI_NB_HIDE_ON_SINGLE_TAB</tt>, a la <i>wx.lib.agw.flatnotebook</i>;</li>" \
        "<li>Implementation of the style <tt>AUI_NB_SMART_TABS</tt>, a la <i>wx.lib.agw.flatnotebook</i>;</li>" \
        "<li>Implementation of the style <tt>AUI_NB_USE_IMAGES_DROPDOWN</tt>, which allows to show tab images " \
        "on the tab dropdown menu instead of bare check menu items (a la <i>wx.lib.agw.flatnotebook</i>);</li>" \
        "<li>6 different tab arts are available, namely:</li>" \
        "<ul>" \
        "<li>Default 'glossy' theme (as in <i>wx.aui.AuiNotebook</i>)</li>" \
        "<li>Simple theme (as in <i>wx.aui.AuiNotebook</i>)</li>" \
        "<li>Firefox 2 theme</li>" \
        "<li>Visual Studio 2003 theme (VC71)</li>" \
        "<li>Visual Studio 2005 theme (VC81)</li>" \
        "<li>Google Chrome theme (only <tt>AUI_NB_TOP</tt> at the moment)</li>" \
        "</ul>" \
        "<li>Enabling/disabling tabs;</li>" \
        "<li>Setting the colour of the tab's text. </li>" \
        "</ul><p>" \
        "<li><b>AuiToolBar:</b></li>" \
        "<ul>" \
        "<li><tt>AUI_TB_PLAIN_BACKGROUND</tt> style that allows to easy setup a plain background to the AUI toolbar, " \
        "without the need to override drawing methods. This style contrasts with the default behaviour " \
        "of the <i>wx.aui.AuiToolBar</i> that draws a background gradient and this break the window design when " \
        "putting it within a control that has margin between the borders and the toolbar (example: put " \
        "<i>wx.aui.AuiToolBar</i> within a <i>wx.StaticBoxSizer</i> that has a plain background);</li>" \
        "<li><i>AuiToolBar</i> allow item alignment: <a href='http://trac.wxwidgets.org/ticket/10174'> " \
        "http://trac.wxwidgets.org/ticket/10174</a>;</li>" \
        "<li><i>AUIToolBar</i> <i>DrawButton()</i> improvement: <a href='http://trac.wxwidgets.org/ticket/10303'>" \
        "http://trac.wxwidgets.org/ticket/10303</a>;</li>" \
        "<li><i>AuiToolBar</i> automatically assign new id for tools: <a href='http://trac.wxwidgets.org/ticket/10173'>" \
        "http://trac.wxwidgets.org/ticket/10173</a>;</li>" \
        "<li><i>AuiToolBar</i> Allow right-click on any kind of button: <a href='http://trac.wxwidgets.org/ticket/10079'>" \
        "http://trac.wxwidgets.org/ticket/10079</a>;</li>" \
        "<li><i>AuiToolBar</i> idle update only when visible: <a href='http://trac.wxwidgets.org/ticket/10075'>" \
        "http://trac.wxwidgets.org/ticket/10075</a>.</li>" \
        "</ul>" \
        "</ul>" \
        "</body></html>"

        return text


def Main():

    app = wx.PySimpleApp()
    frame = AuiFrame(None, -1, "AUI Test Frame", size=(800, 600))
    frame.CenterOnScreen()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':        
    Main()

    