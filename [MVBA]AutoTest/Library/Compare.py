import numpy as np
import cv2


def isImgEqual(lhs, rhs):  # lhs, rhs are strings of img location
    if np.array_equal(lhs, rhs):
        return True
    return False
