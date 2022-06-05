from unittest import result
from PIL import Image
from Params import SystemParams
from Library.LibData import *


class SamplePicParam:

    @property
    def SamplePic(self): return LibData.Merge(
        "/", SystemParams.SysPath.SrcPath, "SamplePic")

    @property
    def AdornerCase_Pen(self):
        result = LibData.Merge(
            "/", self.SamplePic, "AdornerCase/Pen")
        return result

    @property
    def AdornerCase_Shape(self): return LibData.Merge(
        "/", SC.SamplePic, "AdornerCase/Shape")

    @property
    def AdornerCase_Shape_3D(self): return LibData.Merge(
        "/", SC.SamplePic, "AdornerCase/Shape_3D")

    @property
    def AdornerCase_Line(self): return LibData.Merge(
        "/", SC.SamplePic, "AdornerCase/Line")

    @property
    def AdornerCase_Text(self): return LibData.Merge(
        "/", SC.SamplePic, "AdornerCase/Text")

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

    @property
    def EraserCase1(self): return Image.open(
        LibData.Merge(
            "/", SC.AdornerCase_Pen, "Eraser Case 1-1.png"))

SC = SamplePicParam()
