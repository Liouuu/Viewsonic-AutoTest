import os
logPath = "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\"
# logPath = "./log/"

def logAmountCheck():
    allFiles = os.listdir(logPath) #到該目錄下讀現有檔案名稱並存進list (allFiles是list)
    if len(allFiles) > 9:
        os.remove(logPath + allFiles[0]) #超過預定數量就做刪檔案的動作
    
