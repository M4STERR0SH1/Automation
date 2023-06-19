import pyautogui

while True:
    current_pos = pyautogui.position()

    print(f"X: {current_pos.x}, Y: {current_pos.y}")
