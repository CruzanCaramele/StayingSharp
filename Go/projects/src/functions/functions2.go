/*
Variadic functions:
when unsure of how many variables a function will recieve,
variadic functions can be used.
*/


package main

import (
	"fmt"
)

func main() {
	
	bestFinish := bestLeagueFinish(9,4,6,19,10,13,10,17,14,16)
	fmt.Println(bestFinish)
}

func bestLeagueFinish(finishes ...int) int {
	
	best := finishes[0]

	for _, i := range finishes {
		if i < best {
			best = i
		}
	}
	return best
}