#!/usr/bin/env python3


def main():
    i=1;

    while i in range(1,15000000):
        if (i) %3 == 0 and (i) %5 == 0:
            print("fizzbuzz")
        elif (i) %3 == 0:
            print("fizz")
        elif (i) %5 == 0:
            print("buzz")
        else:
            print(i)
        i=i+1


if __name__ == '__main__':
    main()
