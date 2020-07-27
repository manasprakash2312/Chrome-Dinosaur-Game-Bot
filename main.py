import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key='up'):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(300, 415):
            for j in range(600, 650):
                if data[i, j] > 100:
                    return True
    return False

if __name__ == "__main__":
    print('Game about to start in 3 seconds')
    time.sleep(4)

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            hit('up')

        # image.show()