word = input()
newword = ''
for a in word:
    if a != '�' and a != '�':
        newword += a
newword = newword[::-1]
print(newword)