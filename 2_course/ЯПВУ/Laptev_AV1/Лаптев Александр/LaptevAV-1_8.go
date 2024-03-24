package main
import ("fmt"
        
)

func main() {
    var ch int
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&ch)
    c := ch / 10 % 10
    b := ch / 100 %10
    sum := b + c
    fmt.Println (sum)
}