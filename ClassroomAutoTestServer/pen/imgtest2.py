import cv2
save_path = "C:/Users/kero/Desktop/classroom_pen_0916/Classroom/case_img/marker/marker_menu_" + str(1) + ".png"
open_path = "C:/Users/kero/Desktop/classroom_pen_0916/Classroom/sample/marker/marker_menu_sample_" + str(1) + ".png"
image1 = cv2.imread(open_path)
image2 = cv2.imread(save_path)
allPoints = len(image1)*len(image1[0])
errorPoints = 0
#print(image1)
#print(image2)
for i in range (len(image1)):
    for j in range (len(image1[0])):
        for k in range(len(image1[0][0])):
            if image1[i][j][k] != image2[i][j][k]:
                errorPoints += 1
                break
if errorPoints/allPoints < 0.12:
    print(errorPoints/allPoints)
    print("Pass")
else:
    print(errorPoints/allPoints)
    print("False")
