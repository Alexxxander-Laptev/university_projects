package main
import ("fmt"
        "math"
)

func factorial(n float64) float64 {
  // Функция для нахождения факториала для введённого числа:
    if n == 0 {
        return 1
    }
    return n * factorial(n - 1)
}

func fibonacchi(n float64) float64 {
  // Функция для нахождения числа Фибоначчи по его порядковому номеру:
    if n == 0 {
        return 0
    }
    if n == 1 {
        return 1
    }
    return fibonacchi(n - 1) + fibonacchi(n - 2)
}

func Max_1(a, b float64) float64 {
  // Максимальное значение для 2 чисел (вспомогательная функция):
    if (a < b) {
        return (b)
    }
    return (a)
}
func Max_2(a, b, c float64) float64 {
  // Максимальное значение для 3 чисел (вспомогательная функция):
    if ((a < b) && (b < c) && (a < c)) {
        return (c)
    } else if ((c < b) && (b < a) && (c < a)) {
        return (a)
    }
    return (b)
}
func Max_3(a, b, c float64) float64 {
  // Максимальное значение для 2 чисел (вспомогательная функция):
    if ((a - b) > (b - c)) {
        return (a - b)
    }
    return (b - c)
}

func mathematic(a float64, b float64, c float64) float64 {
  // Функция для работы с максимальными значениями среди нескольких значений:
    m := Max_1(a, b)
    n := Max_2(a, b, c)
    k := Max_3(a, b, c)
    y := (m + n) / (k + a + b + c)
    return y
}

func s(a float64, b float64, c float64) float64 {
  // Функция нахождения площади треугольника по формуле Герона
    if ((c < a + b) && (b < a + c) && (a < b + c)) {
        var p = (a + b + c) / 2
        var s = math.Pow((p * (p - a) * (p - b) * (p - c)), 0.5)
        return s
    }
    return -0
}

func sravn(a float64, b float64, c float64, d float64) float64 {
  // Функция для сравнения двух дробей:
    if (a / b) > (c / d) {
        fmt.Println("Первая дробь больше")
    } else if (a / b) < (c / d) {
        fmt.Println("Вторая дробь больше")
    }
    fmt.Println("Дроби равны")
    return 0
}

func st(a float64, b float64, c float64) float64 {
  // Функция для определения разновидности треуголника по его углам:
    if c < a + b && b < a + c && a < b + c {
        if math.Pow(c, 2) == math.Pow(a, 2) + math.Pow(b, 2) || math.Pow(b, 2) == math.Pow(a, 2) + math.Pow(c, 2) || math.Pow(a, 2) == math.Pow(c, 2) + math.Pow(b, 2) {
            fmt.Println("Этот треугольник прямоугольный")
        } else if math.Pow(c, 2) < math.Pow(a, 2) + math.Pow(b, 2) || math.Pow(b, 2) < math.Pow(a, 2) + math.Pow(c, 2) || math.Pow(a, 2) < math.Pow(c, 2) + math.Pow(b, 2) {
            fmt.Println("Этот треуголник остроугольный")
        } else {
            fmt.Println("Этот треуголник тупоугольный")
        }
    } else {
        fmt.Println("Нельзя построить такого треугольника")
    }
    return 0
}

func koord(x1 float64, y1 float64, x2 float64, y2 float64) float64 {
  // Функция для определения того, какая из двух точек находится ближе к центру координат:
    var d1 = math.Pow((math.Pow(x1, 2) + math.Pow(y1, 2)), 0.5)
    var d2 = math.Pow((math.Pow(x2, 2) + math.Pow(y2, 2)), 0.5)
    if d1 > d2 {
        fmt.Println("Вторая точка находится ближе к началу координат")
    } else if d2 > d1 {
        fmt.Println("Первая точек находится ближе к началу координат")
    } else {
        fmt.Println("Эти точки находятся на одинаковом удалении от начала координат")
    }
    return 0
}

func tochka(x float64, y float64) float64 {
  // Функция для определения положения точки на плоскости:
    if x > 0 && y > 0 {
        print ("Точка лежит в первой четверти")
    } else if x > 0 && y < 0 {
        print ("Точка лежит в четвёртой четверти")
    } else if x < 0 && y < 0 {
        print ("Точка лежит в третьей четверти")
    } else if x < 0 && y > 0 {
        print ("Точка лежит во второй четверти")
    } else {
        print ("Точка лежит на осях координат")
    }
    return 0
}

