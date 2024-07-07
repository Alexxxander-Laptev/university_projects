import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from keras._tf_keras.keras.applications import MobileNetV2
from keras._tf_keras.keras.layers import Dense, GlobalAveragePooling2D
from keras._tf_keras.keras.models import Model


def evaluate_model(model, test_generator):
    '''Функция для классификации моделей'''
    predictions = model.predict(test_generator)
    predicted_classes = np.argmax(predictions, axis=1)
    true_classes = test_generator.classes
    class_labels = list(test_generator.class_indices.keys())

    return predicted_classes, true_classes, class_labels


if __name__ == '__main__':
    # Загрузка предобученной модели
    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(3, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)

    for layer in base_model.layers:
        layer.trainable = False

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Подготовка данных
    train_datagen = ImageDataGenerator(rescale=1./255, horizontal_flip=True, zoom_range=0.2)
    test_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        'C:/Users/Lapte/Documents/university_projects/1_course_master/Practice/datasets/train_dataset',
        target_size=(224, 224),
        batch_size=32,
        class_mode='categorical'
    )
    test_generator = test_datagen.flow_from_directory(
        'C:/Users/Lapte/Documents/university_projects/1_course_master/Practice/datasets/test_dataset',
        target_size=(224, 224),
        batch_size=32,
        class_mode='categorical',
        shuffle=False
    )

    # Обучение модели
    model.fit(train_generator, epochs=100, validation_data=test_generator)

    # Проведение классификации
    predicted_classes, true_classes, class_labels = evaluate_model(model, test_generator)

    cm = confusion_matrix(true_classes, predicted_classes)
    report = classification_report(true_classes, predicted_classes, target_names=class_labels)

    # Вычисление ошибок первого и второго рода
    fp = cm.sum(axis=0) - np.diag(cm)  # False Positives
    fn = cm.sum(axis=1) - np.diag(cm)  # False Negatives

    print(f"Confusion Matrix:\n{cm}\nClassification Report:\n{report}\n")
    print(f"False Positives (Type I errors) per class: {fp}\nFalse Negatives (Type II errors) per class: {fn}")
