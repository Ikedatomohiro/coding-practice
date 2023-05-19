package main

import (
    "bufio"
    "fmt"
    "os"
	"strings"
)

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
	inputs := strings.Split(scanner.Text(), " ")
	ym := inputs[0] + inputs[1]
	first := string([]rune(ym)[0])
	for i := 1; i < len(ym); i++ {
		if string([]rune(ym)[i]) != first {
			fmt.Println("No")
			os.Exit(0)
		}
	}
	fmt.Println("Yes")
	os.Exit(0)

	// var (y, m string)
	// fmt.Scan(&y, &m)
	// // fmt.Scan(&y)
	// // fmt.Scan(&m)
	// ym := y + m
	// fmt.Println(ym)
}