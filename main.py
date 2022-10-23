from pytesseract import image_to_string, pytesseract
from os import listdir, getcwd, path
# from PIL import Image, ImageGrab
import cv2
# import matplotlib.pyplot as plt


pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def main():
    """
    dir = listdir(input('Type directory name'))
    coords = [0, 0, 100, 100]
    for filename in dir:
        if filename[::-1].split('.')[0].lower().replace('e', '') == 'jpg':
            image = Image.open(path.join(getcwd(), filename))
        print('Incorrect file type')
    """
    '''mg = Image.open('5-6_2022-23-1exp.jpg')
    img = img.crop((1590, 3100, 2300, 3242))
    img = ImageGrab.grab((0, 0, 1000, 1000))
    img.show()'''
    img = cv2.imread('5-6_2022-23-1exp_copy.jpg')
    cropped = img[3100:3242, 1590:2300]
    cv2.imshow("cropped", cropped)
    cv2.waitKey(0)
    string = image_to_string(cropped, lang='rus')
    print(string)


if __name__ == '__main__':
    main()
