import cv2
import numpy as np


def preprocessing_image(list_filenames: list):
    '''Функция для предобработки изображений или изображения для предсказания'''
    # Предобработка изображений с CAPTCHA
    for file in list_filenames:
        # Открытие изображения в градациях серого
        gray_image = cv2.imread(file[0], 0)
        # Приведение всех изображений к одному размеру ширина х высота)
        resized_image = cv2.resize(gray_image, (250, 60))

        # Морфологический фильтр (дилатация) для сужения символов и более четкого отделения их друг от друга
        morph_kernel = np.ones((3, 3))
        dilatation_image = cv2.dilate(resized_image, kernel=morph_kernel, iterations=1)

        # Применяем пороговую обработку, чтобы получить только черные и белые пиксели
        _, thresholder = cv2.threshold(
            dilatation_image,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        cv2.imwrite(file[0], thresholder)
