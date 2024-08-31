for n in range(2000001):
    match n % 3, n % 5:
        case 0, 0:
            print("fizzbuzz")
        case 0, _:
            print("fizz")
        case _, 0:
            print("buzz")
        case _, _:
            print(n)
