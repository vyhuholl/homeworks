import urllib.request

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('utf-8')
        return text
    except:
        return('Error')
  
links=['http://www.rosbalt.ru/style/2016/11/29/1571387.html', 'https://wek.ru/na-marse-nashli-zagadochnyj-labirint', 'https://www.kp.ru/daily/26612/3630125/', 'https://mir24.tv/news/15371682', 'https://www.m24.ru/articles/nauka/29112016/123422']
texts = []
for i in link:
  
