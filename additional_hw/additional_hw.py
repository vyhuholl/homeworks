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

m = Mystem()

app = Flask(__name__)

@app.route('127.0.0.1/<name>')
def main_page(name=None):
    return render_template('main_page.html', name=name)

@app.route('127.0.0.1/news')
def news_page(name=None):
    return render_template('news_page.html', name=name)

@app.route('127.0.0.1/test')
def test_page(name=None):
    return render_template('test_page.html', name=name)
