package main
import ("fmt"
        "math"
)

func main() {
    var x1 float64
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&x1)
    var y1 float64
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&y1)
    var x2 float64
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&x2)
    var y2 float64
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&y2)
    var x3 float64
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&x3)
    var y3 float64
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&y3)
    a := math.Pow((math.Pow((x2 - x1), 2) + math.Pow((y2 - y1), 2)), 0.5)
    b := math.Pow((math.Pow((x3 - x2), 2) + math.Pow((y3 - y2), 2)), 0.5)
    c := math.Pow((math.Pow((x3 - x1), 2) + math.Pow((y3 - y1), 2)), 0.5)
    if (a == b) && (b == c) && (a == c) {
        fmt.Print ("Etot treygolnik - ravnostoronniyi")
    } else if (a == b) || (b == c) || (a == c) {
        fmt.Print ("Etot treygolnik - ravnobedrenniyi")
    } else {
        fmt.Print ("Etot treygolnik - raznostoronniyi")
    }
}