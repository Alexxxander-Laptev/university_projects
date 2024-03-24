x = int(input('Введите трёхзначное число: '))
c = x % 10
b = x // 10 % 10
a = x // 100
if a == b:
    print ('TRUE')
elif a == c:
    print ('TRUE')
elif b == c:
    print ('TRUE')
elif a == b == c:
    print ('TRUE')
else:
    print ('FALSE')