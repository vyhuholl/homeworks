import os
import urllib.request

def download_page(pageUrl):
    page = urllib.request.urlopen(pageUrl)
    text = page.read().decode('ISO-8859-1')
    regTag = re.compile('<.*?>', re.DOTALL)
    regScript = re.compile('<script>.*?</script>', re.DOTALL)
    regComment = re.compile('<!--.*?-->', re.DOTALL)
    text = regScript.sub("", text)
    text = regComment.sub("", text)
    text = regTag.sub("", text)
    return text

Input = open('input.txt', 'w')
for i in range(1, 10):
    pageUrl = 'https://www.anekdot.ru/scripts/author_best.php?years=anekdot&page=' + str(i)
    text = download_page(pageUrl)
    print(text)
    Input.write(text + '\n')
os.system(r"C:\Users\student\mystem.exe input.txt output.txt")
