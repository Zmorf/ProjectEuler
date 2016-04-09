def isPrime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i*i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i = i + 6
    return True


primeSum = 0
for x in range(2000000):
    if isPrime(x):
        primeSum = primeSum + x

print primeSum
