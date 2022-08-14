# usage: awk -v n=38  -f fizzbuzzNoDiv.awk
#
# FizzBuzz using no division & no modulo-operations:
BEGIN {
    if(!n) n=15000000
    print "# FizzBuzz:"
    while (c1<n) {
	  c1++; c3++; c5++; cF++; x=sprintf("%3d ",c1)
	  if(c3>= 3) { c3=0; x="Fizz " }
          if(c5>= 5) { c5=0; x="Buzz " }
	  if(cF>=15) { cF=0; x="FizzBuzz\n" }
	  printf(x)
    }
    print "\n# Done."
}
