from LibData. LibExcel import LibExcel
from Params.SystemParams import SysPath, FileExt
from Params import LibParams
import datetime


# Logs：Dictionary，Key值為SheetName,Value為List的LibLogObj


class LogPackage:
    def __init__(self,  logName, srcFilePath=SysPath._SrcPath, srcFileName="", logPath=SysPath._ExcelPath, logDict=dict(), logType=LibParams.LogType.excel):
        self.__LogPath = logPath
        self.__LogName = logName + "-" + \
            datetime.datetime.today().strftime("%Y-%m-%d %H：%M：%S")
        self.__srcFilePath = srcFilePath
        self.__srcFileName = srcFileName + FileExt._xlsx
        self.LogDict = logDict
        self.__LogType = logType

    def CreateLog(self):
        match self.__LogType:
            case LibParams.LogType.excel:
                self.__CreateExcelLog()
            case _:
                pass

    def NewLogSheet(self, caseName):
        logList = []
        logList.append(_LogObj())
        self.LogDict[caseName] = logList

    def AddLogRow(self, caseName, action, result, screenshot):
        logList = list(self.LogDict[caseName])
        logList.append(_LogObj(datetime.datetime.now().strftime(
            "%H:%M:%S"), action=action, result=result, screenshot=screenshot))
        self.LogDict[caseName] = logList

    def __CreateExcelLog(self):
        excel = LibExcel(self.__LogPath, self.__LogName)
        excel.Openfile(self.__srcFilePath, self.__srcFileName)
        excel.WriteDatas(self.LogDict)
        excel.AutoSize()
        excel.SaveAs()

# Log欄位格式
# 注：1. 更動欄位順序同時，也要調整Excel輸出格式的順序
#     2. Step欄位永遠為空


class _LogObj:
    def __init__(self, time="", action="", result="", screenshot=""):
        self.Time = time
        self.Step = ""
        self.Action = action
        self.Result = result
        self.Screenshot = screenshot  # 注意：應給予Img類格式
