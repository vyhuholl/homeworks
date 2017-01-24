def text_process(text_name):
    f = open(text_name, 'r', encoding='utf-8')
    text = f.read()
    l = text.split()
    l1 = []
    for word in l:
        l1.append(word.strip('.,;:?![]{}'))
    f.close()
    return l1


def freq_dict(text):
    dictionary = {}
    for word in text:
        freq = 0
        for i in text:
            if i == word:
                freq += 1
        dictionary[word] = freq
    return dictionary


def main():
    text = text_process(text.txt)
    dictionary = freq_dict(text)
    word = input()
    print(dictionary[word])
