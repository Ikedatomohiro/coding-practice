package main

import (
	"fmt"
	"os/user"
	"time"
)

func main() {
	fmt.Println("Hello world!", "TEST TEST", time.Now())
	fmt.Println(user.Current())
}
