import random
words = ['парник', 'порка', 'дротик', 'висюлька', 'генофонд']
words_dict = {'парник': ['теплица', 'тёплый'], 'порка': ['ремнём', 'плетью', 'кнутом', 'розгами'], 'дротик': ['метательный', 'дартса'], 'висюлька': ['украшение', 'безделушка'], 'генофонд': ['популяции', 'нации', 'человека']}
word = random.choice(words)
s = ''
for letter in word:
    s += '.'
s += ' '
s += random.choice(words_dict[word])
print(s)
guess = input()
if guess == word:
    print('Да')
else:
    print('Нет')