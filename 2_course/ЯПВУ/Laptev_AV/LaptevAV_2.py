import math
from math import radians
import numpy as np
import matplotlib.pyplot as plt

def main():
    """Функция для черчения графиков функций"""
    x = np.arange(-31, radians(1800), radians(12)) #Границы графиков по оси х
    plt.plot(x, np.sin(x) * 2)  #Отсюда и ниже осуществляется рисование графиков
    plt.plot(x, np.sin(x) + 7)
    plt.plot(x, np.cos(x / 5) + 5)
    plt.plot(x, np.cos(x) + 5)
    x = np.arange(-7, 7) #Границы графика по оси х
    plt.plot(x, np.tan(x))
    plt.show()

main()
