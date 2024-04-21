import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

class Perceptron:
    '''Класс персептрона'''
    def __init__(self, input_size, learning_rate=0.1):
        # Инициализация весов
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()
        self.learning_rate = learning_rate
    
    def activate(self, x):
        # Пороговая функция активации
        return 1 if x > 0 else 0
    
    def forward(self, inputs):
        # Прямое распространение сигнала
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        return self.activate(weighted_sum)

    def train(self, inputs, target):
        # Обучение перцептрона с использованием дельта-правила
        prediction = self.forward(inputs)
        if prediction != target:
            # Вычисление изменения весов
            delta_weights = self.learning_rate * (target - prediction) * inputs
            # Обновление весов
            self.weights += delta_weights
            # Обновление смещения
            self.bias += self.learning_rate * (target - prediction)
            return True  # Возвращаем True, чтобы указать, что было изменение весов
        else:
            return False  # Если предсказание верное, возвращаем False


if __name__ == '__main__':
    # Загрузка датасета чисел
    digits = load_digits()

    mode  = 0
    while mode != 1 and mode != 2:
        print('Режимы распознавания:\n1. Четность/нечетность числа\n2. Кратность/не кратность числу 3')
        mode = int(input('Введите номер режима:\t'))
        
    if mode == 1:
        # Преобразование целевых меток для отражения четности чисел
        y_transformed = digits.target % 2
    else:
        # Преобразование целевых меток для отражения четности чисел
        y_transformed = (digits.target % 3 == 0).astype(int)
    # Разделение датасета на обучающую и тестовую выборки с соотношением 80:20
    X_train, X_test, y_train, y_test = train_test_split(digits.data, y_transformed, test_size=0.2, random_state=42)

    # Создаем персептрон с размером входа, соответствующим размеру признаков в датасете
    perceptron = Perceptron(X_train.shape[1])

    # Обучение персептрона
    epochs = 1000
    for epoch in range(epochs):
        for i in range(len(X_train)):
            perceptron.train(X_train[i], y_train[i])

    # Проверка работы персептрона на тестовой выборке
    correct = 0
    for i in range(len(X_test)):
        prediction = perceptron.forward(X_test[i])
        if prediction == y_test[i]:
            correct += 1

    accuracy = correct / len(X_test)
    print(f"Точность предсказания: {accuracy}")
