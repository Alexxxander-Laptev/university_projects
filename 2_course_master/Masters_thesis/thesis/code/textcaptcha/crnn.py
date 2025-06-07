import tensorflow as tf
import numpy as np
from keras._tf_keras.keras.layers import Input, Conv2D, MaxPooling2D, Reshape, Dense, Dropout, Bidirectional, GRU, BatchNormalization
from keras._tf_keras.keras.regularizers import l2
from keras._tf_keras.keras.models import Model
from keras._tf_keras.keras import backend as K
from keras._tf_keras.keras.backend import ctc_decode
from keras._tf_keras.keras.optimizers import Adam
from keras._tf_keras.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras._tf_keras.keras.saving import register_keras_serializable


def decode_predictions(preds, max_length, alphabet):
    # Используем CTC-декодирование для предсказаний
    decoded_preds, _ = ctc_decode(preds, input_length=np.ones(preds.shape[0]) * preds.shape[1])
    texts = []
    for seq in decoded_preds[0]:
        text = ''.join([alphabet[i] for i in seq.numpy() if i != -1])  # Исключаем 'blank' символы
        texts.append(text)
    return texts


def decode_batch_predictions(pred):
    # CTC decode
    decoded, _ = ctc_decode(pred, input_length=np.ones(pred.shape[0]) * pred.shape[1],
                            greedy=True)
    decoded_texts = []
    
    # Преобразование в текст
    for seq in decoded[0]:
        text = ''.join([chr(x) for x in seq if x != -1])  # Пропускаем -1 (пустые символы CTC)
        decoded_texts.append(text)
    return decoded_texts


# Функция CTC Loss
# Функция для декодирования предсказаний модели
@register_keras_serializable(package='Custom', name='ctc_loss')
def ctc_loss(y_true, y_pred):
    # Формируем входные данные для CTC
    input_lenght = tf.ones(shape=(tf.shape(y_pred)[0], 1)) * tf.cast(tf.shape(y_pred)[1], tf.float32)
    label_length = tf.ones(shape=(tf.shape(y_true)[0], 1)) * 7
    return tf.reduce_mean(K.ctc_batch_cost(y_true, y_pred, input_lenght, label_length))
    

# Модель
def build_model(num_of_classes):
    '''Создание модели'''
    # Входной слой
    input_layer = Input((60, 250, 1))

    # Первый сверточный блок
    x = Conv2D(32, (3, 3), activation='relu', padding='same', kernel_regularizer=l2(0.003))(input_layer)
    x = BatchNormalization()(x)
    x = Conv2D(32, (3, 3), activation='relu', kernel_regularizer=l2(0.003))(x)
    x = MaxPooling2D((1, 2))(x)
    x = Dropout(0.25)(x)  # Dropout после каждого блока

    # Второй сверточный блок
    x = Conv2D(64, (3, 3), activation='relu', padding='same', kernel_regularizer=l2(0.003))(x)
    x = BatchNormalization()(x)
    x = Conv2D(64, (3, 3), activation='relu', kernel_regularizer=l2(0.003))(x)
    x = MaxPooling2D((1, 2))(x)
    x = Dropout(0.3)(x)

    # Третий сверточный блок
    x = Conv2D(128, (3, 3), activation='relu', padding='same', kernel_regularizer=l2(0.003))(x)
    x = BatchNormalization()(x)
    x = Conv2D(128, (3, 3), activation='relu', kernel_regularizer=l2(0.003))(x)
    x = MaxPooling2D((1, 2))(x)
    x = Dropout(0.4)(x)

    # Изменяем размерность тензора
    x = Reshape((-1, x.shape[-1] * x.shape[-2]))(x)

    # Первый рекурентный блок
    x = Bidirectional(GRU(128, return_sequences=True))(x)
    x = BatchNormalization()(x)
    x = Dropout(0.6)(x)

    # Второй рекурентный блок
    x = Bidirectional(GRU(128, return_sequences=True))(x)
    x = BatchNormalization()(x)
    x = Dropout(0.6)(x)

    # Третий рекурентный блок
    x = Bidirectional(GRU(128, return_sequences=True))(x)
    x = BatchNormalization()(x)
    x = Dropout(0.6)(x)

    # Выходной слой
    outputs = Dense(num_of_classes + 1, activation='softmax')(x)

    # Создание модели
    model = Model(inputs=input_layer, outputs=outputs)

    return model


def fit_crnn(num_of_classes, train, val):
    # Компиляция модели
    model = build_model(num_of_classes)
    optimizer = Adam(learning_rate=0.001, weight_decay=1e-6)
    model.compile(
        loss=ctc_loss,
        optimizer=optimizer
    )

    # Вывод структуры модели
    model.summary()

    lr_sheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6)
    early_stop = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

    # Обучение модели
    history = model.fit(
        train,
        validation_data=val,
        epochs=15,
        callbacks=[early_stop, lr_sheduler]
    )

    model.save('crnn_model.keras')

    return model, history
