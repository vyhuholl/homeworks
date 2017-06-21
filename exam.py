def xml_process(text_name):
    f = open(text_name, 'r', encoding='utf-8')
    text = f.read()
    l = text.split('\n')
    l1 = []
    for tag in l:
        l1.append(tag)
    f.close()
    return l1
 
def ana_word (xml):
  anas = []
  for tag in xml:
    if tag startswith.('<w>'):
      anas.append(tag.count('<ana'))
  return (sum(anas))/(len(anas))

  def main():
    xml = text_process(text.xml)
    print(ana_word(xml))
