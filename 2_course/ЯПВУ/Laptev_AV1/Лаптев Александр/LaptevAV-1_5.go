package main
import ("fmt"
        
)

func main() {
    var ch int
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&ch)
    c := ch % 10
    b := ch / 10 % 10
    a := ch / 100
    pr := a * b * c
    fmt.Println (pr)
}