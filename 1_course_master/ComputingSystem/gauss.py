import threading
import time


def example_matrixes(num_example):
    # ПРимеры матриц, для которых точно есть известное решение
    if num_example == 1:
        # Матрица 2х3
        matrix = [[3, 2, 16],
                  [2, -1, 6]]
        line = 2
        row = 3
    elif num_example == 2:
        # Матрица 3х4
        matrix = [[1, 2, 3, 1],
                  [2, -1, 2, 6],
                  [1, 1, 5, -1]]
        line = 3
        row = 4
    elif num_example == 3:
        # Матрица 4х5
        matrix = [[2, 5, 4, 1, 20],
                  [1, 3, 2, 1, 11],
                  [2, 10, 9, 7, 40],
                  [3, 8, 9, 2, 37]]
        line = 4
        row = 5
    elif num_example == 4:
        # Матрица 5х6
        matrix = [[-4, 6, -10, -2, -2, -72],
                  [-6, 4, -4, -8, -9, -67],
                  [7, -5, -9, -7, -9, -51],
                  [1, -6, 0, 5, -2, -44],
                  [8, 4, 9, 1, -4, 22]]
        line = 5
        row = 6
    else:
        # Матрица 6х7
        matrix = [[4, -9, 6, 1, 4, -6, -52],
                  [-4, 1, 4, -1, 9, 1, 83],
                  [9, -6, -1, 8, -8, -4, -183],
                  [4, -3, 7, -5, -7, 3, 21],
                  [6, 2, -2, 6, -7, -3, -123],
                  [6, -4, 7, 9, 8, -6, -93]]
        line = 6
        row = 7
    return matrix, line, row


def ladder(deep_matrix, i):
    # Функция для распараллеливания суммирования уравнений ниже i-го уравнения с i-м
    first_factor = matrix[i][deep_matrix]
    second_factor = matrix[deep_matrix][deep_matrix]
    for j in range(deep_matrix, row):
        matrix[i][j] = matrix[i][j] * second_factor + \
            matrix[deep_matrix][j] * (-first_factor)


def straight_stroke(matrix, line):
    # Прямой ход в решении СЛАУ методом Гаусса (1 этап)
    if matrix[0][0] == 0:
        for i in range(1, line):
            if matrix[i][0] > 0:
                matrix.insert(0, matrix[i])
                matrix.pop(i + 1)
                break

    for deep_matrix in range(line - 1):
        for i in range(deep_matrix + 1, line):
            matrix_member_str = threading.Thread(
                target=ladder, args=(deep_matrix, i,))
            matrix_member_str.start()
        matrix_member_str.join()
    return matrix


def ladder_reverse(x, count_lines, i):
    # Функция для распараллеливания подстановки извесных коэффициентов
    matrix[count_lines][i] = matrix[count_lines][i + 1] - \
        (matrix[count_lines][i] * x[i])


def reverse_stroke(matrix, line):
    # ОБратный ход в решении СЛАУ методом Гаусса (2 этап)
    x = [0] * line
    for i in range(line - 1, -1, -1):
        x[i] = matrix[i][i + 1] / matrix[i][i]
        for count_lines in range(i - 1, -1, -1):
            matrix_member_rev = threading.Thread(
                target=ladder_reverse, args=(x, count_lines, i,))
            matrix_member_rev.start()
        matrix_member_rev.join()
    return x


if __name__ == "__main__":
    mode = 0
    while mode < 1 or mode > 2:
        mode = int(
            input("Введите номер режима (1 - ввод вручную, 2 - тестовые матрицы):\t"))

    matrix = []
    if mode == 1:
        # Задаем матрицу вручную
        line = int(input("Введите количество строк:\t"))
        row = int(input("Введите количество столбцов:\t"))
        for i in range(line):
            matrix_line = []
            for j in range(row):
                element = int(input(f"Введите элемент ({i};{j}):\t"))
                matrix_line.append(element)
            matrix.append(matrix_line)
    elif mode == 2:
        num_example = int(input("Введите номер тестовой матрицы (от 1 до 5):\t"))
        # Тестовые наборы матриц
        matrix = example_matrixes(num_example)[0]
        line = example_matrixes(num_example)[1]
        row = example_matrixes(num_example)[2]
    print(matrix)
    start_time = time.time()
    
    print(straight_stroke(matrix, line))
    x = reverse_stroke(matrix, line)
    end_time = time.time()
    print(x)
    print(end_time - start_time)
