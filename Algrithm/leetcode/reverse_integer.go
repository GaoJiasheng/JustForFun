package main

import (
	"fmt"
	"strconv"
	"strings"
)

/*
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
*/

func reverse_1(num int) int {
	numString := strconv.Itoa(num)
	sign := ""
	if strings.HasPrefix(numString, "-") {
		sign = "-"
	}
	absNum := strings.TrimLeft(numString, "-")
	resNum := sign
	for i := len(absNum) - 1; i >= 0; i-- {
		resNum = resNum + string(absNum[i])
	}
	numRet, _ := strconv.Atoi(resNum)
	return numRet
}

func reverse_2(num int) int {
	res := 0
	for num != 0 {
		res = res*10 + num%10
		if res > int(^uint32(0)>>1) || res < ^(int(^uint32(0)>>1)) {
			return 0
		}
		num = num / 10
	}
	return res
}

func main() {
	reverse := reverse_2
	fmt.Println(12345, reverse(12345))
	fmt.Println(-12345, reverse(-12345))
}
