import pyautogui
import numpy as np
import cv2

def capture_screen():
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

def record_screen(stop_flag, filename):
    screen_size = pyautogui.size()

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(filename, fourcc, 20.0, screen_size)

    while not stop_flag["stop"]:
        frame = capture_screen()
        out.write(frame)

    out.release()
