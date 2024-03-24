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
    if (a == b) && (b == c) && (a == c) {
        fmt.Print ("Nomer chisla, otlichnogo ot ostalnih: 4")
    } else if (a == c) && (c == d) && (a == d) {
        fmt.Print ("Nomer chisla, otlichnogo ot ostalnih: 2")
    }  else if (a == b) && (b == d) && (a == d) {
        fmt.Print ("Nomer chisla, otlichnogo ot ostalnih: 3")
    } else if (b == c) && (c == d) && (b == d) {
        fmt.Print ("Nomer chisla, otlichnogo ot ostalnih: 1")
    } else {
        fmt.Print ("Nekorrektniyi vvod")
    }
}