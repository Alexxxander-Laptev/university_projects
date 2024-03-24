import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    """Функция для черчения графиков функций"""
    x = np.arange(0, 21) #Границы графика по оси х
    plt.plot(x, x * (-0.5) + 10) #Создание графика функции
    x = np.arange(0, 11) #Границы графика по оси х
    plt.plot(x, x * (-2) + 20) #Создание графика функции
    plt.plot([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) #Создание графика функции
    plt.show()

main()