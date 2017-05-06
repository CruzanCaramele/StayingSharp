// compile as a standalone executable by delcaring package main
package main

import (
	"fmt"
	"runtime"
)

// main function, executable program's entry point
func main() {
	fmt.Println("Hello from", runtime.GOOS)
}