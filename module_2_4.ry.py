numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_primes = 'True'
for i in range(1, len(numbers)):
    current = numbers[i]
    for j in range(2, i):
        if current % j == 0:
            is_primes = False
            break
        else:
            is_primes = True
    if is_primes:  #
        primes.append(current)
    else:
        not_primes.append(current)
print('Primes: ', primes)
print('Not Primes: ', not_primes)

