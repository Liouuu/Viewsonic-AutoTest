import os
from Params.SystemParams import sysPath


def logAmountCheck():
    # 到該目錄下讀現有檔案名稱並存進list (allFiles是list)
    allFiles = os.listdir(sysPath._LogPath)
    allFiles = sorted(allFiles, key=lambda x: os.path.getmtime(
        os.path.join(sysPath._LogPath, x)))  # 依照檔案修改時間排序
    for i in range(len(allFiles) - 30):  # 數量上限30
        os.remove(sysPath._LogPath + allFiles[i])  # 超過預定數量就做刪檔案的動作


def excelAmountCheck():
    # 到該目錄下讀現有檔案名稱並存進list (allFiles是list)
    allFiles = os.listdir(sysPath._ExcelPath)
    allFiles = sorted(allFiles, key=lambda x: os.path.getmtime(
        os.path.join(sysPath._ExcelPath, x)))  # 依照檔案修改時間排序
    for i in range(len(allFiles) - 30):  # 數量上限30
        os.remove(sysPath._ExcelPath + allFiles[i])  # 超過預定數量就做刪檔案的動作
