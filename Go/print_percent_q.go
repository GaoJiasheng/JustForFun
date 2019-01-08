package main

import "fmt"

func main() {
	a := 1
	b := 1.1
	c := "memeda"
	d := []string{"x", "y", "z"}
	e := map[string]bool{"o": true, "p": true, "q": true}
	fmt.Printf("%q\n%q\n%q\n%q\n%q\n", a, b, c, d, e)
}
