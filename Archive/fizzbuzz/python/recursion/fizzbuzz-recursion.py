from sys import setrecursionlimit


setrecursionlimit(2000001)


def fizzbuzz(n):
    match n % 3, n % 5:
        case 0, 0:
            print("fizzbuzz")
        case 0, _:
            print("fizz")
        case _, 0:
            print("buzz")
        case _, _:
            print(n)
    n += 1

    if n == 2000001:
        return

    fizzbuzz(n)


fizzbuzz(1)
