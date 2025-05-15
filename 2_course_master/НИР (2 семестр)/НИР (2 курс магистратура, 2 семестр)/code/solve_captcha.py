# Подключение библиотек для работы с браузером
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver  
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

# Подключение библиотек для работы с текстом заданиия captcha
from deep_translator import GoogleTranslator
import inflect

# Библиотека для парсинга HTML
from bs4 import BeautifulSoup

# Библиотека для работы с изображениями
from ultralytics import YOLO
import cv2
import numpy as np

from random import randint
import time
import requests


class SolveCaptcha():
    '''
    Основной класс проекта, который управляет вызовом дочерних классов для решения определенных видов captcha
    На начальном этапе здесь также будет все, что касатеся получения captcha с веб-страницы
    '''

    def __init__(self, browser: WebDriver):
        '''Конструктор класса'''
        super().__init__()
        self.browser = browser


    def find_captcha(self, link: str):
        # Проходим по ссылке
        self.browser.get(link)
        time.sleep(randint(3, 5))

        # Переключаемся на фрейм с чекбоксом captcha
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, '//*[@id="g-recaptcha"]/div/div/iframe'))
        # Кликаем по чекбоксу "Я не робот"
        self.browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div/span').click()
        time.sleep(randint(3, 5))
        
        # Переключаемся на обычную web-страницу
        self.browser.switch_to.default_content()
        # Переключаемся на фрейм с картинкой captcha
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, '/html/body/div[2]/div[4]/iframe'))


    def get_captcha(self) -> tuple[str, str, str, np.ndarray]:
        '''Метод получения captcha со страницы'''
        # Находим элемент, содержащий ссылку на исходное изображение
        src_image = self.browser.find_element(By.XPATH, '//*[@id="rc-imageselect-target"]/table/tbody/tr[1]/td[1]/div/div[1]/img').get_attribute('src')
        # Делаем запрос для получения файла
        response = requests.get(src_image)
        response.raise_for_status()

        # Получаем название объекта, который надо найти
        object_name = self.browser.find_element(By.XPATH, '//*[@id="rc-imageselect"]/div[2]/div[1]/div[1]/div/strong').text

        # Получаем таблицу с кусочками изображения
        table = self.browser.find_element(By.XPATH, '//*[@id="rc-imageselect-target"]/table').get_attribute('outerHTML')

        # Преобразование байтовой последовательности в изображение
        image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)

        return object_name, table, src_image, image
    

    def get_properties_for_recognition(self, task_object: str, table: str) -> tuple[str, int, int]:
        '''Метод для получения необходимых параметров для распознавания на картинке'''
        # Перевод названия объекта на английский и сохранение его в единственном числе
        task_object = GoogleTranslator(source='auto', target='en').translate(task_object)
        singular = inflect.engine()
        if len(task_object) > 3:
            # Исключаем ошибки с множественным числом для слов, которые не могут быть во множественном числе из-за малого количества символов
            task_object = singular.singular_noun(task_object)
            if task_object.lower() == 'hydrant':
                task_object = 'fire hydrant'

        # Парсинг HTML
        soup = BeautifulSoup(table, 'lxml')
        # Получаем количество строк
        number_of_rows = len(soup.find_all('tr'))
        # Получаем количество столбцов
        number_of_columns = len(soup.find('tr').find_all(['td', 'th']))

        return task_object, number_of_rows, number_of_columns
    

    def predict_class(self, image: np.ndarray, task_object: str) -> list:
        '''Метод для получения масок для изображения с необходимым классом'''
        # Передаем в предобученную модель изображение для поиска нужного объекта
        results = model(image)[0]
        class_names = model.names

        # Получаем идентификатор нужного класса
        for id, name in class_names.items():
            if name == task_object.lower():
                class_id = id
                break

        # Получаем все маски для классов
        masks = results.masks.data.cpu().numpy()
        classes = results.boxes.cls.cpu().numpy()

        # Получаем список масок для нужного класса
        selected_masks = [masks[i] for i in range(len(classes)) if int(classes[i]) == class_id]

        return selected_masks
    

    def get_cells_with_mask(self, cells_with_object: list, coords_cells: list, mask: np.ndarray, grid_size: tuple, threshold: float) -> list:
        '''Метод для получения ячеек таблицы, содержащих объект'''
        # Определяем размер ячейки
        cell_height, cell_width = int(mask.shape[0] / grid_size[0]), int(mask.shape[1] / grid_size[1])
        idx_cell = 0

        for i in range(grid_size[0]):
            for j in range(grid_size[1]):
                # Координаты прямоугольника, соответствующего ячейке
                y1, y2 = i * cell_height, (i + 1) * cell_height
                x1, x2 = j * cell_width, (j + 1) * cell_width

                # Вырезаем часть маски, соответствующую ячейке
                cell_mask = mask[y1:y2, x1:x2]
                # Рассчитываем какую часть ячейки занимает объект
                coverage_area = np.sum(cell_mask) / cell_mask.size

                # Проверяем, есть ли объект в ячейке
                if coverage_area >= threshold:
                    # Сохраняем данные о ячейке
                    cells_with_object.append(idx_cell)
                    coords_cells.append((i, j))

                idx_cell += 1
        
        return cells_with_object, coords_cells


