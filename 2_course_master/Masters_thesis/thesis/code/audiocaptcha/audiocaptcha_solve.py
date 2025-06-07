'''Это основной файл проекта, в котором будут вызываться классы и методы для решения всех популярных видов captcha'''
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver  
from selenium.webdriver.common.by import By

from random import randint
import time
import requests
import os

from audiocaptcha import AudioCaptchaSolver


class MainWorker():
    '''
    Основной класс проекта, который управляет вызовом дочерних классов для решения определенных видов captcha
    На начальном этапе здесь также будет все, что касатеся получения captcha с веб-страницы
    '''

    def __init__(self, browser: WebDriver):
        '''Конструктор класса'''
        super().__init__()
        self.browser = browser


    def get_captcha(self, link: str) -> str:
        '''Метод получения captcha со страницы'''
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
        # Кликаем на кнопку для перехода к audiocaptcha
        self.browser.find_element(By.XPATH, '//*[@id="recaptcha-audio-button"]').click()
        time.sleep(randint(3, 5))
        
        # Переключаемся на обычную web-страницу
        self.browser.switch_to.default_content()
        # Переключаемся на фрейм с айдиозаписью
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, '/html/body/div[2]/div[4]/iframe'))
        # Находим элемент, содержащий ссылку на аудиозапись
        audio = self.browser.find_element(By.XPATH, '//*[@id="audio-source"]').get_attribute('src')
        # Делаем запрос для получения файла
        response = requests.get(audio)
        response.raise_for_status()

        # Создаем папку для хранения временных файлов
        if not os.path.isdir('./audio'):
            os.mkdir('./audio')
        path_to_file = './audio/audiocaptcha.mp3'
        # Сохраняем файл
        with open(f'{path_to_file}', 'wb') as audioCaptcha:
            audioCaptcha.write(response.content)

        return path_to_file


    def paste_response(self, response_message):
        '''Метод для вставки результата распознавания'''
        browser.find_element(By.XPATH, '//*[@id="audio-response"]').send_keys(f'{response_message}')
        time.sleep(randint(3, 5))
        browser.find_element(By.XPATH, '//*[@id="recaptcha-verify-button"]').click()


if __name__ == '__main__':
    '''Запуск программы'''
    list_of_links = [
        'https://rucaptcha.com/demo/recaptcha-v2',
        'https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=low',
        'https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=middle',
        'https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high',
        'https://lessons.zennolab.com/captchas/recaptcha/v2_nosubmit.php?level=low',
        'https://lessons.zennolab.com/captchas/recaptcha/v2_nosubmit.php?level=middle',
        'https://lessons.zennolab.com/captchas/recaptcha/v2_nosubmit.php?level=high',
        'https://lessons.zennolab.com/ru/advanced'
    ]

    for link in list_of_links:
        # Настройки user agent
        USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"

        select_browser = randint(1, 10)

        # Выбор браузера и опций характерных для него
        if select_browser < 5:
            options = webdriver.ChromeOptions()
        else:
            options = webdriver.EdgeOptions()
        
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument(f"user-agent={USER_AGENT}")
        options.add_argument("--disable-blink-features=AutomationControlled")

        # Передача параметров
        if select_browser < 5:
            browser = webdriver.Chrome(options=options)
        else:
            browser = webdriver.Edge(options=options)
        browser.implicitly_wait(30)

        # Cоздаем аудиофайл по указанному пути с captcha
        solver = MainWorker(browser)
        path_to_audio = solver.get_captcha(link)

        # Запускаем распознавание
        captcha_solver = AudioCaptchaSolver()
        response = captcha_solver.recognition_audio(path_to_audio)

        # Вставляем результат распознавания в поле ввода
        solver.paste_response(response)
        time.sleep(randint(10, 15))
