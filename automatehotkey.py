# Importa os módulos executáveis do script
from pyautogui import *
import pyautogui
from time import sleep
import mouse
import pygetwindow
import webbrowser

# Abre o link do Microsoft Teams
webbrowser.open('https://encurtador.com.br/gowD5')
sleep(3)

# Define onde o mouse vai clickar na tela baseado na imagem que o script reconhecer
def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

sleep(2)

def check_barrasup():
    barrasup = pyautogui.locateOnScreen('C:\\Users\\Usuario1\\Desktop\\Luan\\Teams\\images\\barrasuperior.png', confidence=0.5)

    if barrasup != None:
        click(x=797, y=977)
        sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        sleep(1)
        pyautogui.press('enter')
        return True
    return False


def main():
    while True:
        if check_barrasup():
            sleep(2000)


main()
