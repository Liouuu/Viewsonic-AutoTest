from openpyxl.drawing.image import Image
from Params. SystemParams import FileExt
from openpyxl import *
import os


class LibExcel:
    __workbook = Workbook

    def __init__(self, path, name):
        self.Path = path
        self.fileName = name

    def Createfile(self, isCreateNew=False):
        if os.path.isfile(self.Path + self.fileName):
            if isCreateNew:
                '覆蓋'
            else:
                self.__workbook = self.Openfile()
        else:
            self.__workbook = Workbook()

    def Openfile(self, srcPath, srcFileName):
        self.__workbook = load_workbook(srcPath+srcFileName+FileExt._xlsx)

    def WriteDatas(self, sheets=[], isWriteEmpty=False):
        idx = 0
        for table in sheets:
            self.WriteData(idx, table, sheets[table], isWriteEmpty)
            idx += 1

    def WriteData(self, sheetIdx, sheetName, table=[], isWriteEmpty=False):
        self.__workbook.create_sheet(sheetName, sheetIdx)
        self.__workbook.active = sheetIdx
        sheet = self.__workbook.active
        rowIdx = 1
        for row in table:
            columnIdx = 1
            for columnName, colunmValue in row.__dict__.items():
                # match type(colunmValue):
                # case isinstance(str):
                if(isinstance(colunmValue, str)):
                    if(colunmValue != '' or isWriteEmpty):
                        sheet.cell(rowIdx, columnIdx, colunmValue)
                elif (isinstance(colunmValue, Image)):
                    # case isinstance(Image):
                    #    if(colunmValue == null and isWriteEmpty):
                    # pass
                    # sheet.add_image(colunmValue, rowIdx, columnIdx)
                    # Ascii取大寫英文字母欄位
                    sheet.add_image(colunmValue, chr(columnIdx+64)+str(rowIdx))
                columnIdx += 1
            rowIdx += 1

    def AutoSize(self):
        self.__workbook

    def Save(self):
        self.__workbook.save()
        self.__workbook.close()

    def SaveAs(self):
        self.__workbook.save(self.Path + "/"+self.fileName + FileExt._xlsx)
        self.__workbook.close()
