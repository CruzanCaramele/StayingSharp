package main

import (
	"fmt"
	"os"
)


func main() {

	for _, variable := range os.Environ(){
		fmt.Println(variable)
	}
	
}