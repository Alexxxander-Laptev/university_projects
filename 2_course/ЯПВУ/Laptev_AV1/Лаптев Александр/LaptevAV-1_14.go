package main
import ("fmt"
        "math"
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
    pi := 3.14159265
    c_al := (math.Pow(b, 2) + math.Pow(c, 2) - math.Pow(a, 2)) / (2 * b * c)
    al := math.Acos(c_al)
    fmt.Println (al * 180 / pi)
    c_bet := (math.Pow(a, 2) + math.Pow(c, 2) - math.Pow(b, 2)) / (2 * a * c)
    bet := math.Acos(c_bet)
    fmt.Println (bet * 180 / pi)
    c_gam := (math.Pow(b, 2) + math.Pow(a, 2) - math.Pow(c, 2)) / (2 * b * a)
    gam := math.Acos(c_gam)
    fmt.Println (gam * 180 / pi)
}