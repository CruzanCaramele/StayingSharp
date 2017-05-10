package main

import (
	"fmt"
)


func main() {
	// Declare a slice called myCourses
	myCourses := make([]string, 5, 10) //[]string{"Docker", "Puppet"}

	fmt.Printf("\nLength is: %d. \nCapacity is: %d",
		        len(myCourses), cap(myCourses))
}