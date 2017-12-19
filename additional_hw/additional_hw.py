from flask import request
from flask import render_template
from pymystem3 import Mystem
import urllib.request

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('utf-8')
        return text
    except:
        return('Error')

with open('dictionary.txt', 'w') as dictionary:
    common_url = 'http://www.dorev.ru/ru-index.html?xmmpoll='
    letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э]']
    
m = Mystem()
regTag = re.compile('<.*?>', flags= re.DOTALL)

app = Flask(__name__)

@app.route('127.0.0.1/<name>')
def main_page(name=None):
    return render_template('main_page.html', name=name)

@app.route('127.0.0.1/news')
def news_page(name=None):
    meduza = download_page('https://meduza.io')
    meduza_clean = regTag.sub('', meduza)
    return render_template('news_page.html', name=name)

@app.route('127.0.0.1/test')
def test_page(name=None):
    return render_template('test_page.html', name=name)
