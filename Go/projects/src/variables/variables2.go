package main

import (
	"fmt"
	"reflect"
)

// type inference
// package level varaibles, global in scope, available to all functions
var (
	name   = "Hamza"
	course = "Advanced Go"
	module = 3.2
)

func main() {
	fmt.Println("Name is:", name, "Type is:", reflect.TypeOf(name))
	fmt.Println("Enrolled in:", course, "Type is:", reflect.TypeOf(course))
	fmt.Println("In module:", module, "Type is:", reflect.TypeOf(modul)e)
}