package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) > 1 {
		fmt.Println(os.Args[0])
	} else {
		fmt.Println("Hello I am Gopher")
	}

}
