puts ("Введите k от 1 до 10: ")
k = gets.to_i
if k == 1
  puts ("Введите n: ")
  n = gets.to_i
  def factorial (n)
    =begin
    Функция для нахождения факториала для введённого числа
    =end
      if n == 0
          return 1
      else
          return n * factorial(n - 1)
      end
  end
  puts factorial (n)
end

if k == 2
  puts ("Введите n: ")
  n = gets.to_i
  def fibonacchi (n)
    =begin
    Функция для нахождения числа Фибоначчи по его порядковому номеру
    =end
      if n == 0 or n == 1
          return n
      else
          return fibonacchi(n - 2) + fibonacchi(n - 1)
      end
  end
  puts fibonacchi (n)
end

if k == 3
  puts ("Введите a: ")
  a = gets.to_i
  puts ("Введите b: ")
  b = gets.to_i
  puts ("Введите c: ")
  c = gets.to_i
  def mathematic(a, b, c)
    =begin
    Функция для работы с максимальными значениями среди нескольких значений
    =end
      y = ([a, b].max + [a, b, c].max) / ([a - b, b - c] .max + a + b + c)
      return y
  end
  puts mathematic(a, b, c)
end

if k == 4
  puts ("Введите a: ")
  a = gets.to_i
  puts ("Введите b: ")
  b = gets.to_i
  puts ("Введите c: ")
  c = gets.to_i
  def s(a, b, c)
    =begin
    Функция нахождения площади треугольника по формуле Герона
    =end
      if (c < a + b) and (b < a + c) and (a < b + c)
          p = (a + b + c) / 2
          s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
          return s
      else
          return "Нельзя построить такого треуголбника"
      end
  end
  puts s(a, b, c)
end

if k == 5
  puts ("Введите a: ")
  a = gets.to_f
  puts ("Введите b: ")
  b = gets.to_f
  puts ("Введите c: ")
  c = gets.to_f
  puts ("Введите d: ")
  d = gets.to_f
  def sravn(a, b, c, d)
    =begin
    Функция для сравнения двух дробей
    =end
      if (a / b) > (c / d)
          print 'Первая дробь больше'
      elsif (a / b) < (c / d)
          print 'Вторая дробь больше'
      else
          print 'Дроби равны'
      end
  end
  puts sravn(a, b, c, d)
end

if k == 6
  puts ("Введите a: ")
  a = gets.to_f
  puts ("Введите b: ")
  b = gets.to_f
  puts ("Введите c: ")
  c = gets.to_f
  def s(a, b, c)
    =begin
    Функция для определения разновидности треуголника по его углам
    =end
      if c < a + b and b < a + c and a < b + c
          if c ** 2 == a ** 2 + b ** 2 or b ** 2 == a ** 2 + c ** 2 or a ** 2 == c ** 2 + b ** 2
              print ('Этот треугольник прямоугольный')
          elsif c ** 2 < a ** 2 + b ** 2 or b ** 2 < a ** 2 + c ** 2 or a ** 2 < c ** 2 + b ** 2
              print ('Этот треугольник остроугольный')
          else
              print ('Этот треугольник тупоугольный')
          end
      else
          print ('Нельзя построить такого треугольника')
      end
  end
  puts s(a, b, c)
end

if k == 7
  puts ("Введите x1: ")
  x1 = gets.to_f
  puts ("Введите y1: ")
  y1 = gets.to_f
  puts ("Введите x2: ")
  x2 = gets.to_f
  puts ("Введите y2: ")
  y2 = gets.to_f
  def koord(x1, y1, x2, y2)
    =begin
    Функция для определения того, какая из двух точек находится ближе к центру координат
    =end
      d1 = (x1 ** 2 + y1 ** 2) ** 0.5
      d2 = (x2 ** 2 + y2 ** 2) ** 0.5
      if d1 > d2
          print ('Вторая точка находится ближе к началу координат')
      elsif d2 > d1
          print ('Первая точка находится ближе к началу координат')
      else
          print ('Эти точки находятся на одинаковом удалении от начала координат')
      end
  end
  puts koord(x1, y1, x2, y2)
end

if k == 8
  puts ("Введите x: ")
  x = gets.to_f
  puts ("Введите y: ")
  y = gets.to_f
  def tochka(x, y)
    =begin
    Функция для определения положения точки на плоскости
    =end
      if x > 0 and y > 0
          print ('Точка лежит в первой четверти')
      elsif x > 0 and y < 0
          print ('Точка лежит в четвёртой четверти')
      elsif x < 0 and y < 0
          print ('Точка лежит в третьей четверти')
      elsif x < 0 and y > 0
          print ('Точка лежит во второй четверти')
      else
          print ('Точка лежит на осях координат')
      end
  end
  puts tochka(x, y)
end

if k == 9
  puts ("Введите a: ")
  a = gets.to_f
  puts ("Введите b: ")
  b = gets.to_f
  puts ("Введите c: ")
  c = gets.to_f
  puts ("Введите d: ")
  d = gets.to_f
  def pryamoygolnik(a, b, c, d)
    =begin
    Функция для определения того, можно ли построить прямоугольник по данным сторонам
    =end
      if (a == b and c == d) or (a == c and b == d) or (a ==    d and b == c)
          print ('Можно построить прямоугольник с такими сторонами')
      else
          print ('Нельзя построить прямоугольник с такими сторонами')
      end
  end
  puts pryamoygolnik(a, b, c, d)
end

if k == 10
  puts ("Введите skv: ")
  skv = gets.to_f
  puts ("Введите skr: ")
  skr = gets.to_f
  def ploshadi(skv, skr)
    =begin
    Функция для определения того, какая из двух фигур помещается в другую
    =end
      pi = 3.14159265
      akv = skv ** 0.5
      rkr = (skr / pi) ** 0.5
      diamkr = rkr * 2
      diagkv = (akv ** 2 + akv ** 2) ** 0.5
      if diamkr <= akv
          print ('Круг помещается в квадрат')
      elsif diagkv <= diamkr
          print ('Квадрат помещается в круг')
      else
          print ('Ни одна из фигур не помещается в другую')
      end
  end
  puts ploshadi(skv, skr)
end