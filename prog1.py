import os

def new_sentence(sentence):
  sentence1 = ''
  for word in sentence:
    sentence1 += word.strip('.,;:?!') + ' '
    sentence1 += '.'
    return sentence1

def text_process(text_name):
  f = open(text_name, 'r', encoding='utf-8')
  text = f.read()
  text = text.replace('!','.')
  text = text.replace('?', '.')
  text = text.replace('...','.')
  l = text.split(.)
  l1 = [new_sentence(sentence) for sentence in text]
  f.close()
  return l1

def count_longest(text):
    n = 0
    longest = []
    for sent in text:
        sent1 = sent.split(' ')
        if len(sent1) > n:
            longest = sent1
            n = len(sent1)
    return longest

def create_folders(sent):
    sent = '/'.join(sent)
    os.makedirs(sent)

def main():
    text = text_process('text.txt'):
    sent = count_longest(text)
    create_folders(sent)

main()
