package main

import "fmt"

func main() {
	testMap := map[string]bool{
		"a": true,
		"b": true,
		"c": true,
		"d": true,
		"e": true,
		"f": true,
	}
	/* map删除用delete*/
	delete(testMap, "a")

	/* map不存在的key的删除与读取都没问题*/
	fmt.Println(testMap["g"])
	delete(testMap, "g")
}
