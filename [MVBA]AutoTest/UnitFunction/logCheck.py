import os
excelPath = "./Output/Excels/"
logPath = "./Output/Logs/"


def logAmountCheck():
    allFiles = os.listdir(logPath)  # 到該目錄下讀現有檔案名稱並存進list (allFiles是list)
    allFiles = sorted(allFiles, key=lambda x: os.path.getmtime(
        os.path.join(logPath, x)))  # 依照檔案修改時間排序
    for i in range(len(allFiles) - 30):  # 數量上限30
        os.remove(logPath + allFiles[i])  # 超過預定數量就做刪檔案的動作


def excelAmountCheck():
    allFiles = os.listdir(excelPath)  # 到該目錄下讀現有檔案名稱並存進list (allFiles是list)
    allFiles = sorted(allFiles, key=lambda x: os.path.getmtime(
        os.path.join(excelPath, x)))  # 依照檔案修改時間排序
    for i in range(len(allFiles) - 30):  # 數量上限30
        os.remove(excelPath + allFiles[i])  # 超過預定數量就做刪檔案的動作
