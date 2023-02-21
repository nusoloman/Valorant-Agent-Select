import pyautogui
import keyboard
import sys
import re

textfile = open("./points.txt", 'r')
filetext = textfile.read()
textfile.close()
positionLockInX = re.findall("PositionX = \(\d+\)", filetext)
positionLockInY = re.findall("PositionY = \(\d+\)", filetext)
distaneX = re.findall("distanceX = \(\d+\)", filetext)
distaneY = re.findall("distanceY = \(\d+\)", filetext)
initialX = re.findall("initialX = \(\d+\)", filetext)
initialY = re.findall("initialY = \(\d+\)", filetext)

positionLockInX = positionLockInX[len(positionLockInX)-1]
positionLockInY = positionLockInY[len(positionLockInY)-1]
distaneX = distaneX[len(distaneX)-1]
distaneY = distaneY[len(distaneY)-1]
initialX = initialX[len(initialX)-1]
initialY = initialY[len(initialY)-1]

positionLockInX = re.findall("\d+", positionLockInX)
positionLockInY = re.findall("\d+", positionLockInY)
distaneX = re.findall("\d+", distaneX)
distaneY = re.findall("\d+", distaneY)
initialX = re.findall("\d+", initialX)
initialY = re.findall("\d+", initialY)

positionLockInX = int(positionLockInX[0])
positionLockInY = int(positionLockInY[0])
distaneX = int(distaneX[0])
distaneY = int(distaneY[0])
initialX = int(initialX[0])
initialY = int(initialY[0]) 


def valo():
  
    while True:
        if keyboard.is_pressed("1"):
            while (True):
                pyautogui.moveTo(initialX,initialY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("2"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*1,initialY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("3"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*2,initialY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("4"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*3,initialY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("5"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*4,initialY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("6"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*5,initialY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("7"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*6,initialY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("8"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*7,initialY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("9"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*8,initialY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("0"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*9,initialY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("q"):
            while (True):
                pyautogui.moveTo(initialX,initialY+distaneY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("w"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*1,initialY+distaneY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("e"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*2,initialY+distaneY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("r"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*3,initialY+distaneY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("t"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*4,initialY+distaneY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("y"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*5,initialY+distaneY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("u"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*6,initialY+distaneY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("ı"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*7,initialY+distaneY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("o"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*8,initialY+distaneY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("p"):
            while (True):
                pyautogui.moveTo(initialX+distaneX*9,initialY+distaneY)
                pyautogui.click()
                pyautogui.moveTo(positionLockInX,positionLockInY)
                pyautogui.click()
                if keyboard.is_pressed("f"):
                    break
        if keyboard.is_pressed("g"):
            sys.exit()
            
if __name__ == "__main__":  
    valo()


























# agents=["./asset/astra.PNG","./asset/breach.PNG","./asset/brimstone.PNG","./asset/chamber.PNG","./asset/cypher.PNG","./asset/fade.PNG","./asset/harbor.PNG","./asset/jett.PNG","./asset/kay-o.PNG","./asset/killjoy.PNG","./asset/neon.PNG","./asset/omen.PNG","./asset/phoenix.PNG","./asset/raze.PNG","./asset/reyna.PNG","./asset/sage.PNG","./asset/skye.PNG","./asset/sova.PNG","./asset/viper.PNG","./asset/yoru.PNG"]

# agentBoxPosition =0
# pyautogui.FAILSAFE = False

# while (pyautogui.position() != agentBoxPosition):
#     agentBox = pyautogui.locateCenterOnScreen(agents[number],confidence=0.6)
#     time.sleep(0.2)
#     if (agentBox != None):
#         agentBoxPosition = agentBox
#     print(agentBox , "agent")
#     print(pyautogui.position() , "look") 
#     pyautogui.moveTo(agentBox)
#     pyautogui.click()
    
# while (pyautogui.position() == agentBoxPosition):
#     lockInAgent = pyautogui.locateCenterOnScreen('./lock-in.PNG',confidence=0.4)
#     print(lockInAgent , "buton")
#     pyautogui.moveTo(lockInAgent)
#     pyautogui.click()

