import random

def rebus():
    cod = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    number = random.choice(cod)
    return number
result = []
numbers = rebus()
int(numbers)
for i in range(1, numbers):
    for j in range(i + 1, numbers):
        if numbers % (i + j) == 0:
            cod2 = [i, j]
            result.append(cod2)
print('Для числа: ', numbers, 'все  пароли: ', result)


# второй вариант
import random


def rebus():
    cod = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    number = random.choice(cod)
    return number


result = ''
numbers = rebus()
int(numbers)
for i in range(1, numbers):
    for j in range(i + 1, numbers):
        if numbers % (i + j) == 0:
            result += str(i)
            result += str(j)
print('Для числа: ', numbers, 'все  пароли: ', result)

