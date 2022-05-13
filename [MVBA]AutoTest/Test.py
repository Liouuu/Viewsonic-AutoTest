from LibData.LibLogObj import LogPackage
from openpyxl.drawing.image import Image

LogPack = LogPackage("TestFile")
LogPack.NewLogSheet("TestSheet")
img = Image("./TestCases/Screenshots/Adorner/Pen/Menu/Menu.png")
LogPack.AddLogRow("TestSheet", "執行貼圖", "執行結果", img, level="錯誤")
LogPack.CreateLog()
