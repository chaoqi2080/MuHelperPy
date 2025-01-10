import time

import pyautogui
import logging


def move_to_position(pos, msg):
    if len(pos) != 2:
        logging.error("传入的坐标点不合法")
        return

    logging.info("移动鼠标到位置 = [%d, %d], %s", pos[0], pos[1], msg)
    pyautogui.moveTo(pos[0], pos[1], 1.0)


def signal_left_click():
    pyautogui.click()


def double_left_click():
    pyautogui.click()
    pyautogui.click()


