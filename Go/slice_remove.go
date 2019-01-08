package main

import (
	"fmt"
)

/* slice只是一种引用，使用copy函数把后半段拷贝到前面，然后返回len-1即可*/
func remove(slice []int, idx int) []int {
	copy(slice[idx:], slice[idx+1:])
	return slice[:len(slice)-1]
}

func main() {
	a := []int{0, 1, 2, 3, 4, 5}
	a = remove(a, 2)
	fmt.Println(a)
}
