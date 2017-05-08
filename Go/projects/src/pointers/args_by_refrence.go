package main

import (
	"fmt"
)


func main() {
	name   := "Hamza"
	course := "Chemistry"

	fmt.Println("\nHi ", name, "you're watching ", course, " course")

	// send the variable's (course) pointer
	changeCourse(&course)
	fmt.Println("\nOriginal course changed to ==>", course)
}


func changeCourse(course *string) string {
	// assign new value to the location in memory that course pointer references
	*course = "First Look: Native Docker Clustering"

	fmt.Println("\nTrying to change course to ==>", *course)

	return *course
}