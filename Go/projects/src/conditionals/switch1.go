package main

import (
	"fmt"
)

func main() {
	
	switch "docker" { 
		case "linux":
			fmt.Println("\nTake the RHCE Course")
		case "docker":
			fmt.Println("\nTake the Kubernetes course")
		case "windows":
			fmt.Println("\nIn this day and age?")
		default:
			fmt.Println("\nSave your future.")
	}
}