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
    s := math.Abs (float64((x1 - x3) * (y2 - y3) - ((y1 - y3) * (x2 - x3)))) / 2
    fmt.Println (s)
}