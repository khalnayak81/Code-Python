#Program to send same msg multiple times.
import pyautogui as gui
import time 

msg = input("Enter the message  " )
num = input("Enter the num: ")

time.sleep(5)


for i in range(int(num)):
    gui.typewrite(msg)
    gui.press('Enter')
    
    
   