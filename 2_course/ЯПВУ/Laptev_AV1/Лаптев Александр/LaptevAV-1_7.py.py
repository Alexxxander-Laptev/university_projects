ch = int(input('Введите число: '))
d = ch % 10
c = ch // 10 % 10
b = ch // 100 %10
a = ch // 1000
print (d, c, b, a, sep="")