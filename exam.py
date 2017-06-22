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

def instrumentalis(xml):
    for tag in xml:
        if 'ins' in tag and 'gr="S' in tag:
            for word in xml[(xml.index(tag) - 3),(xml.index(tag) + 3)]

  def main():
    xml = text_process(text.xml)
    print(ana_word(xml))
    dictionary = dict_parts_of_speech(xml)
    d = open('dict.txt', 'w')
    for i in dictionary:
        d.write(i + '\t' + dictionary[i] + '\n')
