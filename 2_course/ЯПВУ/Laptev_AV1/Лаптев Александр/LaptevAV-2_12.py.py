a = float(input('Введите число: '))
b = float(input('Введите число: '))
c = float(input('Введите число: '))
if a > b > c or c > b > a:
    y = b
    print (y)
elif b > a > c or c > a > b:
    y = a
    print (y)
elif a > c > b or b > c > a:
    y = c
    print (y)
else:
    print ('Некорретный ввод')