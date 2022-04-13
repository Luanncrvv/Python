from pyautogui import *
import pyautogui
from time import sleep
import keyboard

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def mute():
    if keyboard.read_key() == "page up":
        pyautogui.keyDown('F3')
        return True
    return False

def desmute():
    if keyboard.read_key() == "page down":
        pyautogui.keyDown('V')
        return True
    return False

def main():
    while True:
        if mute() or desmute():
            sleep(3)
main()