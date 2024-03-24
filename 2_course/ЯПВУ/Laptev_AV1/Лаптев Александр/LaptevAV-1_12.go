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
    st := 0.5
    p := (a + b + c) / 2
    s := math.Pow((p * (p - a) * (p - b) * (p - c)), float64(st))
    fmt.Println (s)
}