import strutils
var Results: array[1..2000000, string]

for n in 1..2000000:
  if n mod 15 == 0:
    Results[n] = "fizzbuzz"
  elif n mod 3 == 0:
    Results[n] = "fizz"
  elif n mod 5 == 0:
    Results[n] = "buzz"
  else:
    Results[n] = intToStr(n)

echo Results
