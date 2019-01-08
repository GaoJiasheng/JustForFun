package main

import (
	"flag"
	"fmt"
	"strings"
)

/*
 * go build flag.go && ./flag -s - -n a b c
 */
var n = flag.Bool("n", false, "omit trailing newline")
var sep = flag.String("s", " ", "seperator")

func main() {
	flag.Parse()
	fmt.Print(strings.Join(flag.Args(), *sep))
	if !*n {
		fmt.Println()
	}
}
