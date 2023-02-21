import pyautogui
import time
import keyboard
import sys

positionLockInX = 0
positionLockInY = 0
positionX = 0
positionY = 0
distaneX = 0
distaneY = 0

def kb():
    while True:
        if keyboard.is_pressed("a"): 
            pos = pyautogui.position()
            global positionX
            global positionY
            positionX = pos.x
            positionY = pos.y
            file1 = open("./points.txt","a")
            text = "initialX = ({})\n".format(positionX) + "initialY = ({})\n".format(positionY)
            file1.write(text)
            time.sleep(1)
            file1.close()
        if keyboard.is_pressed("s"): 
            pos = pyautogui.position()
            global distaneX
            global distaneY
            distaneX = pos.x - positionX
            distaneY = pos.y - positionY
            file1 = open("./points.txt","a")
            text = "distanceX = ({})\n".format(distaneX) + "distanceY = ({})\n".format(distaneY)
            file1.write(text)
            time.sleep(1)
            file1.close()
           
        if keyboard.is_pressed("d"):
            pos = pyautogui.position()
            file1 = open("./points.txt","a")
            text = "Lock In Button PositionX = ({})\n".format(pos.x) + "Lock In Button PositionY = ({})\n".format(pos.y)
            file1.write(text)
            time.sleep(1)
            file1.close()
            
        if keyboard.is_pressed("g"):
            sys.exit()
            
    
if __name__ == "__main__":
    text = open("./points.txt","r")
    filetext = text.read()
    text.close()
    if filetext != "":
        file1 = open("./points.txt","w")
        file1.close()
    kb()

