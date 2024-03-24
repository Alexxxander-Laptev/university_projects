a = float(input('Введите число: '))
b = float(input('Введите число: '))
c = float(input('Введите число: '))
d = b * b - 4 * a * c
if d < 0:
    print ('Корней нет')
elif d == 0:
    print (-b / (2 * a))
else:
    print ('x1 = ', (-b + d ** 0.5) / (2 * a), ' x2 = ', (-b - d ** 0.5) / (2 * a))