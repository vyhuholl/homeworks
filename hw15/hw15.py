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


def create_dict(text):
  dictionary = {sentence: {word: len(word) for word in sentence} for sentence in text}

def main():
  text = text_process('text.txt')
  return(create_dict(text))

main()
