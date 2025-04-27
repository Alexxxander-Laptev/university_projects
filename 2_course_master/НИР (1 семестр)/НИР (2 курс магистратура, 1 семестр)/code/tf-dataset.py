import pandas as pd
import tensorflow as tf
from keras._tf_keras.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split


def parse_data(image_path: list, encoder_labels: list, decoder_labels: list) -> tuple[tf.Tensor, list]:
    '''Функция для склеивания изображений и лейблов для датасета'''
    image = tf.io.read_file(image_path)
    image = tf.image.decode_png(image, channels=1)
    image = tf.cast(image, tf.float32) / 255.0

    return (image, encoder_labels), decoder_labels


def create_dataset(images: list, encoder_labels: list, decoder_labels: list, shuffle = True, batch_size = 32) -> tf.data.Dataset:
    '''Функция для создания датасета, понятного для TensorFlow'''
    dataset = tf.data.Dataset.from_tensor_slices((images, encoder_labels, decoder_labels))
    dataset = dataset.map(lambda x, y, w: parse_data(x, y, w))
    if shuffle == True:
        dataset = dataset.shuffle(len(images)).batch(batch_size)
    else:
        dataset = dataset.batch(batch_size)

    return dataset


def create_dataframe(images: list) -> pd.DataFrame:
    '''Функция для создания датафреймов на основе списков'''

    # Создание файла с лейблами о содержимом изображений с CAPTCHA
    filenames = [objects[0] for objects in images]
    list_labels = [objects[1] for objects in images]

    # Создание DataFrame для сохранения соотвествия между путями, лейблами и размерами для каждого элемента датасета
    data = {
        'filename': filenames,
        'label': list_labels,
    }

    return pd.DataFrame(data)


def preparing_dataset(dataframe: pd.DataFrame, alphabet: str, shuffle = True) -> tuple[
        tuple[tf.data.Dataset, tf.data.Dataset, tf.data.Dataset, list],
        tuple[tf.data.Dataset, tf.data.Dataset, tf.data.Dataset, list]
    ]:
    '''Подготовка датасета'''
    
    # Сохранение отдельных составляющих DataFrame
    X_captcha, y_captcha = dataframe['filename'].tolist(), dataframe['label'].tolist()
    
    dict_alphabet = {alphabet[i]:i for i in range(len(alphabet))}
    start_token = len(alphabet)  # Индекс токена <start>
    end_token = len(alphabet) + 1  # Индекс токена <end>

    # Кодируем лейблы с добавлением токена <start> для кодера
    encoder_labels = [[start_token] + [dict_alphabet[char] for char in label] for label in y_captcha]

    # Кодируем лейблы с добавлением токена <end> для декодера
    decoder_labels = [[dict_alphabet[char] for char in label] + [end_token] for label in y_captcha]

    # Преобразование меток в тензоры
    encoder_tensors = pad_sequences(encoder_labels, maxlen=8, padding='post')
    decoder_tensors = pad_sequences(decoder_labels, maxlen=8, padding='post')

    # Создание датасета
    dataset = create_dataset(X_captcha, encoder_tensors, decoder_tensors, shuffle)

    return dataset


def create_dataset_for_captcha(filenames: list, alphabet: str) -> tuple[
        tuple[tf.data.Dataset, tf.data.Dataset, tf.data.Dataset, list],
        tuple[tf.data.Dataset, tf.data.Dataset, tf.data.Dataset, list]
    ]:
    '''Функция для создания датасета на основе алфавита и имен файлов'''
    
    # Создание датафрейма для удобства последующей обработки
    captcha_dataframe = create_dataframe(filenames)

    # Разделение датасета на обучающую и тестовую выборки
    train_captcha_df, test_captcha_df = train_test_split(captcha_dataframe, test_size=0.2, random_state=42)
    # Разделение тестовой части датасета на валидационную и тестовую выборки
    val_captcha_df, test_captcha_df = train_test_split(test_captcha_df, test_size=0.5, random_state=42)
    
    train_dataset = preparing_dataset(train_captcha_df, alphabet)
    val_dataset = preparing_dataset(val_captcha_df, alphabet)
    test_dataset = preparing_dataset(test_captcha_df, alphabet, False)

    return train_dataset, val_dataset, test_dataset
