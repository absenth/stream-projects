package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s [2000000]string
	for i := 1; i < 2000001; i++ {
		if i%3 == 0 && i%5 == 0 {
			s[i-1] = "fizzbuzz \n"
		} else if i%3 == 0 {
			s[i-1] = "fizz \n"
		} else if i%5 == 0 {
			s[i-1] = "buzz \n"
		} else {
			n := strconv.Itoa(i)
			o := fmt.Sprintf("%s \n", n)
			s[i-1] = o
		}
	}
	fmt.Println(s)
}
