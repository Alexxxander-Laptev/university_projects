class Perceptron:
    def __init__(self, input_size):
        self.weights = [0.0] * input_size
        self.threshold = 0.0

    def predict(self, inputs):
        activation = sum(w * x for w, x in zip(self.weights, inputs))
        return 1 if activation > self.threshold else 0

    def train(self, training_inputs, labels, learning_rate=0.1, max_epochs=1000):
        for epoch in range(max_epochs):
            total_error = 0
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                total_error += error
                if error != 0:
                    for i in range(len(self.weights)):
                        self.weights[i] += learning_rate * error * inputs[i]
            if total_error == 0:
                print("Training converged after {} epochs.".format(epoch + 1))
                break
        else:
            print("Training did not converge after {} epochs.".format(max_epochs))


# Создаем экземпляр персептрона с двумя входами (для двузначных чисел)
perceptron = Perceptron(2)

# Обучающие данные для распознавания четных и нечетных чисел
training_data = [
    ([0, 0], 0),  # 0
    ([0, 1], 1),  # 1
    ([1, 0], 1),  # 2
    ([1, 1], 0)   # 3
]

# Обучаем персептрон
perceptron.train([data[0] for data in training_data], [data[1] for data in training_data])

# Проверяем работу персептрона
test_data = [
    [0, 0],  # 0
    [0, 1],  # 1
    [1, 0],  # 2
    [1, 1]   # 3
]

for data in test_data:
    prediction = perceptron.predict(data)
    print("Input: {}, Prediction: {}, Odd (1) or Even (0)".format(data, prediction))


# import numpy as np

# class Perceptron:
#     def __init__(self, input_size):
#         # Инициализация весов с небольшими случайными значениями
#         self.weights = np.random.rand(input_size)
#         self.threshold = 0

#     def predict(self, inputs):
#         # Возвращаем 1, если сумма произведений весов на входы превышает порог, иначе 0
#         return 1 if np.dot(inputs, self.weights) > self.threshold else 0

#     def train(self, training_inputs, labels, epochs):
#         for epoch in range(epochs):
#             for inputs, label in zip(training_inputs, labels):
#                 prediction = self.predict(inputs)
#                 if prediction != label:
#                     if label == 0:
#                         # Увеличиваем веса, если предсказание неверное и оно должно быть 0
#                         self.weights += inputs
#                     else:
#                         # Уменьшаем веса, если предсказание неверное и оно должно быть 1
#                         self.weights -= inputs

# def main():
#     # Образы для обучения: четные числа (0) и нечетные числа (1)
#     training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
#     labels = np.array([0, 1, 1, 0])

#     # Создание и обучение персептрона
#     perceptron = Perceptron(input_size=2)
#     perceptron.train(training_inputs, labels, epochs=10)

#     # Проверка на тестовых данных
#     test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
#     print("Результаты предсказания:")
#     for inputs in test_inputs:
#         prediction = perceptron.predict(inputs)
#         print(f"Входы: {inputs}, Предсказание: {prediction}")

# if __name__ == "__main__":
#     main()
