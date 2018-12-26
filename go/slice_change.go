package main

import "fmt"

/* slice并不是值传递，而是指针传递*/
func main() {
	a := []int{1, 2, 3, 4, 5, 6, 7, 8}
	b := changeSlice(a)
	fmt.Println(a)
	fmt.Println(b)
}

func changeSlice(param []int) []int {
	i := 0
	for _, v := range param {
		if v%2 != 0 {
			param[i] = v
			i++
		}
	}
	return param[:i]
}
