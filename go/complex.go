package main

import (
	"fmt"
	"math/cmplx"
)

func main() {
	var x complex128 = complex(1, 2)
	fmt.Println(x)
	fmt.Println(1i)
	fmt.Println(1i * 1i)
	fmt.Println(cmplx.Sqrt(-1))
}
