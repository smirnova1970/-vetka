numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_primes = 'True'
for i in numbers:
    for j in range(2,i):
        k = i / j
        if k % 1 == 0 and k != 1:
            is_primes = 'False'
            break
        else:
            is_primes = 'True'
    if is_primes == 'True' and i != 1:
        primes.append(i)
    if is_primes == 'False' and i != 1:
        not_primes.append(i)
print('Primes: ',primes)
print('Not Primes: ',not_primes)


