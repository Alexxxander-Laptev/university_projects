import math
k = float(input('Введите число: '))
al = math.atan(k)
al = (math.pi / 2 - al)
print (math.degrees(al))