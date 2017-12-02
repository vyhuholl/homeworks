import urllib.request

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('utf-8')
        return text
    except:
        return('Error')

regTag = re.compile('<.*?>', flags= re.DOTALL)
links=['http://www.rosbalt.ru/style/2016/11/29/1571387.html', 'https://wek.ru/na-marse-nashli-zagadochnyj-labirint', 'https://www.kp.ru/daily/26612/3630125/', 'https://mir24.tv/news/15371682', 'https://www.m24.ru/articles/nauka/29112016/123422']
texts = []
for i in links:
    page = download_page(i)
    page = regTag.sub('', page)
    texts.append(set(page))

with open('ans_1.txt', 'w') as ans_1:
    ans_1.write(texts[0] | texts[1] | texts[2] | texts[3] | texts[4])
    ans_1.close()

with open('ans_2.txt', 'w') as ans_2:
    ans_2.write(texts[0] ^ texts[1] ^ texts[2] ^ texts[3] ^ texts[4])
    ans_2.close()
