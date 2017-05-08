package main

import (
	"fmt"
	"reflect"
)

// variables inside functions are only available to those functions
func main() {
	a := 10.00000
	b := 3

	fmt.Println("\nA is of type: ", reflect.TypeOf(a),
				" and B is of type: ", reflect.TypeOf(b))

	c := int(a) + b 

	fmt.Println("\nC has value:", c, "and is of type", reflect.TypeOf(c))
}