if __name__ == "__main__":
    # Загружаем модель
    model = YOLO('best.pt')

    # Целевой сайт
    target_link = 'https://rucaptcha.com/demo/recaptcha-v2'

    # Настройки user agent
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    options = webdriver.ChromeOptions()
    
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument(f"user-agent={USER_AGENT}")
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Передача параметров
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(30)

    captcha = SolveCaptcha(browser)
    # Находим фрейм с captcha (автоматизация клика на чекбокс)
    captcha.find_captcha(target_link)

    # Выполняем распознавание до тех пор, пока фрейм не исчезнет
    while True:
        try:
            # Получение изображения captcha и объекта для поиска
            task_object, table, src_image, image = captcha.get_captcha()
            # Полчаем необходимые параметры captcha
            task_object, rows, columns = captcha.get_properties_for_recognition(task_object, table)

            RECURSIVE_CAPTCHA = True    # Флаг для captcha, в которых вместо выбранных изображений появляются новые 
            while RECURSIVE_CAPTCHA:
                # Сбрасываем флаг рекурсии
                RECURSIVE_CAPTCHA = False
                # Находим нужный класс на изображении
                selected_masks = captcha.predict_class(image, task_object)
                
                cells_with_object, coords = [], []
                for mask in selected_masks:
                    # Проходим по выбранным маскам для определения клетки к которой она принадлежит
                    resized_mask = cv2.resize(mask, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_NEAREST)
                    cells_with_object, coords = captcha.get_cells_with_mask(cells_with_object, coords, resized_mask, (rows, columns), 0.05)
                
                # Кликаем по ячейкам с уникальными индексами
                for cell, coord in list(set(zip(cells_with_object, coords))):
                    captcha.browser.find_elements(By.TAG_NAME, 'td')[cell].click()
                    time.sleep(randint(2, 3))
                    # Проверяем наличие новых изображений в данной ячейке
                    src_cell = captcha.browser.find_elements(By.TAG_NAME, 'td')[cell].find_element(By.TAG_NAME, 'img').get_attribute('src')
                    if src_cell != src_image:
                        # Делаем запрос для получения изображения
                        response = requests.get(src_cell)
                        response.raise_for_status()
                        cell_image = cv2.imdecode(
                            np.frombuffer(response.content, np.uint8),
                            cv2.IMREAD_COLOR
                        )
                        
                        # Заменяем в исходном изображении старую ячейку на новую
                        x1, x2 = coord[0] * cell_image.shape[0], (coord[0] + 1) * cell_image.shape[0]
                        y1, y2 = coord[1] * cell_image.shape[1], (coord[1] + 1) * cell_image.shape[1]
                        image[x1:x2, y1:y2] = cell_image

                        # Устанавливаем флаг рекурсии
                        RECURSIVE_CAPTCHA = True

            # Находим кнопку подтверждения выбора и кликаем по ней
            captcha.browser.find_element(By.XPATH, '//*[@id="recaptcha-verify-button"]').click()
            time.sleep(randint(3, 5))
        except ElementClickInterceptedException:
            captcha.browser.quit()
            break
            