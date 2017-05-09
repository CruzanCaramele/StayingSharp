package main

import (
	"fmt"
	"math/rand"
	"time"
)


func main() {
	// assign random value to variable
	tmpNum := random()

	// determine if tmpNum is even or odd number
	switch tmpNum {
		case 0, 2, 4, 6, 8:
			fmt.Println("\nThis is an even Number ", tmpNum)
		case 1, 3, 5, 7, 9:
			fmt.Println("\nThis is an odd Number ", tmpNum)
	}
}


func random() int {
	rand.Seed(time.Now().Unix())
	return rand.Intn(10)
}



