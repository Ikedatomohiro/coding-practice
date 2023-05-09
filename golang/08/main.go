package main

import "fmt"

func main() {
	// var i int = 1
	// var f64 float64 = 1.2
	// var s string = "test"
	// var t bool = true
	// var f bool = false
	// var t, f bool = true, false

	var ( // この書き方は関数の外でも定義できる
		i int = 1
		f64 float64 = 1.2
		s string = "test"
		t, f bool = true, false
	)
	fmt.Println(i, f64, s, t, f)

	xi := 1 // この書き方は関数内でしか定義できない
	xi = 2
	x64 := 1.2
	xs := "test"
	xt, xf := true, false
	fmt.Println(xi, x64, xs, xt, xf)
	fmt.Printf("%T\n", f64)
	fmt.Printf("%T\n", xi)
}