func pryamoygolnik(a float64, b float64, c float64, d float64) float64 {
  // Функция для определения того, можно ли построить прямоугольник по данным сторонам:
    if (a == b && c == d) || (a == c && b == d) || (a == d && b == c) {
        fmt.Println("Можно построить прямоугольник с такими сторонами")
    } else {
        fmt.Println("Нельзя построить прямоугольник с такими сторонами")
    }
    return 0
}

func ploshadi(skv float64, skr float64) float64 {
  // Функция для определения того, какая из двух фигур помещается в другую:
    var pi = 3.14159265
    var akv = math.Pow(skv, 0.5)
    var rkr = math.Pow((skr / pi), 0.5)
    var diamkr = rkr * 2
    var diagkv = math.Pow((math.Pow(akv, 2) + math.Pow(akv, 2)), 0.5)
    if diamkr <= akv {
        fmt.Println("Круг помещается в квадрат")
    } else if diagkv <= diamkr {
        fmt.Println("Квадрат помещается в круг")
    } else {
        fmt.Println("Ни одна из фигур не помещается в другую")
    }
    return 0
}

func main() {
    var k float64
    fmt.Println("Введите число от 1 до 10: ")
    fmt.Scan (&k)
    if k == 1 {
      var n float64
      fmt.Println("Введите число: ")
      fmt.Scan (&n)
      fmt.Println(factorial(n))
    }
    if k == 2 {
      var n float64
      fmt.Println("Введите число: ")
      fmt.Scan (&n)
      fmt.Println(fibonacchi(n))
    }
    if k == 3 {
      var a float64
      fmt.Println("Введите число: ")
      fmt.Scan (&a)
      var b float64
      fmt.Println("Введите число: ")
      fmt.Scan (&b)
      var c float64
      fmt.Println("Введите число: ")
      fmt.Scan (&c)
      fmt.Println(mathematic(a, b, c))
    }
    if k == 4 {
      var a float64
      fmt.Println("Введите число: ")
      fmt.Scan (&a)
      var b float64
      fmt.Println("Введите число: ")
      fmt.Scan (&b)
      var c float64
      fmt.Println("Введите число: ")
      fmt.Scan (&c)
      fmt.Println(s(a, b, c))
    }
    if k == 5 {
      var a float64
      fmt.Println("Введите число: ")
      fmt.Scan (&a)
      var b float64
      fmt.Println("Введите число: ")
      fmt.Scan (&b)
      var c float64
      fmt.Println("Введите число: ")
      fmt.Scan (&c)
      var d float64
      fmt.Println("Введите число: ")
      fmt.Scan (&d)
      fmt.Println(sravn(a, b, c, d))
    }
    if k == 6 {
      var a float64
      fmt.Println("Введите число: ")
      fmt.Scan (&a)
      var b float64
      fmt.Println("Введите число: ")
      fmt.Scan (&b)
      var c float64
      fmt.Println("Введите число: ")
      fmt.Scan (&c)
      fmt.Println(st(a, b, c))
    }
    if k == 7 {
      var x1 float64
      fmt.Println("Введите число: ")
      fmt.Scan (&x1)
      var y1 float64
      fmt.Println("Введите число: ")
      fmt.Scan (&y1)
      var x2 float64
      fmt.Println("Введите число: ")
      fmt.Scan (&x2)
      var y2 float64
      fmt.Println("Введите число: ")
      fmt.Scan (&y2)
      fmt.Println(koord(x1, y1, x2, y2))
    }
    if k == 8 {
      var x float64
      fmt.Println("Введите число: ")
      fmt.Scan (&x)
      var y float64
      fmt.Println("Введите число: ")
      fmt.Scan (&y)
      fmt.Println(tochka(x, y))
    }
    if k == 9 {
      var a float64
      fmt.Println("Введите число: ")
      fmt.Scan (&a)
      var b float64
      fmt.Println("Введите число: ")
      fmt.Scan (&b)
      var c float64
      fmt.Println("Введите число: ")
      fmt.Scan (&c)
      var d float64
      fmt.Println("Введите число: ")
      fmt.Scan (&d)
      fmt.Println(pryamoygolnik(a, b, c, d))
    }
    if k == 10 {
      var skv float64
      fmt.Println("Введите число: ")
      fmt.Scan (&skv)
      var skr float64
      fmt.Println("Введите число: ")
      fmt.Scan (&skr)
      fmt.Println(ploshadi(skv, skr))
    }
}