import cv2
import numpy as np
import pyautogui
from mss import mss


def pattern_matching(screen, pattern, found):
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    _, screen_roi_thresh = cv2.threshold(screen_gray, 200, 255, cv2.THRESH_BINARY)

    result = cv2.matchTemplate(screen_roi_thresh, pattern, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)

    threshold = 0.015

    if result[max_loc[1], max_loc[0]] > threshold and not found:
        pyautogui.press('enter')
        return True

    return False


def main():
    bounding_box = {'top': 666, 'left': 996, 'width': 75, 'height': 49}
    pattern = cv2.imread("img_1.png", cv2.IMREAD_UNCHANGED)
    sct = mss()
    pattern_gray2 = cv2.cvtColor(pattern, cv2.COLOR_BGR2GRAY)
    _, pattern_thresh = cv2.threshold(pattern_gray2, 200, 255, cv2.THRESH_BINARY)

    found = False
    while True:
        screen_np = np.array(sct.grab(bounding_box))

        found = pattern_matching(screen_np, pattern_thresh, found)


if __name__ == "__main__":
    main()
