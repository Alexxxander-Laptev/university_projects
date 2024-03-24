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
    x, y = y, x
    fmt.Println (x, y)
}