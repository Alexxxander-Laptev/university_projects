import sys
import numpy as np
from PIL import Image
import random

def create_img():
    """
    Функция считывает файл и добавляет линии.
    """
    image = Image.open('example-1024.png')
    img_array = np.array(image)
    for x in range(0, img_array.shape[0]):
        for y in range(0, img_array.shape[1]):
            img_array[x,y] = 255
            if (y == 0 or y == 127 or y == 255 or y == 383 or y == 511 or y == 511 or y == 639 or y == 767 or y == 895 or y == 1023):
                img_array[x,y] = 0
    # Convert NumPy array back to Pillow image
    img = Image.fromarray(img_array)
    # Save image with Pillow
    img.save('newexample-1024.png')

def randdir():
    """
    Функция randdir выдаёт распределение Гауса в 3 сигма от нуля.
    """
    result = round(random.gauss(0,5/3))
    if (result >= 5):
        result = 5
    elif (result <= -5):
        result = -5
    else:
        return result
    return result

def noise_img(filename):
    """
    Функция считывает данные из png файла и добавляет шум в новый png файл.
    """
    loadfilename = filename + '.png'
    image = Image.open(loadfilename)
    img_array = np.array(image)
    for y in range(0, img_array.shape[0]):
        for x in range(0, img_array.shape[1]):
            if(img_array[y,x] != 255):
                k = randdir()
                # k = 3
                i = 1
                while ((x + i < img_array.shape[1]) and (img_array[y,x+i] != 255)):
                    i = i + 1
                    if k < 0:
                        for j in range(0,i):
                            img_array[y,x+j+k] = img_array[y,x+j]
                            img_array[y,x+j] = 255
                    elif k > 0:
                        for j in range(i-1,-1):
                            img_array[y,x+j+k] = img_array[y,x+j]
                            img_array[y,x+j] = 255
                    else:
                        z = 1
    savefilename = filename + "-noise.png"
    img = Image.fromarray(img_array)
    img.save(savefilename)

if __name__ == "__main__":
    """
    В программе реализована создание линий и добавление шума.
    """
    numberxls = sys.argv[1:]
    if sys.argv[1] == 'LaptevAV':
        print('LaptevAV - вывод данного сообщения.')
        print('png - обработка файла: python3 add-noise-to-png.py *.png')
    else:
        for i in range(1, len(numberxls) + 1):
            print('Обработка файла', sys.argv[i])
            LaptevAV = sys.argv[i]
            if LaptevAV == "Error":
                print('Ошибка обработки', sys.argv[i])
                continue
            elif sys.argv[i] == "create":
                print('Создание линий в файле filename', LaptevAV, LaptevAV.split('.'))
                create_img()
            else:
                print('filename', LaptevAV, LaptevAV.split('.'))
                LaptevAV = LaptevAV.split('.')
                LaptevAV = LaptevAV[0]
                noise_img(LaptevAV)