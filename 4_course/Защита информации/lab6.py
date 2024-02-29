from stegano import lsb
import hashlib
from PIL import Image


'''
Задачи:
1.Примените LSB к одному из изображений из вашей Модели угроз, предварительно сохранив его в удобном формате.
2.Продемонстрируйте в отчёте работоспособность выбранного способа реализации LSB (скриншоты и описание к ним).
3.Используя одну из рассмотренных хэш-функций, показать различие или совпадение хэшей двух изображений.
'''


def lsb_coder():
    # Применение метода LSB
    input_text = "Hello World! It`s test LSB method."
    encode_text = lsb.hide(Image.open("lab6.png"), input_text)
    encode_text.save("outlab6.png")


def hash_check():
    # Сравнение хэшей
    md5_result_input = hashlib.md5(Image.open("lab6.png").tobytes())
    print('Хэш исходного файла:\t', md5_result_input.hexdigest())
        
    md5_result_output = hashlib.md5(Image.open("outlab6.png").tobytes())
    print('Хэш зашифрованного файла:\t', md5_result_output.hexdigest())


if __name__ == '__main__':
    print("1. Применение LSB к изображению.")
    print("2. Сравнение хэшей двух изображений.")
    variant = int(input("Введите вариант работы программы: "))
    while variant < 1 or variant > 2:
        variant = int(input("Введите вариант работы программы: "))

    if variant == 1:
        lsb_coder()
    elif variant == 2:
        hash_check()
