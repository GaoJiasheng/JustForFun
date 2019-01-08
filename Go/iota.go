package main

import (
	"fmt"
)

const (
	FlagUp int = iota
	FlagDown
	FlagLeft
	FlagRight
	FlagMiddle
)

type Weekday int

const (
	_ Weekday = iota * 10
	Monday
	Tuesday
	Wednesday
	Thursday
	Friday
	Saturday
	Sunday
)

const (
	_ = 1 << (10 * iota)
	KiB
	MiB
	GiB
	RiB
	PiB
	EiB
	ZiB
	YiB
)

func main() {
	fmt.Println(FlagUp, FlagDown, FlagLeft, FlagRight, FlagMiddle)
	fmt.Println(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
	// will panic
	// fmt.Println(KiB, MiB, GiB, RiB, PiB, EiB, ZiB, YiB)
}
