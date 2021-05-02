# first attempt ever at solving FizzBuzz
# https://wiki.c2.com/?FizzBuzzTest

for n in range(100000):
    if (n+1) %3 == 0 and (n+1) %5 == 0:
        print("fizzbuzz")
    elif (n+1) %3 == 0:
        print("fizz")
    elif (n+1) %5 == 0:
        print("buzz")
    else:
        print(n+1)
