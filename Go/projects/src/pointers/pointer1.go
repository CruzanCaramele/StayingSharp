package main

import (
	"fmt"
	"reflect"
)


/*
using '&' to reference a pointer
using '*' to de-reference a pointer
*/


func main() {
	name   := "Hamza"
	module := 3.2

	// pointer varialble
	ptr    := &module

	fmt.Println("\nName is: ", name, " and is of type: ", reflect.TypeOf(name))
	fmt.Println("\nModule is: ", module, " and is of type: ", reflect.TypeOf(module))

	// print the pointer value of variable module (it's memory address)
	fmt.Println("\nMemory address of *module* variable is: ", &module)

	// de-refercing the ptr variable to get the value of module
	fmt.Println("\nMemory address of *module* variable is(repeat) : ", ptr,
				" and the value of *module* variable is: ", *ptr)
}