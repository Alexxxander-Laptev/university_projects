a = float(input('Введите число: '))
b = float(input('Введите число: '))
c = float(input('Введите число: '))
p = (a + b + c) / 2
r = ((p - a) * (p - b) * (p - c) / p) ** 0.5
print (r)