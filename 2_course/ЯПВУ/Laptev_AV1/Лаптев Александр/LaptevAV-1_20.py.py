x = int(input('Введите трёхзначное число: '))
c = x % 10
b = x // 10 % 10
a = x // 100
if a == c:
    print ('TRUE')
else:
    print ('FALSE')