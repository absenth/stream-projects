# first attempt ever at solving FizzBuzz
# https://wiki.c2.com/?FizzBuzzTest

for n in range(1, 2000001):
    if (n) % 3 == 0 and (n) % 5 == 0:
        print("fizzbuzz")
    elif (n) % 3 == 0:
        print("fizz")
    elif (n) % 5 == 0:
        print("buzz")
    else:
        print(n)
