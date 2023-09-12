import sys

import PIL.ImageDraw
import easyocr
from PIL import Image
from datetime import datetime
import os


reader = easyocr.Reader(['en', 'ru'], gpu=True)


def read_from_file(fp):
    img = Image.open(fp)
    coords = img.width // 2, 0.9 * img.height, img.width, img.height
    # PIL.ImageDraw.Draw(img).line(([*coords, coords[0]]))

    cropped_img = img.crop(coords)
    fp = f'cropped{datetime.now()}.{img.format}'
    cropped_img.save(fp)
    bounds = reader.readtext(fp)
    os.remove(fp)
    arr = []
    for bound in bounds:
        print(bound)
        arr.append(bound[1])
    new_arr = []
    for item in arr:
        new_item = ''
        for sym in item:
            if sym.isnumeric():
                new_item += sym
        new_arr.append(new_item)
    # print(new_arr)

    result = '|'.join(new_arr)
    # result = map(int, filter(lambda el: el.isnumeric(), sum(map(lambda b: b[1], bounds)).split()))
    return result


def main():
    fp = 'data/word.jpg'
    print(read_from_file(fp))


if __name__ == '__main__':
    main()
