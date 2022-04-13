import pyautogui
from time import sleep

## Esse script é para ser usado em algum momento que vc precisa fazer um pause e sair do pc por alguns instantes
## A automação fica clicando a tecla de espaço infinitamente, fazendo com que não tenha queda dentro do game

def travatecla():
    pyautogui.press(['Space'])
    sleep(5)

def main():
    while True:
        if travatecla():
            sleep(7)
main()