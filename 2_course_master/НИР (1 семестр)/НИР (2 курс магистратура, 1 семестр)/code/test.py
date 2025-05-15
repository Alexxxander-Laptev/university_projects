import numpy as np
import tensorflow as tf
from keras._tf_keras.keras.models import load_model


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import seaborn as sbn

    # Алфавит допустимых символов
    alphabet = ' ABCDEFGHJKLMNPQRSTWXYZ023456789'

    list_filenames = np.load('data.npy', allow_pickle=True)
    # Создание единого датасета
    captcha_dataset = create_dataset_for_captcha(list_filenames, alphabet)
    if False:
        # Обучение модели
        model_captcha, history_captcha = fit_seq_to_seq(len(alphabet), captcha_dataset[0], captcha_dataset[1])
        # Построение графика изменения val_loss и loss
        plt.plot(history_captcha.history['loss'], label='Training Loss')
        plt.plot(history_captcha.history['val_loss'], label='Validation Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        # Сохраняем график для отчета
        plt.savefig('Model_loss.png')

    # Загружаем предобученную модель и получаем предсказания для тестовой выборки
    model = load_model('seq_to_seq_model.keras')
    predictions = model.predict(captcha_dataset[2])

    # Переводим предсказания из представления вероятностей в классы
    pred_classes = np.argmax(predictions, axis=-1)
    captcha_labels = [label.numpy() for _, label in captcha_dataset[2].unbatch()]
    captcha_labels = np.array(captcha_labels)

    # Убираем padding
    def remove_padding(sequences, padding_value=0):
        return [seq[seq != padding_value] for seq in sequences]

    # Убираем padding из предсказаний и меток
    pred_classes_no_padding = remove_padding(pred_classes, padding_value=0)
    true_labels_no_padding = remove_padding(np.array(captcha_labels), padding_value=0)

    # Проверяем размеры списков после удаления padding
    print(f"Количество предсказаний: {len(pred_classes_no_padding)}")
    print(f"Количество меток: {len(true_labels_no_padding)}")

    # Проверяем совпадение предсказаний и истинных меток посимвольно
    sequence_accuracy = np.mean(
        [np.array_equal(pred, true) for pred, true in zip(pred_classes, captcha_labels)]
    )
    print(f"Точность последовательностей (без padding): {sequence_accuracy:.4f}")

    # Расчет точности символов (character-level accuracy)
    total_characters = np.prod(captcha_labels.shape)
    correct_characters = np.sum(pred_classes == captcha_labels)
    character_accuracy = correct_characters / total_characters
    print(f"Точность символов: {character_accuracy:.4f}")

    from sklearn.metrics import confusion_matrix
    # Построение матрицы ошибок для анализа
    true_symb, pred_symb = [], []

    for true_seq, pred_seq in zip(true_labels_no_padding, pred_classes_no_padding):
        true_symb.extend(true_seq)
        pred_symb.extend(pred_seq)
    cm = confusion_matrix(true_symb, pred_symb)

    plt.figure(figsize=(10, 7))
    sbn.heatmap(cm, annot=True, fmt='g', cmap='Blues')
    plt.xlabel('Predicted classes')
    plt.ylabel('True classes')
    plt.title('Confusion matrix')
    plt.savefig('Confusion_matrix.png')

    from collections import defaultdict

    sequence_accuracy_by_length = defaultdict(list)
    for pred, true in zip(pred_classes_no_padding, true_labels_no_padding):
        seq_len = len(true)
        is_correct = np.array_equal(pred, true)
        sequence_accuracy_by_length[seq_len].append(is_correct)

    # Считаем точность для каждой длины
    for length, results in sequence_accuracy_by_length.items():
        acc = np.mean(results)
        print(f"Длина {length}: Точность {acc:.4f}")