from pyautogui import *
import pyautogui
from time import sleep
import mouse
import pygetwindow


##As coordenadas foram feitas na resolução 1920x1080 no monitor da esquerda, caso a resolução do seu monitor for diferente devera alterar os valores do eixo X e Y

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()


def check_comecar():
    comecar = pyautogui.locateOnScreen('PickGame\\ImageValorant\\comecar.png', confidence=0.5)

    if comecar != None:
        click(x=912, y=989) #confirmar
        return True
    return False

def check_agente():
    agentes = pyautogui.locateOnScreen('PickGame\\ImageValorant\\confirmar_blocked.png', confidence=0.5)

    if agentes != None:

       # pyautogui.hotkey('winleft')
       # sleep(1)

        #primeira coluna

        #mouse.move(x=1225, y=925, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #click aleatorio
        carlinhos = "VALORANT"; carlinho = pygetwindow.getWindowsWithTitle(carlinhos)[0]; carlinho.activate()

        sleep(1)
        mouse.move(x=1209, y=917, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Killjoy
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=1283, y=917, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Neon
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=1122, y=917, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #KAY/O
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=705, y=1000, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Phoenix
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=956, y=1000, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Sage
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar
        return True
    return False

def main():
    while True:
        if check_comecar() or check_agente():
            sleep(7)
main()


"""
        mouse.move(x=704, y=917, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Breach
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=789, y=917, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Brimstone
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=873, y=917, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Chamber
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=957, y=917, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Cypher
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=1041, y=917, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Jett
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=1122, y=917, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #KAY/O
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=1209, y=917, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Killjoy
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=1283, y=917, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Neon
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        #segunda coluna

        mouse.move(x=620, y=1000, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Omen
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=705, y=1000, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Phoenix
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=785, y=1000, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Raze
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=871, y=1000, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Reyna
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=956, y=1000, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Sage
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=1040, y=1000, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Skye
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=1119, y=1000, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Sova
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=1210, y=1000, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Viper
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar

        mouse.move(x=1292, y=1000, duration=0.200);  sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #Yoru
        mouse.move(x=966, y=808, duration=0.200);   sleep(1); pyautogui.mouseDown(); pyautogui.mouseUp() #confirmar
"""