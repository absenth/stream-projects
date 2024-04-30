output = []
for n in range(1, 2000001):
    if (n) % 3 == 0 and (n) % 5 == 0:
        output.append("fizzbuzz")
    elif (n) % 3 == 0:
        output.append("fizz")
    elif (n) % 5 == 0:
        output.append("buzz")
    else:
        output.append(f"{n}")

print(output)
