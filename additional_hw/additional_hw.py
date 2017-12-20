from flask import request
from flask import render_template
import urllib.request

regTag = re.compile('<.*?>', flags= re.DOTALL)
regPostWord = re.compile('<font color="#808080"></font>&nbsp;</td><td class="uu">', flags= re.DOTALL)

def mystem():
    os.system(r"mystem.exe " + "-d -e utf-8 " + 'input.txt' + " " + 'output.txt')
    return

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('utf-8')
        return text
    except:
        return('Error')

with open('dictionary.txt', 'w') as dictionary:
    common_url = 'http://www.dorev.ru/ru-index.html?xmmpoll='
    letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я']
    for i in letters:
        word_page = download_page(common_url + i)
        
    
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
