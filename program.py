import random
number = random.randint(0,9)
guess = random.randint(0,9)
print(guess)
if guess == number:
    print('Yes')
else:
    print('No')
    if guess > number:
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')
    guess = random.randint(0,9)
    print(guess)
    if guess == number:
        print('Yes')
    else:
        print('No')
