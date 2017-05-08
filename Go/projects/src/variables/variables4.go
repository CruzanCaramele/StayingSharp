package main

import (
	"fmt"
	"os"
)


func main() {
	name   := os.Getenv("USER")
	course := "Docker Deep Dive"

	fmt.Println("\nHi ", name, "you're watching ", course, " course")

	// send the variable's (course) pointer
	changeCourse(&course)
	fmt.Println("\nOriginal course changed to ==>", course)
}

func changeCourse(course *string) string {

	*course = "Chemistry"
	fmt.Println("\nChanging course to...", *course)

	return *course
}