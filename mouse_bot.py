import pyautogui as pag
import random
import time
import keyboard

pag.FAILSAFE=False

time.sleep(10)

while True:
    x = random.randint(0,1920)
    y = random.randint(0,1080)
    pag.moveTo(x,y,0.2)
    if keyboard.is_pressed("g") & keyboard.is_pressed("o") & keyboard.is_pressed("a") & keyboard.is_pressed("t"):
        break