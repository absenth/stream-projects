package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s []string
	for i := 1; i < 2000001; i++ {
		if i%3 == 0 && i%5 == 0 {
			s = append(s, "fizzbuzz \n")
		} else if i%3 == 0 {
			s = append(s, "fizz \n")
		} else if i%5 == 0 {
			s = append(s, "buzz \n")
		} else {
			n := strconv.Itoa(i)
			o := fmt.Sprintf("%s \n", n)
			s = append(s, o)
		}
	}
	fmt.Println(s)
}
