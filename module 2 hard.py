import random

def rebus():
    cod = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    number = random.choice(cod)
    return number
result = []
devider = []
numbers = rebus()
int(numbers)
for k in range(1,21):
    if numbers % k == 0 and k < numbers:
        devider.append(k)
for i in devider:
    b = numbers - i
    cod1 = [i,b]
    result.append(cod1)
for j in range(2, numbers):
    a = numbers - i
    cod2 = [j,a]
    result.append(cod2)
print('Для числа: ', numbers, 'все  пароли: ', result)



