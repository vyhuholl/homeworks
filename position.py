def text_process(text_name):
    f = open(text_name, 'r', encoding='utf-8')
    text = f.read()
    l = text.split()
    l1 = []
    for word in l:
        l1.append(word.strip('.,;:?!'))
    f.close()
    return l1

def position_dict(text):
    dictionary = {}
    for word in text:
        dictionary[word] == text.index[word]
    return(dictionary)

def main():
    text = text_process('text.txt')
    dictionary = position_dict(text)
    s = 'Слово {} находится на месте номер {} \n'
    text2 = open('text2.txt', 'w')
    for word in dictionary:
        text2.write(s.format(word, str(dictionary[word])))
    text2.close()

main()
