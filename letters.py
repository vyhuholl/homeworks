def text_process(text_name):
    f = open(text_name, 'r', encoding='utf-8')
    text = f.read()
    l = text.split()
    l1 = []
    for word in l:
        l1.append(word.strip('.,;:?!'))
    f.close()
    return l1

def count(text, letter, letter2):
    n = 0
    for word in text:
        if word.startswith(letter) or word.startswith(letter2):
            n += 1
    return n

def letters_dict(text):
    dictionary = {}
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'
    for letter in alphabet:
        letter2 = ALPHABET[alphabet.find(letter)]
        dictionary[letter] = count(text, letter, letter2)

def main():
    text = text_process('text.txt')
    dictionary = letters_dict(text)
    text2 = open('text2.tsv', 'w')
    for letter in dictionary:
    text2.write(letter + '\t' + str(dictionary[letter]))
    text2.close()

main()
