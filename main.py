
import pyautogui
import time
from time import sleep
def start_game():
        x = pyautogui.locateOnScreen(r"C:\Users\prokopchick\PycharmProjects\pythonProject\play.png")
        pyautogui.click(x)
        y = pyautogui.locateOnScreen(r"C:\Users\prokopchick\PycharmProjects\pythonProject\findgame.png")
        pyautogui.click(y)
def accept():
    x = None
    while x == None:
        x = pyautogui.locateCenterOnScreen(r"C:\Users\prokopchick\PycharmProjects\pythonProject\accept.png")
        print("Поиск игры...")
        time.sleep(3)
    d1, d2, d3, d4, d5 = pyautogui.locateAllOnScreen(r"C:\Users\prokopchick\PycharmProjects\pythonProject\accept.png")
    pyautogui.click(d1, duration= 1.5)
    pyautogui.click(d2, duration= 1.5)
    pyautogui.click(d3, duration= 1.5)
    pyautogui.click(d4, duration= 1.5)
    pyautogui.click(d5, duration= 1.5)


def selectchar():
    d1, d2, d3, d4, d5 = pyautogui.locateAllOnScreen(r"C:\Users\prokopchick\PycharmProjects\pythonProject\random.png")

    pyautogui.click(d1, duration=1.5)
    pyautogui.hotkey("alt", "tab")
    pyautogui.click(d2, duration=1.5)
    pyautogui.hotkey("alt", "tab")
    pyautogui.click(d3, duration=1.5)
    pyautogui.hotkey("alt", "tab")
    pyautogui.click(d4, duration=1.5)
    pyautogui.hotkey("alt", "tab")
    pyautogui.click(d5, duration=1.5)
    pyautogui.hotkey("alt", "tab")

def feed1():
    x1 = 57
    y1 = 459
    x2 = 165
    y2 = 480
    pyautogui.rightClick(x1, y1, duration=1)

    pyautogui.rightClick(x1, y1, duration=1)

    pyautogui.doubleClick(x2, y2, duration=1)
    time.sleep(0.5)
def feed2():
    x1 = 699
    y1 = 459
    x2 = 800
    y2 = 480
    pyautogui.rightClick(x1, y1, duration=1)

    pyautogui.rightClick(x1, y1, duration=1)

    pyautogui.doubleClick(x2, y2, duration=1)
    time.sleep(0.5)
def feed3():
    x1 = 1340
    y1 = 459
    x2 = 1454
    y2 = 480
    pyautogui.rightClick(x1, y1, duration=1)

    pyautogui.rightClick(x1, y1, duration=1)

    pyautogui.doubleClick(x2, y2, duration=1)
    time.sleep(0.5)
def feed4():
    x1 = 57
    y1 = 978
    x2 = 173
    y2 = 998
    pyautogui.rightClick(x1, y1, duration=1)

    pyautogui.rightClick(x1, y1, duration=1)

    pyautogui.doubleClick(x2, y2, duration=1)
    time.sleep(0.5)
def feed5():
    x1 = 699
    y1 = 978
    x2 = 816
    y2 = 998
    pyautogui.rightClick(x1, y1, duration=1)

    pyautogui.rightClick(x1, y1, duration=1)

    pyautogui.doubleClick(x2, y2, duration=1)
    time.sleep(0.5)

def feedmid():
   feed1()
   pyautogui.hotkey('alt', 'tab')
   feed2()
   pyautogui.hotkey('alt', 'tab')
   feed3()
   pyautogui.hotkey('alt', 'tab')
   feed4()
   pyautogui.hotkey('alt', 'tab')
   feed5()
   pyautogui.hotkey('alt', 'tab')

script = None
while script != 1:

    start_game()
    accept()
    sleep(10)
    pyautogui.hotkey("win")
    pyautogui.click(1883,906, duration=0.25)
    sleep(25)

    print("Выбор персонажа")
    selectchar()
    sleep(60)
    victory = None
    end = None
    error = None
    while end != True:
        victory = pyautogui.locateCenterOnScreen(r"C:\Users\prokopchick\PycharmProjects\pythonProject\play.png")
        error = pyautogui.locateCenterOnScreen(r"C:\Users\prokopchick\PycharmProjects\pythonProject\accept.png")

        if victory != None or error != None:
            end = True
            print("Игра завершилась")
        else:
            end = False
            print("Игра идет")
            feedmid()
            sleep(90)



