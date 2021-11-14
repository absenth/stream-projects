import time
import sys

#Start and end numbers
start_number = 1
end_number = 500000

#Record the test start time
start = time.time()

#Create variable to store the prime numbers and a counter
primes = []
noPrimes = 0

#Loop through each number, then through the factors to identify prime numbers
for candidate_number in range(start_number, end_number, 1):
    found_prime = True
    for div_number in range(2, candidate_number):
        if candidate_number % div_number == 0:
            found_prime = False
            break
    if found_prime:
        primes.append(candidate_number)
        noPrimes += 1

#Once all numbers have been searched, stop the timer
end = round(time.time() - start, 2)

#Display the results, uncomment the last to list the prime numbers found
print('Find all primes up to: ' + str(end_number))
print('Time elasped: ' + str(end) + ' seconds')
print('Number of primes found ' + str(noPrimes))
#print(primes)
