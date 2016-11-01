import random
number = random.randint(0,9)
guess = int(input())
while guess != number:
    print('No')
    if guess < number:
        print ('больше')
    else:
        print ('меньше')
    guess = int(input())
print('Yes')
