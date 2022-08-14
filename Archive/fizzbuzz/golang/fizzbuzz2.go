package main

import (
	"os"
	"strconv"
)

func main() {
	for i := 1; i < 15000001; i++ {
		if i%3 == 0 && i%5 == 0 {
			os.Stdout.Write([]byte("fizzbuzz"))
		} else if i%3 == 0 {
			os.Stdout.Write([]byte("fizz"))
		} else if i%5 == 0 {
			os.Stdout.Write([]byte("buzz"))
		} else {
			os.Stdout.Write([]byte(strconv.Itoa(i)))
		}
	}
}
