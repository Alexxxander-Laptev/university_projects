package main
import ("fmt"
        "math"
)

func main() {
    var k float64
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&k)
    pi := 3.14159265
    al_r := math.Atan(k)
    al := (pi / 2 - al_r) * 180 / pi
    fmt.Println (al)
}
