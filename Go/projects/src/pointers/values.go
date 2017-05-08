package main

import (
	"fmt"
)


func main() {
	name   := "Hamza"
	course := "Chemistry"

	fmt.Println("\nHi ", name, "you're watching ", course, " course")

	changeCourse(course)
	fmt.Println("\nOriginal course is still ==>", course)
}


func changeCourse(course string) string {
	// assigning a new value to an existing variable
	course = "First Look: Native Docker Clustering"

	fmt.Println("\nTrying to change your course to ==>", course)

	return course
}

