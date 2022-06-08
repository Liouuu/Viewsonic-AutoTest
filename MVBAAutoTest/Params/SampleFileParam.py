from io import BytesIO
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
            "/", self.SamplePic, "Adorner/Pen")
        return result

    @property
    def AdornerCase_Shape(self): return LibData.Merge(
        "/", SC.SamplePic, "Adorner/Shape")

    @property
    def AdornerCase_Shape_3D(self): return LibData.Merge(
        "/", SC.SamplePic, "Adorner/Shape_3D")

    @property
    def AdornerCase_Line(self): return LibData.Merge(
        "/", SC.SamplePic, "Adorner/Line")

    @property
    def AdornerCase_Text(self): return LibData.Merge(
        "/", SC.SamplePic, "Adorner/Text")

    @property
    def Pen_AdorneMenu(self): return LibData.GetFileBytes(
        LibData.Merge("/", SC.AdornerCase_Pen, "AdornerMenu1.png"))

    @property
    def Pen_Delete(self): return LibData.GetFileBytes(
        LibData.Merge("/", SC.AdornerCase_Pen, "Delete1.png"))

    @property
    def Pen_Lock1(self): return LibData.GetFileBytes(
        LibData.Merge("/", SC.AdornerCase_Pen, "Lock1.png"))

    @property
    def Pen_Lock2(self): return LibData.GetFileBytes(
        LibData.Merge("/", SC.AdornerCase_Pen, "Lock2.png"))

    @property
    def EraserCase1(self): return LibData.GetFileBytes(
        LibData.Merge("/", SC.AdornerCase_Pen, "Eraser Case 1-1.png"))


SC = SamplePicParam()
