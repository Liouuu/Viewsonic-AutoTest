from unittest import result
from PIL import Image
from Params import SystemParams
from Library.LibData import *


class ControlPic:

    @property
    def ControlPicure(self): return LibData.Merge(
        "/", SystemParams.SysPath.SrcPath, "ControlPicture")

    @property
    def AdornerCase_Pen(self):
        result = LibData.Merge(
            "/", SC.ControlPicure, "AdornerCase/Pen")
        return result

    @property
    def AdornerCase_Shape(self): return LibData.Merge(
        "/", SC.ControlPicure, "AdornerCase/Shape")

    @property
    def AdornerCase_Shape_3D(self): return LibData.Merge(
        "/", SC.ControlPicure, "AdornerCase/Shape_3D")

    @property
    def AdornerCase_Line(self): return LibData.Merge(
        "/", SC.ControlPicure, "AdornerCase/Line")

    @property
    def AdornerCase_Text(self): return LibData.Merge(
        "/", SC.ControlPicure, "AdornerCase/Text")

    @property
    def Pen_AdorneMenu(self): return Image.open(
        LibData.Merge("/", SC.AdornerCase_Pen, "AdornerMenu1.png"))

    @property
    def Pen_Delete(self): return Image.open(
        LibData.Merge(
            "/", SC.AdornerCase_Pen, "Delete1.png"))

    @property
    def Pen_Lock1(self): return Image.open(
        LibData.Merge(
            "/", SC.AdornerCase_Pen, "Lock1.png"))

    @property
    def Pen_Lock2(self): return Image.open(
        LibData.Merge(
            "/", SC.AdornerCase_Pen, "Lock2.png"))


SC = ControlPic()
