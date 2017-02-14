f = open('corpus.xml', 'r')
n = 0
for line in f:
    n += 1
f1 = open('number.txt', 'w')
f1.write(str(n))
f.close()
f1.close()
