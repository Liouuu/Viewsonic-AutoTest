from Library.LibData import LibData


class c_sysPath:
    @property
    def DestPath(self):
        """輸出路徑"""
        return "./Documents/Output"

    @property
    def SrcPath(self):
        """測試資料路徑(Input Data)"""
        return "./Documents/Src"

    @property
    def _LogPath(self):
        """Log路徑"""
        return LibData.Merge("/", self.DestPath, "Logs")

    @property
    def _ExcelPath(self):
        """ExcelLog路徑"""
        return LibData.Merge("/", self.DestPath, "Excels")

    @property
    def _Screenshots(self):
        """截圖路徑"""
        return LibData.Merge("/", self.DestPath, "Screenshots")

    @property
    def _BlackBoxExcel(self):
        """黑箱測試文檔"""
        return LibData.Merge("/", self.SrcPath, "TestStep")


SysPath = c_sysPath()


class c_SysParam:
    @property
    def _Email(self):
        return "mvbaautotest2@gmail.com"

    @property
    def _Password(self):
        return "$Password1"


SysParams = c_SysParam()


class c_fileExt:
    @property
    def _xlsx(self):
        return ".xlsx"

    @property
    def _png(self):
        return ".png"


FileExt = c_fileExt()


class c_imgPath:

    @property
    def _TextPath():
        return SysPath._Screenshots+"/Text"


ImgPath = c_imgPath()
