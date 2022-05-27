from pyclbr import Function

from django.test import TestCase
from Library import LibLogHelper
from Library.LibData import LibData
from Library.LibLogHelper import LogPackage
from openpyxl.drawing.image import Image
from inspect import getmembers, isfunction


class TestClass:
    def functionA():
        print("A")

    def functionB():
        print("B")

    def functionC():
        print("C")

    def functionD():
        print("D")

    def functionE():
        print("E")

    def functionF():
        print("F")


LibData.DynamicExecClassFunction(TestClass)
print(callable(TestClass.functionA))


# sheetName = "TextCase1"
# LogPack = LogPackage("TestFile", srcFileName="Text")
# LogPack.NewLogSheet(sheetName, LibLogHelper.UnitLogObj())
# # img = Image("./TestCases/Screenshots/Adorner/Pen/Menu/Menu.png")
# LogPack.AddUnitLog(sheetName, "執行貼圖", "執行結果")
# # LogPack.AddLogRow(sheetName, "執行貼圖", "執行結果", img)
# LogPack.CreateLog()
