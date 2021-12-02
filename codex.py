import pynput
import time
from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con
import pynput
import time
import overlay

from playsound import playsound

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

position = []
beforeBotting = []
codexPosition = [0,0]

print("Gzdingty - Codex bot")
print("Usage: Ask a friend")

def LookForEnemy():
    enemyLocation = pyautogui.locateOnScreen('enemyHealthBar.png', confidence=0.9)
    if enemyLocation != None:
        time.sleep(0.05)
        print("Codex: " + str(codexPosition[0]) + " " + str(codexPosition[1]))
        mouse.position = (codexPosition[0], codexPosition[1])
        mouse.press(pynput.mouse.Button.left)
        time.sleep(0.05)
        mouse.release(pynput.mouse.Button.left)
        time.sleep(0.05)
        print("Enemy Position: " + str(enemyLocation[0]) + " " + str(enemyLocation[1]))
        mouse.position = (enemyLocation[0]+50, enemyLocation[1]+100)
        time.sleep(0.05)
        mouse.press(pynput.mouse.Button.left)
        time.sleep(0.05)
        mouse.release(pynput.mouse.Button.left)
        print("I can see it")
        playsound('snap.wav')
        time.sleep(0.1)


def isCodexReady():
    codex = pyautogui.locateOnScreen('Codex1.png', grayscale=True, confidence=0.8)
    if codex != None: 
        codexPosition[0] = codex[0]
        codexPosition[1] = codex[1]
        print("Codex is ready")
        return True
    else:
        return False
    

def UltiHero(x,y):
    while True:
        #LookForEnemy()
        if pyautogui.locateOnScreen('Ulti-on.png', grayscale=True, confidence=0.8) != None:
            print("I can see it")
            time.sleep(0.5)
        elif pyautogui.locateOnScreen('Ulti-off.png', grayscale=True, confidence=0.8) != None:
            keyboard.press('r')
            keyboard.release('r')
            time.sleep(0.1)
            beforeBotting.append(mouse.position[0])
            beforeBotting.append(mouse.position[1])
            mouse.position = (x,y)
            mouse.press(pynput.mouse.Button.left)
            mouse.release(pynput.mouse.Button.left)
            mouse.position = (beforeBotting[0], beforeBotting[1])
            beforeBotting.pop()
            beforeBotting.pop()
            print("I am unable to see it")
            time.sleep(0.5)


def mainLoop():
    while True:
        if isCodexReady():
            print("I got this far...")
            LookForEnemy()

overlay = overlay.Overlay(
        'yes',
        'Checking for IP address updates...',
        500,
        'fu'
        )
overlay.run()

#mainLoop()