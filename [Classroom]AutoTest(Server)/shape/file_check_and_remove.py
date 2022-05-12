import os
import write_log

def fileCheck_and_remove(filePath, logPath):  #檢查該路徑下是否有此檔案
    isFileExists = os.path.exists(filePath) 
    content = "Is the target file " + filePath + "existed? " + str(isFileExists)
    print("Is the target file", filePath, "existed? ", isFileExists) #有會回傳True，沒有就是False
    write_log.log(content, logPath)
    if isFileExists == True: 
        os.remove(filePath) #有檔案在就刪除
    else:
        pass