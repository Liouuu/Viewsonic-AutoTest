import cv2

def menu_compare(sample, case): #菜單比對，與畫布比對相同，只有Print的地方描述有差
    image1 = cv2.imread(sample)
    image2 = cv2.imread(case)
    allpoint = len(image1) * len(image1[0])
    errorCount = 0
    for i in range(len(image1)):
        for j in range(len(image1[0])):
            for k in range(len(image1[0][0])):
                if image1[i][j][k] != image2[i][j][k]:
                    errorCount += 1
                    break
    #print("全部的點: ", allpoint)
    #print("誤差值: ", errorCount)
    print("Menu所有點的數量: ", allpoint, " / Menu有誤差的點數量: ", errorCount, " / Menu誤差率: ",float(errorCount/allpoint))
    if errorCount / allpoint < 0.1:
        #print("Pass")
        return True
    else:
        #print("Failed")
        return False