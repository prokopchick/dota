
import pyautogui
import time
import cv2
import numpy as np
import pyscreenshot as ImageGrab


def start_game(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()
def move_to(x, y):
    pyautogui.moveTo(x, y, duration=0.5)

def left_click():
    pyautogui.click(button='right')

def farm_jungle():

    time.sleep(3)


    jungle_center_x = 93
    jungle_center_y = 564


    move_to(jungle_center_x, jungle_center_y)


    print("Farming jungle...")
    for i in range(5):
        left_click()
    time.sleep(1) # Задержка между каждой атакой

    print("Finished farming jungle!")


farm_jungle()
