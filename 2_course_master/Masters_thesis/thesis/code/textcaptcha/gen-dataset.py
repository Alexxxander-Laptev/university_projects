from captcha.image import ImageCaptcha

from random import randint, shuffle
import numpy as np
import os

from textcaptcha.preprocessing_image import preprocessing_image


def generate_image(path_to_file: str, alphabet: list, number_of_start:int, number_of_captcha: int, size_of_image: tuple) -> list:
    # Генерация текстовых captcha
    text = ImageCaptcha(size_of_image[0], size_of_image[1], ['./fonts/arial.ttf', './fonts/comic.ttf', './fonts/cour.ttf', './fonts/georgia.ttf'])
    # Структура возвращаемого списка: [filename, label, (width, height)]
    filenames = []
    for _ in range(number_of_start, number_of_captcha):
        captcha_text = [alphabet[randint(0, len(alphabet) - 1)] for _ in range(randint(4, 7))]
        shuffle(captcha_text)
        text.write(''.join(captcha_text), f'{path_to_file}/{"".join(captcha_text)}.png')
        filenames.append(
            [f'{path_to_file}/{"".join(captcha_text)}.png',
            ''.join(captcha_text)]
        )
    
    return filenames


if __name__ == '__main__':
    # Алфавит допустимых символов
    alphabet = 'ABCDEFGHJKLMNPQRSTWXYZ023456789'
    # Создание директории для хранения полноценных синтетических текстовых captcha
    path_to_dataset = '../datasets/captcha'
    if not os.path.isdir(path_to_dataset):
        os.mkdir(path_to_dataset)
    # Создаем датасет из нужного полноценных синтетических captcha длиной от 4 до 7 символов размером 250х60
    filenames = generate_image(path_to_dataset, list(alphabet), 0, 100000, (250, 60))

    # Предобработка изображений
    preprocessing_image(filenames)

    # Для отладки без создания датасета с нуля
    numpy_data = np.array(filenames, dtype=object)
    np.save('data.npy', numpy_data)
