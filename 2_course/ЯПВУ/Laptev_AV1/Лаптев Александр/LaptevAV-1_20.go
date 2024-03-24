package main
import ("fmt"
        
)

func main() {
    var x int
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&x)
    c := x % 10
    a := x / 100
    if a == c {
        fmt.Print ("TRUE")
    }  else {
        fmt.Print ("FALSE")
    }
}
