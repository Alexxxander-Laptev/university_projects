import speech_recognition as sr
import subprocess
import logger
import os


logger = logger.ConfigLogger(__name__)

class AudioCaptchaSolver():
    '''Класс решателя audio captcha'''

    def __init__(self):
        '''Конструктор класса'''
        # Создаем объект распознавателя речи
        self.recognizer = sr.Recognizer()
        # Распознанное текстовое сообщение
        self.text_message = None


    def recognition_audio(self, path_to_audio: str) -> str:
        '''
        Метод распознавания аудиофайла
        Файлы сохраняются в формате mp3 (обычно содержат шум, кроме мест, где слышен голос)
        '''

        # Преобразование mp3 файла в формат, который подходит для распознавания
        mp3_file = path_to_audio
        wav_file = './audio/audiocaptcha.wav'

        if os.name == 'nt':
            subprocess.run(['C:/ffmpeg/bin/ffmpeg.exe', '-i', mp3_file, wav_file])
        else:
            subprocess.run(['ffmpeg', '-i', mp3_file, wav_file])
        
        try:
            # Загружаем аудио файл
            audio_captcha = sr.AudioFile(wav_file)

            # Распознаем речь из аудио файла
            with audio_captcha as voice:
                audio_data = self.recognizer.record(voice)
                text_message = self.recognizer.recognize_google(audio_data, language='en-US')
            logger.log_info('Распознавание речи завершено успешно!')
        except Exception as e:
            logger.log_warning(f'Распознавание завершилось с ошибкой: {e}')
        
        if text_message:
            self.text_message = text_message
            os.remove(mp3_file)
            os.remove(wav_file)
        
        return self.text_message
