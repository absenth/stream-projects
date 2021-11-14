import time
import sys
from joblib import Parallel, delayed

def runMultiTask(s,e, jobs=8):
    #Record the test start time
    start = time.time()
    
    scopeSize = (e-s+1)/(jobs*2)
    
    startBoundary = s
    endBoundary   = e
    firstResidual = 0
    lastResidual  = 0

    tasks = []
    for t in range(0,jobs):
        first = int(round(startBoundary + scopeSize + firstResidual))
        firstResidual = startBoundary + scopeSize + firstResidual - first
        
        last  = int(round(endBoundary - scopeSize - lastResidual))
        lastResidual = last - (endBoundary - scopeSize - lastResidual)
        
        tasks.append([(startBoundary, first, 1),
                      (last, endBoundary, 1)])
    
        startBoundary = first
        endBoundary = last
    
    def batchTasks(l):
        return [p for ps in [runTask(*t) for t in l] for p in ps]
    
    taskPrimes = Parallel(n_jobs=jobs)(delayed(batchTasks)(task) for task in tasks)    

    primes = [p for ps in taskPrimes for p in ps]

    #Once all numbers have been searched, stop the timer
    end = round(time.time() - start, 2)

    #Display the results, uncomment the last to list the prime numbers found
    print('Find all primes up to: ' + str(e))
    print('Number of threads: 8')
    print('Time elasped: ' + str(end) + ' seconds')
    print('Number of primes found ' + str(len(primes)))
    #print(primes)

def runSingleTask(s,e):
    #Record the test start time
    start = time.time()

    primes = runTask(s,e,1)

    #Once all numbers have been searched, stop the timer
    end = round(time.time() - start, 2)

    #Display the results, uncomment the last to list the prime numbers found
    print('Find all primes up to: ' + str(e))
    print('Time elasped: ' + str(end) + ' seconds')
    print('Number of primes found ' + str(len(primes)))
    #print(primes)

def runTask(s,e,i):

    #Start and end numbers
    start_number = s
    end_number = e

    #Create variable to store the prime numbers and a counter
    primes = []
    noPrimes = 0

    #Loop through each number, then through the factors to identify prime numbers
    for candidate_number in range(start_number, end_number, i):
        found_prime = True
        for div_number in range(2, candidate_number):
            if candidate_number % div_number == 0:
                found_prime = False
                break
        if found_prime:
            primes.append(candidate_number)
            noPrimes += 1
    
    return primes


tasks = [(1,10000), (1,100000), (1,200000), (1,500000)]

#for task in tasks:
#    runSingleTask(*task)
    
for task in tasks:
    runMultiTask(*task, 4)    
