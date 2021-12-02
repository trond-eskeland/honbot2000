from pyautogui import * 
import pyautogui
import pynput
import time
import logging
import win32api, win32con
import keyboard

### Controllers ###
mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()


### Logging config ###
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")


### Classes ### 
class Mouse(object):
    def __init__(self):
        self.x_res = win32api.GetSystemMetrics(0)
        self.y_res = win32api.GetSystemMetrics(1)

    def rightClick(self, x, y):
        logging.info('Used Mouse-class')
        nx = x*65535/self.x_res
        ny = y*65535/self.y_res
        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(nx),int(ny))
        win32api.Sleep(50)
        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.Sleep(50)
        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        win32api.Sleep(50)

### Basic Functions ###
def getEnemyPosition():
    # Returns X, Y coordinates of enemy
    enemyLocation = pyautogui.locateOnScreen('enemyHealthBar.png', confidence=0.9)
    if enemyLocation != None:
        logging.info('Enemy found:\t\t%d %d', enemyLocation[0], enemyLocation[1])
        return enemyLocation[0]+50, enemyLocation[1]+100, 1
    else:
        return mouse.position[0], mouse.position[1], 0

def isCodexready():
    codex = pyautogui.locateOnScreen('Codex1.png', grayscale=True, confidence=0.8)
    if codex != None:
        logging.info('Spell ready:\t\tCodex')
        return codex[0], codex[1], 1
    else:
        return 0, 0, 0

def pressKey(key):
    keyboard.press(str(key))
    keyboard.release(str(key))

def targetEnemy():
    enemyPosition = getEnemyPosition()
    
