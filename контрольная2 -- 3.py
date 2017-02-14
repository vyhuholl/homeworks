import re

def corpus_process(text_name):
    f = open(text_name, 'r')
    text = f.read()
    l = []
    for line in text:
        l.append(line)
    f.close()
    return l

def count_frequency(word, text):
    n = 0
    for s in text:
        if word in s:
            n += 1
    return n

def count_adj(text):
    dictionary = {}
    for s in text:
        if re.search('type=l.f.*', text) != None:
            wordtype = s
            number = wordtype.find('type=')
            wordtype = wordtype[number, len(s)]
            wordtype.replace('type="', '')
            number2 = wordtype.find('"')
            wordtype = wordtype[0, number]
            wordtype = '"' + wordtype
            n = count_frequency(wordtype, text)
            dictionary[wordtype] = n
    return dictionary

def write_in_file(corpus):
    dictionary = count_adj(corpus)
    adjectives = open('adjectives.txt', 'w')
    for i in dictionary:
        adjectives.write(i + ' ' + dictionary[i] + '\n')
    adjectives.close()

def main():
    corpus = corpus.process('corpus.xml')
    write_in_file(corpus)
    corpus1 = corpus
    n1 = corpus1.index('<body>')
    n2 = corpus1.index('</body>')
    for s in corpus1[n1 + 1, n2 - 1]:
        s = re.sub('<w lemma=', '', s)
        s = re.sub('" type="', ', ', s)
        s = re.sub('">', ', ', s)
        s = re.sub('</w>', '', s)
    corpus1_file = open(corpus1.txt, 'w')
    for i in corpus1:
        corpus1_file.write(i + '\n')
    corpus1_file.close()

main()
