package main

import (
	"fmt"
	"sync"
)

func main() {
	a := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	wg := sync.WaitGroup{}

	for i := range a {
		wg.Add(1)
		go func() {
			fmt.Println(a[i])
			wg.Done()
		}()
	}

	wg.Wait()
	fmt.Println("---------------------------")

	for i := range a {
		x := i
		wg.Add(1)
		go func() {
			fmt.Println(a[x])
			wg.Done()
		}()
	}
	wg.Wait()
}
