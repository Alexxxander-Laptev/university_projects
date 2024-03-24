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
    st := 0.5
    dl := math.Pow((x2 - x1), 2) + math.Pow((y2 - y1), 2)
    ras := math.Pow(dl, float64(st))
    fmt.Println (ras)
}