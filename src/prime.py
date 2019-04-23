import sys
import math

def isPrime(number):
    number = int(number)
    if number < 2:
        return False
    if number < 4:
        return True
    limit = int(math.sqrt(number)) + 1
    for i in range(2, limit):
        if number % i == 0:
            return False
    
    return True

for i in sys.argv[1:]:
    try:
        i = int(i)
        if isPrime(i):
            print(f'{i} is prime!')
        else:
            print(f'{i} is not prime')
    except ValueError as ex:
        print(f'\"{i}\" cannot be cast as an int: {ex}')