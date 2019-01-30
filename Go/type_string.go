package main

import "fmt"

type a struct {
	A string
	B string
}

type b struct {
	A string
	B string
}

func (a a) String() string {
	return "[Type a]--" + a.A + "--" + a.B
}

func main() {
	tempA := a{"testA", "testB"}
	tempB := b{"testA", "testB"}
	fmt.Println(tempA)
	fmt.Println(tempB)
}
