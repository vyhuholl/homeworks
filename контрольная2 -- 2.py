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

def lemma_dict(text):
    dictionary = {}
    for s in text:
        if '<w lemma=' in s:
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

def main():
    corpus = corpus_process('corpus.xml')
    keys = open('keys.txt', 'w')
    dictionary = lemma_dict(corpus)
    l = dictionary.keys()
    for key in l:
        keys.write(key + '\n')
    keys.close()

main()
            
