package main

import "fmt"

func main() {
	naturals := make(chan int)
	squares := make(chan int)

	// counter
	go func(ch chan<- int) {
		for x := 0; x <= 100; x++ {
			naturals <- x
		}
		close(ch)
	}(naturals)

	// squarer
	go func(chReceive <-chan int, chSend chan<- int) {
		for x := range chReceive {
			chSend <- x * x
		}
	}(naturals, squares)

	// printer
	for a := range squares {
		fmt.Println(a)
	}
}
