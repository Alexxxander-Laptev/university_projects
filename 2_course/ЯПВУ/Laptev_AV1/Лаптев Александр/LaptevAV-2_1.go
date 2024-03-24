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
    if (a == 0) && (b != 0){
        fmt.Print ("Uravnenie ne imeet resheniyi")
    }  else if (a == 0) && (b == 0) {
        fmt.Print ("Uravnenie imeet beskonechnoe mnojestvo resheniyi")
    } else {
        fmt.Print (b / a)
    }
}
