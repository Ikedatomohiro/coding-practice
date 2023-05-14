package main

import (
	"fmt"
	"strconv"
)
func main() {
	var x int = 1
	xx := float64(x)
	fmt.Printf("%T %v %f\n", xx, xx, xx)

	var y float64 = 1.2
	yy := int(y)
	fmt.Printf("%T %v %d\n", yy, yy, yy)

	var s string = "14"
	// z = int(s) intにキャストできない
	i, _ := strconv.Atoi(s) // Atoiは値とerrを返り値とする。errで受け取るとその後に使わなかった時にエラーとなる。_ならつかわなくても良い
	fmt.Printf("%T %v\n", i, i)

	h := "Hello World"
	fmt.Println(string(h[0]))
}
