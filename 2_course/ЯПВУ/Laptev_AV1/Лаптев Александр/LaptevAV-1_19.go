package main
import ("fmt"
        
)

func main() {
    var x int
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&x)
    c := x % 10
    b := x / 10 % 10
    a := x / 100
    if a == b {
        fmt.Print ("TRUE")
    } else if a == c {
        fmt.Print ("TRUE")
    } else if b == c {
        fmt.Print ("TRUE")
    } else if (a == b) && (b == c) && (a == c) {
        fmt.Print ("TRUE")
    } else {
        fmt.Print ("FALSE")
    }
}
