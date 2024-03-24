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
    p := (a + b + c) / 2
    r := math.Pow(((p - a) * (p - b) * (p - c) / p), 0.5)
    fmt.Println (r)
}
