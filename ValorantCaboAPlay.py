from pyautogui import *
import pyautogui
from time import sleep

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()


def check_screen():
    vitoria = pyautogui.locateOnScreen('Game\\ImageValorant\\Vitoria.png', confidence=0.5)
    derrota = pyautogui.locateOnScreen('Game\\ImageValorant\\Derrota.png', confidence=0.5)

    if vitoria or derrota != None:
        pyautogui.press('Enter')
        pyautogui.typewrite('/all @twitch.tv/SalamandraLw Da um salve na Twitch :)')
        pyautogui.press('Enter')
        sleep(4)
        return True
    return False

def main():
    while True:
        if check_screen():
            sleep(4)
main()
