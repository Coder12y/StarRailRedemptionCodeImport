import time
import pydirectinput as pag
import pyperclip
import win32api

time.sleep(5)
print(pag.position())

with open("123.txt") as f:
    txt=f.readlines()
for i in txt:
    time.sleep(2)
    pag.press("esc")
    time.sleep(1)
    print(pag.position())
    pag.moveTo(3202,139) #...Position
    pag.click()
    time.sleep(0.5)
    pag.moveTo(2946,273) #duihuanma Position
    pag.click()
    pyperclip.copy(i.split()[0])
    pag.moveTo(2185,690) #paste Position
    pag.click()
    time.sleep(3)
    pag.moveTo(1989,909) #confirm Position
    pag.click()