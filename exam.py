import re

def xml_process(text_name):
    f = open(text_name, 'r', encoding='utf-8')
    text = f.read()
    l = text.split('\n')
    l1 = []
    for tag in l:
        l1.append(tag)
    f.close()
    return l1
 
def ana_word(xml):
  anas = []
  for tag in xml:
    if tag startswith.('<w>'):
      anas.append(tag.count('<ana'))
  return (sum(anas))/(len(anas))

def dict_parts_of_speech(xml):
    dictionary = {}
    l = []
    for tag in xml:
        part = re.findall('gr=".*,', tag)
        l += part
    for tag in part:
        tag.lstrip('gr="')
        tag.rstrip(',')
        dictionary[tag] += 1
    return(dictionary)

def instrumentalis(tag):
    s = ''
    if 'ins' in tag and 'gr="S' in tag:
        for word in xml[(xml.index(tag) - 3),(xml.index(tag) - 1)]:
            s += word.strip('<.*>') + ' '
        for word in xml[(xml.index(tag))]:
            s += '\t' + word.strip('<.*>') + '\t'
        for word in xml[(xml.index(tag) + 1),(xml.index(tag) + 3)]:
            s += word.strip('<.*>') + ' '
        s += '\n'
     return s

  def main():
    xml = text_process(text.xml)
    print(ana_word(xml))
    dictionary = dict_parts_of_speech(xml)
    d = open('dict.txt', 'w')
    for i in dictionary:
        d.write(i + '\t' + dictionary[i] + '\n')
    ins = open('ins.txt', 'w')
    for tag in xml:
        ins.write(instrumentalis(tag))
    d.close()
    ins.close()
 
main()
