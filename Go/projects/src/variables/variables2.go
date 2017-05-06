package main

import (
	"fmt"
	"reflect"
)

var (
	name, course, module = "Hamza", "Advanced Go", 3.2
)

func main() {
	fmt.Println("Name is:", name, "Type is:", reflect.TypeOf(name))
	fmt.Println("Enrolled in:", course, "Type is:", reflect.TypeOf(course))
	fmt.Println("In module:", module, "Type is:", reflect.TypeOf(module))
}