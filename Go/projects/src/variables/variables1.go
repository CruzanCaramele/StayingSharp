package main

// to check types, reflect package is used
import (
	"fmt"
	"reflect"
)

var (
	module 		 float64
	name, course string
)


func main() {
	fmt.Println("Name is set to:", name, "type is:", reflect.TypeOf(name))
	fmt.Println("Module is set to:", module, "type is:", reflect.TypeOf(module))
}