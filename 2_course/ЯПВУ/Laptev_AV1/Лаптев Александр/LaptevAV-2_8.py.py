a = float(input('Введите положительное число: '))
b = float(input('Введите положительное число: '))
c = float(input('Введите положительное число: '))
d = float(input('Введите положительное число: '))
if (a <= c and b <= d) or (a <= d and b <= c):
    print ('Да, может')
else:
    print ('Нет, не может')