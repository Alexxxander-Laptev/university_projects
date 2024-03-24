a = float(input('Введите число: '))
b = float(input('Введите число: '))
c = float(input('Введите число: '))
d = b * b - 4 * a * c
if d < 0:
    print ('Корней нет')
elif d == 0:
    print ('1 корень')
else:
    print ('2 корня')