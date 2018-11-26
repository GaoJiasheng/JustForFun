package main

import (
	"fmt"
)

type MyCircularQueue struct {
	Head   int
	Tail   int
	Length int
	Body   []int
}

/** Initialize your data structure here. Set the size of the queue to be k. */
func Constructor(k int) MyCircularQueue {
	return MyCircularQueue{
		Head:   0,
		Tail:   -1,
		Length: k,
		Body:   make([]int, k),
	}
}

func (this *MyCircularQueue) nextNode(idx int) int {
	if idx < this.Length-1 {
		return idx + 1
	}
	if idx == this.Length-1 {
		return 0
	} else {
		fmt.Println("this is imposibble")
		return -1
	}
}

/** Insert an element into the circular queue. Return true if the operation is successful. */
func (this *MyCircularQueue) EnQueue(value int) bool {
	if this.IsFull() {
		return false
	}

	nextTail := this.nextNode(this.Tail)
	this.Body[nextTail] = value
	this.Tail = nextTail
	return true
}

/** Delete an element from the circular queue. Return true if the operation is successful. */
func (this *MyCircularQueue) DeQueue() bool {
	if this.IsEmpty() {
		return false
	}

	if this.Head == this.Tail {
		// if only one element in queue
		this.Head = 0
		this.Tail = -1
	} else {
		this.Head = this.nextNode(this.Head)
	}
	return true
}

/** Get the front item from the queue. */
func (this *MyCircularQueue) Front() int {
	/*
		if this.IsEmpty() {
			return -1
		}

		value := this.Body[this.Head]
		if this.Head == this.Tail {
			// if only one element in queue
			this.Head = 0
			this.Tail = -1
		} else {
			this.Head = this.nextNode(this.Head)
		}
	*/
	value := this.Body[this.Head]
	return value
}

/** Get the last item from the queue. */
func (this *MyCircularQueue) Rear() int {
	/*
		if this.IsEmpty() {
			return -10
		}

		value := this.Body[this.Tail]
		if this.Head == this.Tail {
			// if only one element in queue
			this.Head = 0
			this.Tail = -1
		} else {
			tail := this.Tail - 1
			if tail < 0 {
				tail = 2
			}
		}
	*/
	var value int
	if this.IsEmpty() {
		value = -1
	} else {
		value = this.Body[this.Tail]
	}
	return value
}

/** Checks whether the circular queue is empty or not. */
func (this *MyCircularQueue) IsEmpty() bool {
	if this.Tail == -1 {
		return true
	}
	return false
}

/** Checks whether the circular queue is full or not. */
func (this *MyCircularQueue) IsFull() bool {
	if this.Tail >= 0 && this.nextNode(this.Tail) == this.Head {
		return true
	}
	return false
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.EnQueue(value);
 * param_2 := obj.DeQueue();
 * param_3 := obj.Front();
 * param_4 := obj.Rear();
 * param_5 := obj.IsEmpty();
 * param_6 := obj.IsFull();
 */
func main() {
	Q := Constructor(6)
	fmt.Println(Q.EnQueue(6))
	fmt.Println(Q.Rear())
	fmt.Println(Q.Rear())
	fmt.Println(Q.DeQueue())
	fmt.Println(Q.EnQueue(5))
	fmt.Println(Q.Rear())
	fmt.Println(Q.DeQueue())
	fmt.Println(Q.Front())
	fmt.Println(Q.DeQueue())
	fmt.Println(Q.DeQueue())
	fmt.Println(Q.DeQueue())
}
