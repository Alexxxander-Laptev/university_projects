import math
import numpy as np
import matplotlib.pyplot as plt

"""Пункт 2: А, В"""

g = 2
n = 5

def f(x):
    return g * math.sin(0.1 * math.pi * n) + g * x / 2 - n * x ** 2 / 10

Y = []
Xi = []
M = 2.5
a = 0
b = 10
M0 = 625899
m = 40
x0 = 2 ** (-m)                              	#нулевой сгенерированный элемент, генерится по отдельной формуле
N = 100000000
r1 = 0
r2 = 0
h = 1 / N
z = []
Mx = 0
Mx2 = 0

fig, ax = plt.subplots()

for i in range(N):
    r1 = x0
    xn = math.modf(M0 * x0)                 #вычленение дробной части произведения из формулы (1)
    x1 = xn[0]
    r2 = x1
    X0 = a + r1 * (b - a)
    l = r2 * M
    if l < f(X0):
        Xi.append(X0)
        z.append(l)
    Mx += X0
    Mx2 += X0 ** 2
    x0 = x1
    xn = math.modf(M0 * x0)                 #вычленение дробной части произведения из формулы (1)
    x1 = xn[0]
    x0 = x1
Mx = Mx / N
Mx2 = Mx2 / N
a = Mx
b = Mx2
D = b - a ** 2
print('Математическое ожидание: ', Mx)
print('Дисперсия: ', D)

ckl2 = [x * 0.1 for x in range(101)]
for j in ckl2:
    Y.append(f(j))

ax.scatter(Xi, z, alpha = 0.5)
plt.plot(ckl2, Y, "r", alpha = 0.5)
plt.show()
