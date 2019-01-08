package main

import (
	"fmt"
	"os"
)

/*
go run console_args.go 1 2 3 4 5 6
*/

func main() {
	var s, sep string
	for i := 1; i < len(os.Args); i++ {
		s += sep + os.Args[i]
		sep = ", "
	}
	fmt.Println(s)
}
