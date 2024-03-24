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
    var d float64
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&d)
    if ((a <= c) && (b <= d)) || ((a <= d) && (b <= c)) {
        fmt.Print ("Da, mojet")
    } else {
        fmt.Print ("Net, ne mojet")
    }
}