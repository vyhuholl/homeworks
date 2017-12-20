from flask import request
from flask import render_template
import urllib.request
import os
import html

regTag = re.compile('<.*?>', flags= re.DOTALL)
regSpace = re.compile('\s\s*', re.DOTALL)
regScript = re.compile('<script>.*?</script>', re.DOTALL)
regComment = re.compile('<!--.*?-->', re.DOTALL)


def mystem():
    os.system(r"mystem.exe " + "-d -e utf-8 " + 'input.txt' + " " + 'output.txt')
    return()

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('utf-8')
        return text
    except:
        return('Error')
    
def lemmatize(text):
    mystem()
    file = open('output.txt', 'r', encoding = 'utf-8')
    text = file.read()
    text = text.replace ('{', ' ')
    text = text.replace ('}', ' ')    
    text = text.replace ('?', '')
    text = text.split()
    new_text = ''
    for i in range(1, len(text), 2):
        new_word = one_word(text[i], dictionary)
        new_text = new_text + new_word + ' '
    return new_text
    
def clean_text(text):
    clean_t = text.replace ('&nbsp;', '')
    clean_t = regScript.sub(" ", clean_t)
    clean_t = regComment.sub(" ", clean_t)
    clean_t = regTag.sub(" ", clean_t)
    clean_t = regSpace.sub(' ', clean_t)
    html.unescape(clean_t)
    return clean_t
       
app = Flask(__name__)

@app.route('127.0.0.1/')

@app.route('127.0.0.1/<name>')
def main_page(name=None):
    page = download_page('https://yandex.ru/pogoda/10463')
    weather = re.search('<time class="time fact__time"(.*?)<dl class="term fact__water">', text)
    weather = regTag.sub ('\n', weather.group())
    weather = regSpace.sub (' ', clean_weather)
    return render_template('main_page.html', weather=weather)

@app.route('127.0.0.1/news')
def news_page(name=None):
    meduza = download_page('https://meduza.io')
    file = open('input.txt','w', encoding = 'utf-8')
    clean_meduza = clean_text(meduza)
    file.write(clean_meduza)
    file.close()
    clean_meduza = lemmatize()
    return render_template('news_page.html', meduza = clean_meduza)

@app.route('127.0.0.1/test')
def test_page(name=None):
    return render_template('test_page.html', name=name)

@app.route('127.0.0.1/result')
def result_page(name=None):
    return render_template('result_page.html', new_word = new_word)

@app.route('127.0.0.1/score')
def test_result_page(name=None):
    return render_template('test_result_page.html', score = score)
