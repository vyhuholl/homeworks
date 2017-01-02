import random
n = open('nouns.txt', 'r')
nouns = [line.strip() for line in n]
v = open('verbs.txt', 'r')
verbs = [line.strip() for line in v]
c = open('clitics.txt', 'r')
clitics = [line.strip() for line in c]
n2 = open('nouns2.txt', 'r')
nouns2 = [line.strip() for line in n2]
p = open('marks.txt', 'r')
punctuation = [line.strip() for line in p]
i = open('imperative.txt', 'r')
imperative = [line.strip() for line in i]
def verse1:
    return (random.choice(nouns)+ ' ' + random.choice(verbs) + ' ' + random.choice(nouns) + ' ' + random.choice(punctuation))
def verse2:
    return(random.choice(imperative) + ' ' + random.choice(nouns) + ' ' + random.choice(clitics) + ' ' + random.choice(nouns2) + ' ' + random.choice(punctiation))                                                                                                                           seq))
def verse3:
    return (random.choice(clitics) + ' ' + random.choice(nouns2) + ' ' + random.choice(verbs) + ' ' + random.choice(nouns) + ' ' + random.choice(punctuation))
def make_verse:
    verse = random.choice([1,2,3])
    if verse == 1:
        return verse1()
    elif verse == 2:
        return verse2()
    else:
        return verse3()
for n in range(4):
    print(make_verse)