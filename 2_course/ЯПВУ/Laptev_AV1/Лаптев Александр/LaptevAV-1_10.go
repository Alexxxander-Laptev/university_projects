package main
import ("fmt"
        
)

func main() {
    var x float64
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&x)
    var y float64
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&y)
    per := x
    x = y
    y = per
    fmt.Println (x, y)
}