import pyautogui
import webbrowser as wb
import time

wb.open("https://web.whatsapp.com/")
time.sleep(10)
for i in range(5):
    pyautogui.write("Full Practice")
    pyautogui.press("enter")
