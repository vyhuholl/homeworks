word = input()
newword = ''
for a in word:
    if a != 'ç' and a != 'ÿ':
        newword += a
newword = newword[::-1]
print(newword)