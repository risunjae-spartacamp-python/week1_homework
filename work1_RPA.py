import pyautogui
import webbrowser
import time
import pyperclip

# while True:
#     x, y = pyautogui.position()
#     positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
#     print(positionStr, end="")
#     print("\b" * len(positionStr), end="", flush=True)
webbrowser.open("https://www.google.com/")
pyautogui.click(x=520, y=-290)
time.sleep(0.5)
pyperclip.copy("平泉町　観光")
pyautogui.hotkey("command", "v")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(1)
pyautogui.screenshot("screenshot.png")
time.sleep(1)
