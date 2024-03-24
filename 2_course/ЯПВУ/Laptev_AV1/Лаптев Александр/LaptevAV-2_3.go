package main
import ("fmt"
        
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
        fmt.Print ("1 koren")
    } else {
        fmt.Print ("2 Korneyi")
    }
}
