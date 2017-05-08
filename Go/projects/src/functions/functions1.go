package main

import (
	"fmt"
	"strings"
)


func main() {
	
	author := "hamza yahaya"
	module := "docker deep dive"

	fmt.Println(converter(author, module))
}


// this returns 2 strings of type strings
func converter(author, module string) (s1, s2 string) {
	
	author = strings.ToUpper(author)
	module = strings.Title(module)

	return author, module
}