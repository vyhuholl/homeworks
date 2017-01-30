import re


def text_process(text_name):
    f = open(text_name, 'r', encoding='utf-8')
    text = f.read()
    l = text.split()
    l1 = []
    for word in l:
        l1.append(word.strip('.,;:?![]'))
    f.close()
    return l1


def regexp(text):
    for word in text:
        if re.search('на(йти(сь)?|йд(ут?(ся)?|ё(((шь|т|м)(ся)?|(те(сь)?)))|и(сь)?|ите(сь)?|я(сь)?|ённый)|ш(ёл(ся)?|ла(сь)?|ло(сь)?|ли(сь)?|едши((сь)?|й(ся)?))' , word):
            print(word)


def main():
    text = text_process('text.txt')
    regexp(text)

main()