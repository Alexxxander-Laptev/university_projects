package main
import ("fmt"
        
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
    k := (y2 - y1) / (x2 - x1)
    b := y1 - (y2 - y1) / (x2 - x1) * x2
    fmt.Println (k, b)
}
