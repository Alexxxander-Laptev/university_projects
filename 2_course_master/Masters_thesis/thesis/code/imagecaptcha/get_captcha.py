# Подключение библиотек для работы с браузером
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver  
from selenium.webdriver.common.by import By

# Подключение библиотек для работы с текстом заданиия captcha
from deep_translator import GoogleTranslator
import inflect

# Библиотека для парсинга HTML
from bs4 import BeautifulSoup

from random import randint
import time
import requests
import os
import csv


class GetCaptcha():
    '''
    Основной класс проекта, который управляет вызовом дочерних классов для решения определенных видов captcha
    На начальном этапе здесь также будет все, что касатеся получения captcha с веб-страницы
    '''

    def __init__(self, browser: WebDriver):
        '''Конструктор класса'''
        super().__init__()
        self.browser = browser


    def get_captcha(self, link: str, cnt: int) -> tuple[str, str, str]:
        '''Метод получения captcha со страницы'''
        # Проходим по ссылке
        self.browser.get(link)
        time.sleep(randint(3, 5))

        # Переключаемся на фрейм с чекбоксом captcha
        self.browser.switch_to.frame(self.browser.find_element(
            By.XPATH,
            '//*[@id="g-recaptcha"]/div/div/iframe'
        ))
        # Кликаем по чекбоксу "Я не робот"
        self.browser.find_element(
            By.XPATH,
            '/html/body/div[2]/div[3]/div[1]/div/div/span'
        ).click()
        time.sleep(randint(3, 5))
        
        # Переключаемся на обычную web-страницу
        self.browser.switch_to.default_content()
        # Переключаемся на фрейм с картинкой captcha
        self.browser.switch_to.frame(self.browser.find_element(
            By.XPATH,
            '/html/body/div[2]/div[4]/iframe'
        ))
        # Находим элемент, содержащий ссылку на исходное изображение
        image = self.browser.find_element(
            By.XPATH,
            '//*[@id="rc-imageselect-target"]/table/tbody'+
            '/tr[1]/td[1]/div/div[1]/img'
        ).get_attribute('src')
        # Делаем запрос для получения файла
        response = requests.get(image)
        response.raise_for_status()

        # Получаем название объекта, который надо найти
        object_name = self.browser.find_element(
            By.XPATH,
            '//*[@id="rc-imageselect"]/div[2]/div[1]/div[1]'+
            '/div/strong'
        ).text

        # Получаем таблицу с кусочками изображения
        table = self.browser.find_element(
            By.XPATH,
            '//*[@id="rc-imageselect-target"]/table'
        ).get_attribute('outerHTML')

        # Создаем папку для хранения временных файлов
        if not os.path.isdir('../datasets/imagecaptcha_dataset'):
            os.mkdir('../datasets/imagecaptcha_dataset')
        path_to_file = f'../datasets/imagecaptcha_dataset/{cnt}.jpg'
        # Сохраняем файл
        with open(f'{path_to_file}', 'wb') as imageCaptcha:
            imageCaptcha.write(response.content)

        return object_name, path_to_file, table
    

    def get_number_of_cells(self, table:str) -> tuple[int, int]:
        '''Метод для получения колличества ячеек таблицы для последующего разбиения изображения на части'''
        # Парсинг HTML
        soup = BeautifulSoup(table, 'lxml')

        # Получаем количество строк
        number_of_rows = len(soup.find_all('tr'))

        # Получаем количество столбцов
        number_of_columns = len(soup.find('tr').find_all(['td', 'th']))
        
        return number_of_rows, number_of_columns


if __name__ == "__main__":
    # Целевой сайт
    target_link = 'https://rucaptcha.com/demo/recaptcha-v2'
    for cnt in range(463, 638):
        # Настройки user agent
        USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
        options = webdriver.ChromeOptions()
        
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument(f"user-agent={USER_AGENT}")
        options.add_argument(
            "--disable-blink-features=AutomationControlled"
        )

        # Передача параметров
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(30)

        captcha = GetCaptcha(browser)
        # Получение captcha и объекта для поиска
        task_object, image, table = captcha.get_captcha(target_link, cnt)

        # Перевод названия объекта на английский и сохранение его в единственном числе
        task_object = GoogleTranslator(source='auto', target='en').translate(task_object)
        singular = inflect.engine()
        if len(task_object) > 3:
            # Исключаем ошибки с множественным числом для слов, которые не могут быть во множественном числе из-за малого количества символов
            task_object = singular.singular_noun(task_object)
            if task_object.lower() == 'hydrant':
                task_object = 'fire hydrant'

        # Получаем количество ячеек
        rows, columns = captcha.get_number_of_cells(table)

        # Запись полученных параметров в csv-файл
        with open('images_for_captcha.csv', 'a') as datasetFile:
            csv_rows = csv.writer(datasetFile, quoting=csv.QUOTE_NONE)
            csv_rows.writerow([task_object, image, rows, columns])
