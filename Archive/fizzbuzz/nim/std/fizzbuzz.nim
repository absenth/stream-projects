for n in 1..2000000:
  if n mod 15 == 0:
    echo "fizzbuzz"
  if n mod 3 == 0:
    echo "fizz"
  if n mod 5 == 0:
    echo "buzz"
  else:
    echo n
