from numpy import imag
from Library.LibData import LibData
from Library.LibExcel import LibExcel
from Params.SystemParams import SysPath, FileExt
from Params import LibParams
import datetime
from openpyxl.drawing.image import Image


# Logs：Dictionary，Key值為SheetName,Value為List的LibLogObj


class LogPackage:
    """Log包"""

# region Construct
    def __init__(self,  logName, srcFilePath=SysPath._SrcPath, srcFileName="",
                 logPath=SysPath._ExcelPath, logDict=dict(), logType: LibParams.LogType = LibParams.LogType.excel):
        self.__LogPath = logPath
        self.__LogName = LibData.StringMerge(
            "-", logName, datetime.datetime.today().strftime("%Y-%m-%d %H：%M：%S"))
        self.__srcFilePath = srcFilePath
        self.__srcFileName = srcFileName + FileExt._xlsx
        self.LogDict = logDict
        self.__LogType = logType
# endregion

# region Public
    def CreateLog(self):
        if self.__LogType is LibParams.LogType.excel:
            self.__CreateExcelLog()
        else:
            pass

    def NewLogSheet(self, sheetName):
        logList = []
        logList.append(LogObj())
        self.LogDict[sheetName] = logList

    def AddLogRow(self, sheetName, action, result, screenshot: Image = Image()):
        logList = list(self.LogDict[sheetName])
        logList.append(LogObj(datetime.datetime.now().strftime(
            "%H:%M:%S"), action=action, result=result, screenshot=screenshot))
        self.LogDict[sheetName] = logList
# endregion

# region Private
    def __CreateExcelLog(self):
        excel = LibExcel(self.__LogPath, self.__LogName)
        excel._Openfile(self.__srcFilePath, self.__srcFileName)
        excel._WriteDatas(self.LogDict)
        excel._AutoSize()
        excel._SaveAs()
# endregion

# Log欄位格式
# 注：1. 更動欄位順序同時，也要調整Excel輸出格式的順序
#     2. Step欄位永遠為空


class LogObj:
    def __init__(self, time: str, action: str, result: str, screenshot: Image = Image()):
        self.Time = time
        self.Step = ""
        self.Action = action
        self.Result = result
        self.Screenshot = screenshot  # 注意：應給予Img類格式
