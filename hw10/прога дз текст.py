def text_process(text_name):
    f = open(text_name, 'r', encoding='utf-8')
    text = f.read()
    l = text.split()
    l1 = []
    for word in l:
        l1.append(word.strip('.,;:?![]{}'))
    f.close()
    return l1


def count_ness(text):
    list_ness = []
    for word in text:
        if word.endswith(ness):
            list_ness.append(word)
    return list_ness


def frequency(word, text):
    n = 0
    for i in text:
        if i == word:
            n += 1
    return n


def main():
    text = text_process('text.txt')
    words = {}
    for word in count_ness(text):
        words[word] = frequency(word, text)
    frequencies = word.values()
    print(len(count_ness(text)))
    print(max(frequencies))


main()