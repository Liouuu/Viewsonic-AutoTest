from PIL import Image
import imagehash

save_path = "C:/Users/kero/Desktop/classroom_pen_0916/Classroom/case_img/marker/marker_menu_" + str(1) + ".png"
open_path = "C:/Users/kero/Desktop/classroom_pen_0916/Classroom/sample/marker/marker_menu_sample_" + str(1) + ".png"
hash = imagehash.average_hash(Image.open(open_path))
otherhash = imagehash.average_hash(Image.open(save_path))
print(hash)
print(otherhash)
if hash == otherhash and hash - otherhash == 0:
    print("Marker color" + str(1) + " True!")
else:
    print("Marker color" + str(1) + " False!")
    