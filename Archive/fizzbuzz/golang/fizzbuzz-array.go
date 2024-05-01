package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s []string
	for i := 1; i < 2000001; i++ {
		if i%3 == 0 && i%5 == 0 {
			s = append(s, "fizzbuzz")
		} else if i%3 == 0 {
			s = append(s, "fizz")
		} else if i%5 == 0 {
			s = append(s, "buzz")
		} else {
			s = append(s, strconv.Itoa(i))
		}
	}
	fmt.Println(s)
}
