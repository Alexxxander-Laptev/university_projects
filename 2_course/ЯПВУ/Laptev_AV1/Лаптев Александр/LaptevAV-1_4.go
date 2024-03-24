package main
import ("fmt"
        
)

func main() {
    var ch = 269
    fmt.Println (ch)
    c := ch % 10
    b := ch / 10 % 10
    a := ch / 100
    sum := a + b + c
    fmt.Println (sum)
}