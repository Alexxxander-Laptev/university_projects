x1 = float(input('Введите координату: '))
y1 = float(input('Введите координату: '))
x2 = float(input('Введите координату: '))
y2 = float(input('Введите координату: '))
k = (y2 - y1) / (x2 - x1)
b = y1 - (y2 - y1) / (x2 - x1) * x2
print (k)
print (b)