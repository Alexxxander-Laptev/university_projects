a = float(input('Введите число: '))
b = float(input('Введите число: '))
c = float(input('Введите число: '))
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print (s)