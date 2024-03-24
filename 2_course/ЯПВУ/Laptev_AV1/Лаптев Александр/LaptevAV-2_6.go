package main
import ("fmt"
        
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
    var d float64
    fmt.Println ("Vvedite chislo: ")
    fmt.Scan (&d)
    if (a <= 0) || (b <= 0) || (c <= 0) || (d <= 0) {
        fmt.Print ("Nekorrektnie dannie")
    } else if (a == c) && (b == d) {
        fmt.Print ("Mojno postroit pryamoygolnik s takimi storonami")
    } else {
        fmt.Print ("Nelzya postroit pryamoygolnik s takimi storonami")
    }
}