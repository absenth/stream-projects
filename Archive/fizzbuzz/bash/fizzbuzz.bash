#!/bin/bash

for n in $(seq 2000000)
do
    if (( $n % 15 == 0 )); then
        echo "fizzbuzz"
    elif (( $n % 3 == 0 )); then
        echo "fizz"
    elif (( $n % 5 == 0 )); then
        echo "buzz"
    else
        echo $n
    fi
done
