import pyautogui
import time
import pynput

width, height = pyautogui.size() # 取得螢幕寬度、高度
print(width, height)

with pynput.mouse.Events() as event:
    count = 0
    for j in event:
        if isinstance(j, pynput.mouse.Events.Click) and count <= 5:
            print(j.x, j.y, j.button, j.pressed)
            count += 1
        elif count >= 5:
            break





