package main
import ("fmt"
        
)

func main() {
    var ch int
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&ch)
    d := ch % 10
    c := ch / 10 % 10
    b := ch / 100 %10
    a := ch / 1000
    fmt.Println (d, c, b, a)
}