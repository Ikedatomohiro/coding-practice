package main

import (
	"fmt"
	"strings"
)
func main() {
	fmt.Println("Hello World!")
	fmt.Println("Hello" + "World!")
	fmt.Println(string("Hellot World"[0]))

	var s string = "Hello World!"
	fmt.Println(strings.Replace(s, "H", "X", 1))
	fmt.Println(s)
	fmt.Println(strings.Contains(s, "World"))
	fmt.Println("Test\n" +
		"Test")
	fmt.Println(`Test
		test
	Test`)
	fmt.Println("\"")
	fmt.Println(`"`)
	fmt.Println(`\"`)

}
