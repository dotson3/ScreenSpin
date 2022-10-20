import gc
import os
import sys
from PIL import Image, ImageGrab
from pytesseract import pytesseract
from time import time, sleep
import pyautogui
from datetime import datetime

sys.setrecursionlimit(10 ** 6)

count = 1
minicount = 0
majorcount = 0
grandcount = 0
highMini = ''
highMajor = ''
highGrand = ''


def screenGrab():
    global highMini
    global highMajor
    global highGrand

    box = (236, 508, 305, 541)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\mini_snap' + '.png', 'PNG')

    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = r'C:\Users\ddots\PycharmProjects\screenSpin/mini_snap.png'
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)

    box1 = (235, 400, 325, 434)
    im1 = ImageGrab.grab(box1)
    im1.save(os.getcwd() + '\\major_snap' + '.png', 'PNG')

    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path1 = r'C:\Users\ddots\PycharmProjects\screenSpin/major_snap.png'
    img = Image.open(image_path1)
    pytesseract.tesseract_cmd = path_to_tesseract
    text1 = pytesseract.image_to_string(img)

    box2 = (235, 300, 342, 333)
    im2 = ImageGrab.grab(box2)
    im2.save(os.getcwd() + '\\Grand_snap' + '.png', 'PNG')

    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path2 = r'C:\Users\ddots\PycharmProjects\screenSpin/Grand_snap.png'
    img = Image.open(image_path2)
    pytesseract.tesseract_cmd = path_to_tesseract
    text2 = pytesseract.image_to_string(img)

    box3 = (960, 115, 1060, 155)
    im3 = ImageGrab.grab(box3)
    im3.save(os.getcwd() + '\\money_snap' + '.png', 'PNG')

    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path3 = r'C:\Users\ddots\PycharmProjects\screenSpin/money_snap.png'
    img = Image.open(image_path3)
    pytesseract.tesseract_cmd = path_to_tesseract
    text3 = pytesseract.image_to_string(img)

    print('Real Money', text3[:-1])
    print('Grand', text2[:-1])
    print("It Hit @", highGrand)
    print('Major', text1[:-1])
    print("It Hit @", highMajor)
    print('Mini ', text[:-1])
    print("It Hit @", highMini)


    if text >= "199.83" and text.startswith('199'):
        print("Mini will hit!")
        pyautogui.click(1150, 660, interval=.2)

        global minicount
        minicount += 1
        screenGrab()
    elif text1 >= "1,999.50" and text1.startswith('1,99'):
        print("Major will hit!")
        pyautogui.click(1150, 660, interval=.2)

        global majorcount
        majorcount += 1
        screenGrab()
    elif text2 >= "49,999.00" and text2.startswith('49,9'):
        print("Grand will hit!")
        pyautogui.click(1150, 660, interval=.2)

        global grandcount
        grandcount += 1
        screenGrab()
    elif text3 <= "1.00" and text3.startswith('1.00'):
        exit("Money is less than $210")

    elif text > highMini and text.startswith('1'):

        highMini = text
        # print(highMini)

    elif text1 > highMajor and text.startswith('1'):
        highMajor = text1
        # //print(highMajor)
    # elif text1 < highMajor and text.startswith('1'):
    #     text_file = open("mjackpot.txt", "w")
    #     text_file.write("major: %s" % highMajor + datetime.now().strftime("%m_%d_%Y--%I_%M_%S_%p") + '\n')
    #     text_file.close()

    elif text2 > highGrand and text.startswith('1'):
        highGrand = text2
        # print(highGrand)


    else:
        global count
        count += 1
        print("hours", count // 3600, "Minutes", count // 60)
        print('attempts mini:', minicount, 'grand:', grandcount, 'major:', majorcount)
        # pyautogui.click(200, 125)
        # pyautogui.click(1025, 675, interval=3.0)

while True:
    sleep(1 - time() % 1)
    # thing to run
    gc.collect()
    screenGrab()
