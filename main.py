import pyautogui
import keyboard
import sys
import re

#   0 - astra               10 - neon
#   1 - breach              11 - omen
#   2 - brimstone           12 - phoenix
#   3 - chamber             13 - raze
#   4 - cyhper              14 - reyna
#   5 - fade                15 - sage
#   6 - harbor              16 - skye
#   7 - jett                17 - sova
#   8 - kay-o               18 - viper
#   9 - killjoy             19 - yoru

textfile = open("./points.txt", 'r')
filetext = textfile.read()
textfile.close()
positionLockInX = re.findall("PositionX = \(\d+\)", filetext)
positionLockInY = re.findall("PositionY = \(\d+\)", filetext)
distaneX = re.findall("distanceX = \(\d+\)", filetext)
distaneY  = re.findall("distanceY = \(\d+\)", filetext)
initialX = re.findall("initialX = \(\d+\)", filetext)
initialY = re.findall("initialY = \(\d+\)", filetext)

positionLockInX =positionLockInX[len(positionLockInX)-1]
positionLockInY =positionLockInY[len(positionLockInY)-1]
distaneX =distaneX[len(distaneX)-1]
distaneY =distaneY[len(distaneY)-1]
initialX = initialX[len(initialX)-1]
initialY = initialY[len(initialY)-1]

positionLockInX = re.findall("\d+", positionLockInX)
positionLockInY = re.findall("\d+", positionLockInY)
distaneX = re.findall("\d+", distaneX)
distaneY  = re.findall("\d+", distaneY)
initialX = re.findall("\d+", initialX)
initialY = re.findall("\d+", initialY)

positionLockInX = int(positionLockInX[0])
positionLockInY = int(positionLockInY[0])
distaneX = int(distaneX[0])
distaneY = int(distaneY[0])
initialX = int(initialX[0])
initialY = int(initialY[0]) 

def kb():

    while True:
        if keyboard.is_pressed("1"):
            pyautogui.moveTo(initialX,initialY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("2"):
            pyautogui.moveTo(initialX+distaneX*1,initialY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("3"):
            pyautogui.moveTo(initialX+distaneX*2,initialY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("4"):
            pyautogui.moveTo(initialX+distaneX*3,initialY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("5"):
            pyautogui.moveTo(initialX+distaneX*4,initialY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("6"):
            pyautogui.moveTo(initialX+distaneX*5,initialY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("7"):
            pyautogui.moveTo(initialX+distaneX*6,initialY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("8"):
            pyautogui.moveTo(initialX+distaneX*7,initialY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("9"):
            pyautogui.moveTo(initialX+distaneX*8,initialY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("0"):
            pyautogui.moveTo(initialX+distaneX*9,initialY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("q"):
            pyautogui.moveTo(initialX,initialY+distaneY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("w"):
            pyautogui.moveTo(initialX+distaneX*1,initialY+distaneY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("e"):
            pyautogui.moveTo(initialX+distaneX*2,initialY+distaneY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("r"):
            pyautogui.moveTo(initialX+distaneX*3,initialY+distaneY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("t"):
            pyautogui.moveTo(initialX+distaneX*4,initialY+distaneY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("y"):
            pyautogui.moveTo(initialX+distaneX*5,initialY+distaneY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("u"):
            pyautogui.moveTo(initialX+distaneX*6,initialY+distaneY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("ı"):
            pyautogui.moveTo(initialX+distaneX*7,initialY+distaneY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("o"):
            pyautogui.moveTo(initialX+distaneX*8,initialY+distaneY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("p"):
            pyautogui.moveTo(initialX+distaneX*9,initialY+distaneY)
            pyautogui.click()
            pyautogui.moveTo(positionLockInX,positionLockInY)
            pyautogui.click()
        if keyboard.is_pressed("f"):
            sys.exit()
            
if __name__ == "__main__":  
    kb()


























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

