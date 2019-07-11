from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Cordinates():
    replayBtn = (340,390)#Coordenada do botão de reiniciar 300,389
    dinoLimity = (170,420)#Coordenada Limite do Dino 192,421
    #x= 100 y=415

#Reiniciar o Jogo
def restartGame():
    pyautogui.click(Cordinates.replayBtn)#Açãode Click

#Pressionar o Espaço
def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('space')

def imageGrab():
    box = (Cordinates.dinoLimity[0]+60,Cordinates.dinoLimity[1], Cordinates. dinoLimity[0]+100,Cordinates.dinoLimity[1]+30)
    #verifica se existe uma 'Imagem' nessa coordenada
    #coordDinoX, coordDinoY, CoordLimtyX, CoordLimityY
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    if a.sum()!= 1447:
     print(a.sum())

    return a.sum()
#while True:
#  imageGrab()

def main():

    restartGame()
    while True:
     if(imageGrab()!= 1447):
        pressSpace()
        time.sleep(0.1)
main()