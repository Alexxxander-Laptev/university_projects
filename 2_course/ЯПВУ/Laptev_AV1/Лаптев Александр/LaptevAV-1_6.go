package main
import ("fmt"
        
)

func main() {
    var ch int
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&ch)
    b := ch % 10
    a := ch / 1000
    sum := a + b
    fmt.Println (sum)
}