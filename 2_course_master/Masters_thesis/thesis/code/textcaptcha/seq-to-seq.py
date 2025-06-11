import tensorflow as tf
from keras._tf_keras.keras import layers, Model
from keras._tf_keras.keras.callbacks import EarlyStopping, ReduceLROnPlateau

from create_dataset import create_dataset_for_captcha


# Кодировщик
def build_encoder():
    encoder_inputs = layers.Input(shape=(60, 250, 1), name="encoder_inputs")
    
    # Первый сверточный блок
    x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(encoder_inputs)
    x = layers.BatchNormalization()(x)
    x = layers.Conv2D(32, (3, 3), activation='relu')(x)
    x = layers.MaxPooling2D((2, 2))(x)

    # Второй сверточный блок
    x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Conv2D(64, (3, 3), activation='relu')(x)
    x = layers.MaxPooling2D((2, 2))(x)

    # Третий сверточный блок
    x = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Conv2D(128, (3, 3), activation='relu')(x)
    x = layers.MaxPooling2D((2, 2))(x)

    # Четвертый сверточный блок
    x = layers.Conv2D(256, (3, 3), activation='relu', padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Conv2D(256, (3, 3), activation='relu')(x)
    x = layers.MaxPooling2D((2, 2))(x)

    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(256, activation="relu")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Reshape((1, 256))(x)  # Добавляем временное измерение
    
    # RNN слой
    encoder_output, encoder_state = layers.GRU(256, return_sequences=True, return_state=True)(x)
    
    return Model(encoder_inputs, [encoder_output, encoder_state], name="encoder")


# Декодировщик с использованием Attention-механизма
def build_decoder(alphabet_size):
    decoder_inputs = layers.Input(shape=(None,), name="decoder_inputs")
    encoder_state_input = layers.Input(shape=(256,), name="encoder_state_input")

    x = layers.Embedding(alphabet_size, 128)(decoder_inputs)
    rnn_output, decoder_state = layers.GRU(256, return_sequences=True, return_state=True)(x, initial_state=encoder_state_input)
    
    # Attention
    attention_output = layers.AdditiveAttention()([rnn_output, encoder_state_input])
    x = layers.Concatenate()([rnn_output, attention_output])
    decoder_outputs = layers.Dense(alphabet_size, activation="softmax")(x)
    
    return Model([decoder_inputs, encoder_state_input], [decoder_outputs, decoder_state], name="decoder")


def fit_seq_to_seq(number_of_classes: int, train_dataset: tf.data.Dataset, val_dataset: tf.data.Dataset) -> tuple[Model, dict]:
    # Построение полной модели
    encoder = build_encoder()
    decoder = build_decoder(number_of_classes + 2)

    # Полная модель
    encoder_inputs = encoder.input
    decoder_inputs = layers.Input(shape=(None,), name="decoder_inputs")

    _, encoder_state = encoder(encoder_inputs)
    decoder_output, _ = decoder([decoder_inputs, encoder_state])

    seq2seq_model = Model([encoder_inputs, decoder_inputs], decoder_output, name="seq2seq_model")

    # Компиляция модели
    seq2seq_model.compile(
        loss="sparse_categorical_crossentropy",
        optimizer="adam",
        metrics=["accuracy"]
    )

    seq2seq_model.summary()

    lr_sheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6)
    early_stop = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

    # Обучение модели
    history = seq2seq_model.fit(
        train_dataset,
        validation_data=val_dataset,
        epochs=20,
        callbacks=[early_stop, lr_sheduler]
    )
    
    seq2seq_model.save('seq_to_seq_model.keras')

    return seq2seq_model, history
