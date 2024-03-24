package main
import ("fmt"
        "math"
)

func main() {
    var a float64 = 15.0
    var b float64 = 10.0
    var c float64 = 25.0
    var pr float64 = a * b * c
    var st float64 = 1.0 / 3.0
    var geom float64 = math.Pow(pr, float64(st))
    fmt.Println (geom)
}