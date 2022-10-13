import cv2 as cv
import numpy as np
import pyautogui as pa
import time
import keyboard

def encontrarImagen():
    imagen = pa.screenshot()
    img_gray = cv.cvtColor(np.array(imagen), cv.COLOR_BGR2GRAY)
    template = cv.imread('image_000.png',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    i = 0
    for pt in zip(*loc[::-1]):
        i += 1
        #pa.moveTo(x=pt[0] + w, y=pt[1] + h)
        #pydirectinput.click()
        pa.moveTo(x=pt[0] + w,y=pt[1] + h)
        pa.mouseDown()
        time.sleep(0.2)
        pa.mouseUp()
        time.sleep(3)
        if(len(loc[0] >= 2)):
            encontrarImagen()
        break
        
    

while True:
    encontrarImagen()
    time.sleep(0.5)
    pa.press('f8')
    time.sleep(0.5)
    if keyboard.is_pressed('p'):
        break
