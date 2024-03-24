ch = int(input('Введите число: '))
c = ch % 10
b = ch // 10 % 10
a = ch // 100
pr = a * b * c
print (pr)