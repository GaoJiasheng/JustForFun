package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	a := "我爱工作，工作使我快乐"
	fmt.Println(a)
	fmt.Println(a[0], a[1], a[2])
	fmt.Println(len(a))
	fmt.Println(utf8.RuneCountInString(a))

	// 下标式的拿字符串，不一定能符合预期
	// 因为utf-8的字符所占用的字节长度不定
	for i := range a {
		fmt.Printf("%q ", a[i])
	}
	fmt.Println()

	// range是隐式的包含了对utf-8的操作
	for _, r := range a {
		fmt.Printf("%q ", r)
	}
	fmt.Println()

	// 不符合预期的字符
	fmt.Println(string(1234567))
}
