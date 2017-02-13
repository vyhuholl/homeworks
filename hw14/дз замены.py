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

def replace(text):
    for word in text:
        if word == 'викинг(и|a(х)?|ов|у|ам(и)?|ом|е)?':
            word = re.sub('викинг', 'бурундук', word)
    return text

def main():
    text = text_process('text.txt')
    text_replaced = replace(text)
    return ' '.join(text_replaced)