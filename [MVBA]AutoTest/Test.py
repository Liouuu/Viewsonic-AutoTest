from Library.LibData import LibData
from Library.LibLogObj import LogPackage
from openpyxl.drawing.image import Image
strval = LibData.StringMerge("/", "test1/", "test2", "test3")


sheetName = "TextCase1"

LogPack = LogPackage("TestFile", srcFileName="Text")

# 分頁1
LogPack.NewLogSheet(sheetName)
# ..
img = Image("./TestCases/Screenshots/Adorner/Pen/Menu/Menu.png")
LogPack.AddLogRow(sheetName, "執行貼圖", "執行結果", img)
# ..
# ..
# ..
# 分頁2
# ..
# ..
LogPack.CreateLog()
