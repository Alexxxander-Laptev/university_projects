package main
import ("fmt"
        "math"
)

func main() {
    var a float64
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&a)
    var b float64
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&b)
    var c float64
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&c)
    d := b * b - 4 * a * c
    if d < 0 {
        fmt.Print ("Korneyi net")
    }  else if d == 0 {
        fmt.Print ("x = ", -b / (2 * a))
    } else {
        fmt.Print ("x1 = ", (-b + math.Pow(d, 0.5)) / (2 * a), " x2 = ", (-b - math.Pow(d, 0.5)) / (2 * a))
    }
}
