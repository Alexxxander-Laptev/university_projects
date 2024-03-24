package main
import ("fmt"
        
)

func main() {
    var ch = 156
    fmt.Println (ch)
    c := ch % 10
    b := ch / 10 % 10
    a := ch / 100
    fmt.Println (a, b, c)
}