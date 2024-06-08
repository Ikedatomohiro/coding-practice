package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	var s = strings.Split(sc.Text(), " ")

	for l := range s {
		fmt.Println(s[l])
	}
}
