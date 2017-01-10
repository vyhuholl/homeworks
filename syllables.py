def text_process(text_name):
    f = open(text_name, 'r', encoding='utf-8')
    text = f.read()
    l = text.split()
    l1 = []
    for word in l:
        l1.append(word.strip('.,;:?!'))
    f.close()
    return l1


def count_syllables(word):
    n = 0
    for i in word:
        if i in 'аеёиоуыэюяАЕЁИОУЫЭЮЯ':
            n +=1
    return n


def starting_letter(word):
    return(word[0])
    

def main():
    l = text_process('text.txt')
    n = input()
    if n in '123456789':
        n = int(n)
        for word in l:
            if count_syllables(word) == n:
                print(word)
    elif n in 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
        for word in l:
            if starting_letter(word) == n:
                print(word)


main()
