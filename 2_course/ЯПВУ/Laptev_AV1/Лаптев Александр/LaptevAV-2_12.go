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
    if (((a > b) && (b > c) && (a > c)) || ((c > b) && (b > a) && (c > a))) {
        y := b
        fmt.Println (y)
    } else if (((b > a) && (a > c) && (b > c)) || ((c > a) && (a > b) && (c > b))) {
        y := a
        fmt.Println (y)
    } else if (((a > c) && (c > b) && (a > b)) || ((b > c) && (c > a) && (b > a))) {
        y := c
        fmt.Println (y)
    } else {
        fmt.Println ("Nekorrektniyi vvod")
    }
}