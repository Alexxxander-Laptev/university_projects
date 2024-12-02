package main
import ("fmt"
        
)

func Max_1(a, b float64) float64 {
    if (a < b) {
        return (b)
    }
    return (a)
}
func Max_2(a, b, c float64) float64 {
    if ((a < b) && (b < c) && (a < c)) {
        return (c)
    } else if ((c < b) && (b < a) && (c < a)) {
        return (a)
    }
    return (b)
}
func Max_3(a, b, c float64) float64 {
    if ((a - b) > (b - c)) {
        return (a - b)
    }
    return (b - c)
}

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
    m := Max_1(a, b)
    n := Max_2(a, b, c)
    k := Max_3(a, b, c)
    y := (m + n) / (k + a + b + c)
    fmt.Print (y)
}