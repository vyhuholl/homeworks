import random
words = ['������', '�����', '������', '��������', '��������']
words_dict = {'������': ['�������', '�����'], '�����': ['�����', '������', '������', '�������'], '������': ['�����������', '������'], '��������': ['���������', '����������'], '��������': ['���������', '�����', '��������']}
word = random.choice(words)
s = ''
for letter in word:
    s += '.'
s += ' '
s += random.choice(words_dict[word])
print(s)
guess = input()
if guess == word:
    print('��')
else:
    print('���')